from __future__ import annotations

import functools
import itertools

import hail as hl
import luigi

from v03_pipeline.lib.annotations.enums import annotate_enums
from v03_pipeline.lib.annotations.fields import get_fields
from v03_pipeline.lib.paths import (
    remapped_and_subsetted_callset_path,
    sample_lookup_table_path,
    valid_reference_dataset_collection_path,
)
from v03_pipeline.lib.tasks.base.base_variant_annotations_table import (
    BaseVariantAnnotationsTableTask,
)
from v03_pipeline.lib.tasks.update_sample_lookup_table import (
    UpdateSampleLookupTableTask,
)
from v03_pipeline.lib.vep import run_vep


class UpdateVariantAnnotationsTableWithNewSamplesTask(BaseVariantAnnotationsTableTask):
    callset_path = luigi.Parameter()
    project_guids = luigi.ListParameter()
    project_remap_paths = luigi.ListParameter()
    project_pedigree_paths = luigi.ListParameter()
    ignore_missing_samples = luigi.BoolParameter(
        default=False,
        parsing=luigi.BoolParameter.EXPLICIT_PARSING,
    )
    liftover_ref_path = luigi.OptionalParameter(
        default='gs://hail-common/references/grch38_to_grch37.over.chain.gz',
        description='Path to GRCh38 to GRCh37 coordinates file',
    )
    vep_config_json_path = luigi.OptionalParameter(
        default=None,
        description='Path of hail vep config .json file',
    )

    def requires(self) -> list[luigi.Task]:
        return [
            *super().requires(),
            UpdateSampleLookupTableTask(
                self.env,
                self.reference_genome,
                self.dataset_type,
                self.hail_temp_dir,
                self.callset_path,
                self.project_guids,
                self.project_remap_paths,
                self.project_pedigree_paths,
                self.ignore_missing_samples,
            ),
        ]

    def complete(self) -> bool:
        return super().complete() and hl.eval(
            hl.all(
                [
                    hl.read_table(self.output().path).updates.contains(
                        hl.Struct(callset=self.callset_path, project_guid=project_guid),
                    )
                    for project_guid in self.project_guids
                ],
            ),
        )

    def update_table(self, ht: hl.Table) -> hl.Table:
        callset_hts = [
            hl.read_matrix_table(
                remapped_and_subsetted_callset_path(
                    self.env,
                    self.reference_genome,
                    self.dataset_type,
                    self.callset_path,
                    project_guid,
                ),
            ).rows()
            for project_guid in self.project_guids
        ]
        callset_ht = functools.reduce(
            (lambda ht1, ht2: ht1.union(ht2, unify=True)),
            callset_hts,
        )
        callset_ht = callset_ht.distinct()

        # 1) Get new rows and annotate with vep
        new_variants_ht = callset_ht.anti_join(ht)
        new_variants_ht = run_vep(
            new_variants_ht,
            self.env,
            self.reference_genome,
            self.dataset_type,
            self.vep_config_json_path,
        )

        # 2) Get handles on rdc hts:
        annotatable_rdc_hts = {
            f'{rdc.value}_ht': hl.read_table(
                valid_reference_dataset_collection_path(
                    self.env,
                    self.reference_genome,
                    rdc,
                ),
            )
            for rdc in self.dataset_type.annotatable_reference_dataset_collections
        }
        joinable_rdc_hts = {
            f'{rdc.value}_ht': hl.read_table(
                valid_reference_dataset_collection_path(
                    self.env,
                    self.reference_genome,
                    rdc,
                ),
            )
            for rdc in self.dataset_type.joinable_reference_dataset_collections(
                self.env,
            )
        }

        # 3) Select down to the formatting annotations fields and
        # anyreference dataset collection annotations.
        new_variants_ht = new_variants_ht.select(
            **get_fields(
                new_variants_ht,
                self.dataset_type.formatting_annotation_fns,
                annotatable_rdc_hts,
                **self.param_kwargs,
            ),
        )

        # 4) Join against the reference dataset collections that are not "annotated".
        for rdc_ht in joinable_rdc_hts.values():
            new_variants_ht = new_variants_ht.join(rdc_ht, 'left')

        # 5) Union with the existing variant annotations table
        # and annotate with the sample lookup table.
        ht = ht.union(new_variants_ht, unify=True)
        ht = ht.annotate(
            **get_fields(
                ht,
                self.dataset_type.sample_lookup_table_annotation_fns,
                {
                    'sample_lookup_ht': hl.read_table(
                        sample_lookup_table_path(
                            self.env,
                            self.reference_genome,
                            self.dataset_type,
                        ),
                    ),
                },
                **self.param_kwargs,
            ),
        )

        # 6) Fix up the globals.
        ht = ht.annotate_globals(
            paths=hl.Struct(),
            versions=hl.Struct(),
            enums=hl.Struct(),
        )
        for rdc_ht in itertools.chain(
            annotatable_rdc_hts.values(),
            joinable_rdc_hts.values(),
        ):
            rdc_globals = rdc_ht.index_globals()
            ht = ht.annotate_globals(
                paths=hl.Struct(
                    **ht.globals.paths,
                    **rdc_globals.paths,
                ),
                versions=hl.Struct(
                    **ht.globals.versions,
                    **rdc_globals.versions,
                ),
                enums=hl.Struct(
                    **ht.globals.enums,
                    **rdc_globals.enums,
                ),
            )
        ht = annotate_enums(ht, self.dataset_type)

        # 6) Mark the table as updated with these callset/project pairs.
        return ht.annotate_globals(
            updates=ht.updates.union(
                {
                    hl.Struct(callset=self.callset_path, project_guid=project_guid)
                    for project_guid in self.project_guids
                },
            ),
        )
