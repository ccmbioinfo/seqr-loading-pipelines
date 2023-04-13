#!/usr/bin/env python3
import argparse
import os

import hail as hl

from hail_scripts.reference_data.combine import get_ht, update_joined_ht_globals
from hail_scripts.reference_data.config import GCS_PREFIXES
from hail_scripts.utils.hail_utils import write_ht, import_table

INTERVAL_REFERENCE_HT_PATH = 'combined_interval_reference/combined_interval_reference.GRCh{genome_version}.ht'

def run(environment: str, dataset: str):
    genome_version = '38'
    destination_path = os.path.join(GCS_PREFIXES[environment], INTERVAL_REFERENCE_HT_PATH).format(
        environment=environment,
        genome_version=genome_version,
    )
    ht = import_table(destination_path)
    dataset_ht = get_ht(dataset, genome_version)
    ht.transmute({dataset: dataset_ht})
    ht = update_joined_ht_globals(ht)
    ht = ht.annotate_globals(screenRegionTypeLookup=SCREEN_REGION_TYPE_LOOKUP)
    print(f'Uploading ht to {destination_path}')
    write_ht(ht, destination_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--environment',
        default='dev',
        choices=['dev', 'prod']
    )
    parser.add_argument(
        '--dataset',
        choices=['gnomad_non_coding_constraint', 'screen'],
        required=True,
    )
    args, _ = parser.parse_known_args()
    run(args.environment, args.dataset)
