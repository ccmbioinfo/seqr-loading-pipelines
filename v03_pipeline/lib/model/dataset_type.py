from __future__ import annotations

from enum import Enum
from typing import Callable

import hail as hl

from v03_pipeline.lib.annotations import gcnv, mito, shared, snv, sv
from v03_pipeline.lib.model.definitions import AccessControl, Env, ReferenceGenome
from v03_pipeline.lib.model.reference_dataset_collection import (
    ReferenceDatasetCollection,
)

MITO_MIN_HOM_THRESHOLD = 0.95
ZERO = 0.0


class DatasetType(Enum):
    GCNV = 'GCNV'
    MITO = 'MITO'
    SNV = 'SNV'
    SV = 'SV'

    @property
    def annotatable_reference_dataset_collections(
        self,
    ) -> list[ReferenceDatasetCollection]:
        return {
            DatasetType.SNV: [
                ReferenceDatasetCollection.INTERVAL,
            ],
            DatasetType.MITO: [
                ReferenceDatasetCollection.INTERVAL_MITO,
            ],
        }.get(self, [])

    def joinable_reference_dataset_collections(
        self,
        env: Env,
    ) -> list[ReferenceDatasetCollection]:
        rdcs = {
            DatasetType.SNV: [
                ReferenceDatasetCollection.COMBINED,
                ReferenceDatasetCollection.HGMD,
            ],
            DatasetType.MITO: [
                ReferenceDatasetCollection.COMBINED_MITO,
            ],
        }.get(self, [])
        if env == Env.LOCAL:
            return [rdc for rdc in rdcs if rdc.access_control == AccessControl.PUBLIC]
        return rdcs

    def table_key_type(
        self,
        reference_genome: ReferenceGenome,
    ) -> hl.tstruct:
        default_key = hl.tstruct(
            locus=hl.tlocus(reference_genome.value),
            alleles=hl.tarray(hl.tstr),
        )
        return {
            DatasetType.GCNV: hl.tstruct(variant_id=hl.tstr),
            DatasetType.SV: hl.tstruct(rsid=hl.tstr),
        }.get(self, default_key)

    @property
    def col_fields(
        self,
    ) -> list[str]:
        return {
            DatasetType.SNV: [],
            DatasetType.MITO: ['contamination', 'mito_cn'],
            DatasetType.SV: [],
            DatasetType.GCNV: [],
        }[self]

    @property
    def entries_fields(
        self,
    ) -> list[str]:
        return {
            DatasetType.SNV: ['GT', 'AD', 'GQ'],
            DatasetType.MITO: ['GT', 'DP', 'MQ', 'HL'],
            DatasetType.SV: ['GT', 'CONC_ST', 'GQ', 'RD_CN'],
            DatasetType.GCNV: [
                'any_ovl',
                'defragmented',
                'genes_any_overlap_Ensemble_ID',
                'genes_any_overlap_totalExons',
                'identical_ovl',
                'is_latest',
                'no_ovl',
                'sample_start',
                'sample_end',
                'CN',
                'GT',
                'QS',
            ],
        }[self]

    @property
    def row_fields(
        self,
    ) -> list[str]:
        return {
            DatasetType.SNV: ['rsid', 'filters'],
            DatasetType.MITO: [
                'rsid',
                'filters',
                'common_low_heteroplasmy',
                'hap_defining_variant',
                'AF_het',
                'AC_het',
                'AN',
                'mitotip_trna_prediction',
                'vep',
            ],
            DatasetType.SV: ['locus', 'alleles', 'filters', 'info'],
            DatasetType.GCNV: [
                'cg_genes',
                'chr',
                'end',
                'filters',
                'gene_ids',
                'lof_genes',
                'num_exon',
                'sc',
                'sf',
                'start',
                'strvctvre_score',
                'svtype',
            ],
        }[self]

    @property
    def excluded_filters(self) -> hl.SetExpression:
        return {
            DatasetType.SNV: hl.empty_set(hl.tstr),
            DatasetType.MITO: hl.set(['PASS']),
            DatasetType.SV: hl.set(['PASS', 'BOTHSIDES_SUPPORT']),
            DatasetType.GCNV: hl.empty_set(hl.tstr),
        }[self]

    @property
    def has_sample_lookup_table(self) -> bool:
        return self in {DatasetType.SNV, DatasetType.MITO}

    @property
    def has_gencode_mapping(self) -> dict[str, str]:
        return self == DatasetType.SV

    @property
    def sample_entries_filter_fn(self) -> Callable[[hl.StructExpression], bool]:
        return {
            DatasetType.GCNV: lambda e: hl.is_defined(e.GT),
        }.get(self, lambda e: e.GT.is_non_ref())

    @property
    def can_run_validation(self) -> bool:
        return self == DatasetType.SNV

    @property
    def veppable(self) -> bool:
        return self == DatasetType.SNV

    @property
    def sample_lookup_table_fields_and_genotype_filter_fns(
        self,
    ) -> dict[str, Callable[hl.MatrixTable, hl.Expression]]:
        return {
            DatasetType.SNV: {
                'ref_samples': lambda mt: mt.GT.is_hom_ref(),
                'het_samples': lambda mt: mt.GT.is_het(),
                'hom_samples': lambda mt: mt.GT.is_hom_var(),
            },
            DatasetType.MITO: {
                'ref_samples': lambda mt: hl.is_defined(mt.HL) & (mt.HL == ZERO),
                'heteroplasmic_samples': lambda mt: (
                    (mt.HL < MITO_MIN_HOM_THRESHOLD) & (mt.HL > ZERO)
                ),
                'homoplasmic_samples': lambda mt: mt.HL >= MITO_MIN_HOM_THRESHOLD,
            },
        }[self]

    @property
    def formatting_annotation_fns(self) -> list[Callable[..., hl.Expression]]:
        return {
            DatasetType.SNV: [
                snv.gnomad_non_coding_constraint,
                snv.screen,
                shared.rg37_locus,
                shared.rsid,
                shared.sorted_transcript_consequences,
                shared.variant_id,
                shared.xpos,
            ],
            DatasetType.MITO: [
                mito.common_low_heteroplasmy,
                mito.haplogroup,
                mito.high_constraint_region,
                mito.mitotip,
                shared.rg37_locus,
                mito.rsid,
                shared.sorted_transcript_consequences,
                shared.variant_id,
                shared.xpos,
            ],
            DatasetType.SV: [
                sv.algorithms,
                sv.bothsides_support,
                sv.cpx_intervals,
                sv.end_locus,
                sv.gt_stats,
                sv.gnomad_svs,
                shared.rg37_locus,
                sv.rg37_locus_end,
                sv.sorted_gene_consequences,
                sv.start_locus,
                sv.strvctvre,
                sv.sv_type_id,
                sv.sv_type_detail_id,
                shared.xpos,
            ],
            DatasetType.GCNV: [
                gcnv.end_locus,
                gcnv.gt_stats,
                gcnv.num_exon,
                gcnv.rg37_locus,
                gcnv.rg37_locus_end,
                gcnv.sorted_gene_consequences,
                gcnv.start_locus,
                gcnv.strvctvre,
                gcnv.sv_type_id,
                gcnv.xpos,
            ],
        }[self]

    @property
    def genotype_entry_annotation_fns(self) -> list[Callable[..., hl.Expression]]:
        return {
            DatasetType.SNV: [
                shared.GQ,
                snv.AB,
                snv.DP,
                shared.GT,
            ],
            DatasetType.MITO: [
                mito.contamination,
                mito.DP,
                mito.HL,
                mito.mito_cn,
                mito.GQ,
                shared.GT,
            ],
            DatasetType.SV: [
                sv.CN,
                sv.concordance,
                shared.GQ,
                shared.GT,
            ],
            DatasetType.GCNV: [
                gcnv.defragged,
                gcnv.new_call,
                gcnv.prev_call,
                gcnv.prev_overlap,
                gcnv.sample_end,
                gcnv.sample_gene_ids,
                gcnv.sample_num_exon,
                gcnv.sample_start,
                gcnv.CN,
                gcnv.GT,
                gcnv.QS,
            ],
        }[self]

    @property
    def sample_lookup_table_annotation_fns(self) -> list[Callable[..., hl.Expression]]:
        return {
            DatasetType.SNV: [
                snv.gt_stats,
            ],
            DatasetType.MITO: [
                mito.gt_stats,
            ],
        }[self]
