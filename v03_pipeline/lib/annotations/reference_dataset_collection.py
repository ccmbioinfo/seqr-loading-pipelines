from __future__ import annotations

from typing import Any

import hail as hl

from v03_pipeline.lib.model import (
    DatasetType,
    Env,
    ReferenceDatasetCollection,
    ReferenceGenome,
)
from v03_pipeline.lib.paths import reference_dataset_collection_path


def hgmd(
    t: hl.Table | hl.MatrixTable,
    env: Env,
    reference_genome: ReferenceGenome,
    dataset_type: DatasetType,
    **_: Any,
) -> hl.Expression:
    hgmd_ht = hl.read_table(
        reference_dataset_collection_path(
            env,
            reference_genome,
            ReferenceDatasetCollection.HGMD,
        ),
    )
    key = t.row_key if hasattr(t, 'row_key') else t.key
    return hgmd_ht[key].hgmd


def gnomad_non_coding_constraint(
    t: hl.Table | hl.MatrixTable,
    env: Env,
    reference_genome: ReferenceGenome,
    **_: Any,
) -> hl.Expression:
    interval_reference_ht = hl.read_table(
        reference_dataset_collection_path(
            env,
            reference_genome,
            ReferenceDatasetCollection.INTERVAL_REFERENCE,
        ),
    )
    return hl.Struct(
        z_score=(
            interval_reference_ht.index(t.locus, all_matches=True)
            .filter(
                lambda x: hl.is_defined(x.gnomad_non_coding_constraint['z_score']),
            )
            .gnomad_non_coding_constraint.z_score.first()
        ),
    )


def screen(
    t: hl.Table | hl.MatrixTable,
    env: Env,
    reference_genome: ReferenceGenome,
    **_: Any,
) -> hl.Expression:
    interval_reference_ht = hl.read_table(
        reference_dataset_collection_path(
            env,
            reference_genome,
            ReferenceDatasetCollection.INTERVAL_REFERENCE,
        ),
    )
    return hl.Struct(
        region_type_ids=(
            interval_reference_ht.index(
                t.locus,
                all_matches=True,
            ).flatmap(
                lambda x: x.screen['region_type_ids'],
            )
        ),
    )
