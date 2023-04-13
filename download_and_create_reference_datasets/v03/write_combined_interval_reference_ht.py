#!/usr/bin/env python3
import argparse
import os

import hail as hl

from hail_scripts.reference_data.combine import join_hts
from hail_scripts.reference_data.config import GCS_PREFIXES, SCREEN_REGION_TYPE_LOOKUP
from hail_scripts.utils.hail_utils import write_ht

DATASETS = ['gnomad_non_coding_constraint', 'screen']
INTERVAL_REFERENCE_HT_PATH = 'combined_interval_reference/combined_interval_reference.GRCh{genome_version}.ht'
VERSION = '1.0.0'

def run(environment: str):
    genome_version = '38'
    ht = join_hts(
        DATASETS,
        VERSION,
        reference_genome=genome_version,
    )
    destination_path = os.path.join(GCS_PREFIXES[environment], INTERVAL_REFERENCE_HT_PATH).format(
        environment=environment,
        genome_version=genome_version,
    )
    print(f'Uploading ht to {destination_path}')
    write_ht(ht, destination_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--environment',
        default='dev',
        choices=['dev', 'prod']
    )
    args, _ = parser.parse_known_args()
    run(args.environment)
