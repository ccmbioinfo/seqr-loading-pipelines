import hail as hl

MOCK_VEP_DATA = hl.struct(
    allele_string='G/A',
    ancestral=hl.null('str'),
    assembly_name='GRCh37',
    colocated_variants=hl.array(
        [
            hl.struct(
                aa_allele='A',
                aa_maf=0.0685,
                afr_allele='A',
                afr_maf=0.06566,
                allele_string='G/A',
                amr_allele='A',
                amr_maf=0.0038,
                clin_sig=hl.null('str'),
                ea_allele='A',
                ea_maf=0.015,
                eas_allele='A',
                eas_maf=0.0259,
                end=881918,
                eur_allele='A',
                eur_maf=0.0,
                exac_adj_allele='A',
                exac_adj_maf=0.02117,
                exac_afr_allele='A',
                exac_afr_maf=0.046,
                exac_allele='A',
                exac_amr_allele='A',
                exac_amr_maf=0.01143,
                exac_eas_allele='A',
                exac_eas_maf=0.047,
                exac_fin_allele='A',
                exac_fin_maf=0.0002325,
                exac_maf=0.0616,
                exac_nfe_allele='A',
                exac_nfe_maf=0.0264,
                exac_oth_allele='A',
                exac_oth_maf=0.06086,
                exac_sas_allele='A',
                exac_sas_maf=0.04032,
                id='rs35471880',
                minor_allele='A',
                minor_allele_freq=0.0294,
                phenotype_or_disease=hl.null('str'),
                pubmed=hl.null('str'),
                sas_allele='A',
                sas_maf=0.0567,
                somatic=hl.null('str'),
                start=881918,
                strand=1,
            ),
        ],
    ),
    context=hl.null('str'),
    end=881918,
    id='1_881918_G/A',
    input='1\t881918\t.\tG\tA\t.\t.\tGT',
    intergenic_consequences=hl.null('str'),
    most_severe_consequence='missense_variant',
    motif_feature_consequences=hl.null('str'),
    regulatory_feature_consequences=hl.null('str'),
    seq_region_name='1',
    start=881918,
    strand=1,
    transcript_consequences=hl.array(
        [
            hl.struct(
                allele_num=1,
                amino_acids='S/L',
                biotype='protein_coding',
                canonical=1,
                ccds='CCDS3.1',
                cdna_end=1717,
                cdna_start=1717,
                cds_end=1667,
                cds_start=1667,
                codons='tCg/tTg',
                consequence_terms=hl.array(['missense_variant']),
                distance=hl.null('int32'),
                domains=hl.array(
                    [
                        hl.struct(db='hmmpanther', name='PTHR12687'),
                        hl.struct(db='hmmpanther', name='PTHR12687'),
                        hl.struct(db='Pfam_domain', name='PF03715'),
                        hl.struct(
                            db='Superfamily_domains',
                            name='SSF48371',
                        ),
                    ],
                ),
                exon='15/19',
                gene_id='ENSG00000188976',
                gene_pheno=hl.null('int32'),
                gene_symbol='NOC2L',
                gene_symbol_source='HGNC',
                hgnc_id='24517',
                hgvs_offset=hl.null('int32'),
                hgvsc='ENST00000327044.6:c.1667C>T',
                hgvsp='ENSP00000317992.6:p.Ser556Leu',
                impact='MODERATE',
                intron=hl.null('str'),
                lof='LC',
                lof_filter='END_TRUNC,INCOMPLETE_CDS',
                lof_flags=hl.null('str'),
                lof_info='INTRON_END:881781,EXON_END:881925,EXON_START:881782,DE_NOVO_DONOR_MES:-7.36719797135343,DE_NOVO_DONOR_PROB:0.261170618766552,DE_NOVO_DONOR_POS:-138,INTRON_START:881667,DE_NOVO_DONOR_MES_POS:-138,MUTANT_DONOR_MES:4.93863747168278',
                minimised=1,
                polyphen_prediction='benign',
                polyphen_score=0.311,
                protein_end=556,
                protein_id='ENSP00000317992',
                protein_start=556,
                sift_prediction='deleterious',
                sift_score=0.01,
                strand=-1,
                swissprot='Q9Y3T9',
                transcript_id='ENST00000327044',
                trembl=hl.null('str'),
                uniparc='UPI000041820C',
                variant_allele='A',
            ),
            hl.struct(
                allele_num=1,
                amino_acids=hl.null('str'),
                biotype='protein_coding',
                canonical=hl.null('int32'),
                ccds=hl.null('str'),
                cdna_end=hl.null('int32'),
                cdna_start=hl.null('int32'),
                cds_end=hl.null('int32'),
                cds_start=hl.null('int32'),
                codons=hl.null('str'),
                consequence_terms=hl.array(['downstream_gene_variant']),
                distance=1963,
                domains=hl.null('array<struct{db: str, name: str}>'),
                exon=hl.null('str'),
                gene_id='ENSG00000187634',
                gene_pheno=hl.null('int32'),
                gene_symbol='SAMD11',
                gene_symbol_source='HGNC',
                hgnc_id='28706',
                hgvs_offset=hl.null('int32'),
                hgvsc=hl.null('str'),
                hgvsp=hl.null('str'),
                impact='MODIFIER',
                intron=hl.null('str'),
                lof=hl.null('str'),
                lof_filter=hl.null('str'),
                lof_flags=hl.null('str'),
                lof_info=hl.null('str'),
                minimised=1,
                polyphen_prediction=hl.null('str'),
                polyphen_score=hl.null('float64'),
                protein_end=hl.null('int32'),
                protein_id='ENSP00000349216',
                protein_start=hl.null('int32'),
                sift_prediction=hl.null('str'),
                sift_score=hl.null('float64'),
                strand=1,
                swissprot=hl.null('str'),
                transcript_id='ENST00000341065',
                trembl=hl.null('str'),
                uniparc='UPI000155D47A',
                variant_allele='A',
            ),
            hl.struct(
                allele_num=1,
                amino_acids=hl.null('str'),
                biotype='protein_coding',
                canonical=1,
                ccds='CCDS2.2',
                cdna_end=hl.null('int32'),
                cdna_start=hl.null('int32'),
                cds_end=hl.null('int32'),
                cds_start=hl.null('int32'),
                codons=hl.null('str'),
                consequence_terms=hl.array(['downstream_gene_variant']),
                distance=1963,
                domains=hl.null('array<struct{db: str, name: str}>'),
                exon=hl.null('str'),
                gene_id='ENSG00000187634',
                gene_pheno=hl.null('int32'),
                gene_symbol='SAMD11',
                gene_symbol_source='HGNC',
                hgnc_id='28706',
                hgvs_offset=hl.null('int32'),
                hgvsc=hl.null('str'),
                hgvsp=hl.null('str'),
                impact='MODIFIER',
                intron=hl.null('str'),
                lof=hl.null('str'),
                lof_filter=hl.null('str'),
                lof_flags=hl.null('str'),
                lof_info=hl.null('str'),
                minimised=1,
                polyphen_prediction=hl.null('str'),
                polyphen_score=hl.null('float64'),
                protein_end=hl.null('int32'),
                protein_id='ENSP00000342313',
                protein_start=hl.null('int32'),
                sift_prediction=hl.null('str'),
                sift_score=hl.null('float64'),
                strand=1,
                swissprot='Q96NU1',
                transcript_id='ENST00000342066',
                trembl='Q5SV95,I7FV93,A6PWC8',
                uniparc='UPI0000D61E04',
                variant_allele='A',
            ),
            hl.struct(
                allele_num=1,
                amino_acids=hl.null('str'),
                biotype='protein_coding',
                canonical=hl.null('int32'),
                ccds=hl.null('str'),
                cdna_end=hl.null('int32'),
                cdna_start=hl.null('int32'),
                cds_end=hl.null('int32'),
                cds_start=hl.null('int32'),
                codons=hl.null('str'),
                consequence_terms=hl.array(['downstream_gene_variant']),
                distance=2279,
                domains=hl.null('array<struct{db: str, name: str}>'),
                exon=hl.null('str'),
                gene_id='ENSG00000187634',
                gene_pheno=hl.null('int32'),
                gene_symbol='SAMD11',
                gene_symbol_source='HGNC',
                hgnc_id='28706',
                hgvs_offset=hl.null('int32'),
                hgvsc=hl.null('str'),
                hgvsp=hl.null('str'),
                impact='MODIFIER',
                intron=hl.null('str'),
                lof=hl.null('str'),
                lof_filter=hl.null('str'),
                lof_flags=hl.null('str'),
                lof_info=hl.null('str'),
                minimised=1,
                polyphen_prediction=hl.null('str'),
                polyphen_score=hl.null('float64'),
                protein_end=hl.null('int32'),
                protein_id='ENSP00000412228',
                protein_start=hl.null('int32'),
                sift_prediction=hl.null('str'),
                sift_score=hl.null('float64'),
                strand=1,
                swissprot=hl.null('str'),
                transcript_id='ENST00000455979',
                trembl=hl.null('str'),
                uniparc='UPI000155D479',
                variant_allele='A',
            ),
            hl.struct(
                allele_num=1,
                amino_acids=hl.null('str'),
                biotype='retained_intron',
                canonical=hl.null('int32'),
                ccds=hl.null('str'),
                cdna_end=hl.null('int32'),
                cdna_start=hl.null('int32'),
                cds_end=hl.null('int32'),
                cds_start=hl.null('int32'),
                codons=hl.null('str'),
                consequence_terms=hl.array(['downstream_gene_variant']),
                distance=3646,
                domains=hl.null('array<struct{db: str, name: str}>'),
                exon=hl.null('str'),
                gene_id='ENSG00000187634',
                gene_pheno=hl.null('int32'),
                gene_symbol='SAMD11',
                gene_symbol_source='HGNC',
                hgnc_id='28706',
                hgvs_offset=hl.null('int32'),
                hgvsc=hl.null('str'),
                hgvsp=hl.null('str'),
                impact='MODIFIER',
                intron=hl.null('str'),
                lof=hl.null('str'),
                lof_filter=hl.null('str'),
                lof_flags=hl.null('str'),
                lof_info=hl.null('str'),
                minimised=1,
                polyphen_prediction=hl.null('str'),
                polyphen_score=hl.null('float64'),
                protein_end=hl.null('int32'),
                protein_id=hl.null('str'),
                protein_start=hl.null('int32'),
                sift_prediction=hl.null('str'),
                sift_score=hl.null('float64'),
                strand=1,
                swissprot=hl.null('str'),
                transcript_id='ENST00000464948',
                trembl=hl.null('str'),
                uniparc=hl.null('str'),
                variant_allele='A',
            ),
            hl.struct(
                allele_num=1,
                amino_acids=hl.null('str'),
                biotype='retained_intron',
                canonical=hl.null('int32'),
                ccds=hl.null('str'),
                cdna_end=hl.null('int32'),
                cdna_start=hl.null('int32'),
                cds_end=hl.null('int32'),
                cds_start=hl.null('int32'),
                codons=hl.null('str'),
                consequence_terms=hl.array(['downstream_gene_variant']),
                distance=3736,
                domains=hl.null('array<struct{db: str, name: str}>'),
                exon=hl.null('str'),
                gene_id='ENSG00000187634',
                gene_pheno=hl.null('int32'),
                gene_symbol='SAMD11',
                gene_symbol_source='HGNC',
                hgnc_id='28706',
                hgvs_offset=hl.null('int32'),
                hgvsc=hl.null('str'),
                hgvsp=hl.null('str'),
                impact='MODIFIER',
                intron=hl.null('str'),
                lof=hl.null('str'),
                lof_filter=hl.null('str'),
                lof_flags=hl.null('str'),
                lof_info=hl.null('str'),
                minimised=1,
                polyphen_prediction=hl.null('str'),
                polyphen_score=hl.null('float64'),
                protein_end=hl.null('int32'),
                protein_id=hl.null('str'),
                protein_start=hl.null('int32'),
                sift_prediction=hl.null('str'),
                sift_score=hl.null('float64'),
                strand=1,
                swissprot=hl.null('str'),
                transcript_id='ENST00000466827',
                trembl=hl.null('str'),
                uniparc=hl.null('str'),
                variant_allele='A',
            ),
            hl.struct(
                allele_num=1,
                amino_acids=hl.null('str'),
                biotype='retained_intron',
                canonical=hl.null('int32'),
                ccds=hl.null('str'),
                cdna_end=hl.null('int32'),
                cdna_start=hl.null('int32'),
                cds_end=hl.null('int32'),
                cds_start=hl.null('int32'),
                codons=hl.null('str'),
                consequence_terms=hl.array(['downstream_gene_variant']),
                distance=3544,
                domains=hl.null('array<struct{db: str, name: str}>'),
                exon=hl.null('str'),
                gene_id='ENSG00000187634',
                gene_pheno=hl.null('int32'),
                gene_symbol='SAMD11',
                gene_symbol_source='HGNC',
                hgnc_id='28706',
                hgvs_offset=hl.null('int32'),
                hgvsc=hl.null('str'),
                hgvsp=hl.null('str'),
                impact='MODIFIER',
                intron=hl.null('str'),
                lof=hl.null('str'),
                lof_filter=hl.null('str'),
                lof_flags=hl.null('str'),
                lof_info=hl.null('str'),
                minimised=1,
                polyphen_prediction=hl.null('str'),
                polyphen_score=hl.null('float64'),
                protein_end=hl.null('int32'),
                protein_id=hl.null('str'),
                protein_start=hl.null('int32'),
                sift_prediction=hl.null('str'),
                sift_score=hl.null('float64'),
                strand=1,
                swissprot=hl.null('str'),
                transcript_id='ENST00000474461',
                trembl=hl.null('str'),
                uniparc=hl.null('str'),
                variant_allele='A',
            ),
            hl.struct(
                allele_num=1,
                amino_acids=hl.null('str'),
                biotype='retained_intron',
                canonical=hl.null('int32'),
                ccds=hl.null('str'),
                cdna_end=3114,
                cdna_start=3114,
                cds_end=hl.null('int32'),
                cds_start=hl.null('int32'),
                codons=hl.null('str'),
                consequence_terms=hl.array(
                    [
                        'non_coding_transcript_exon_variant',
                        'non_coding_transcript_variant',
                    ],
                ),
                distance=hl.null('int32'),
                domains=hl.null('array<struct{db: str, name: str}>'),
                exon='13/17',
                gene_id='ENSG00000188976',
                gene_pheno=hl.null('int32'),
                gene_symbol='NOC2L',
                gene_symbol_source='HGNC',
                hgnc_id='24517',
                hgvs_offset=hl.null('int32'),
                hgvsc='ENST00000477976.1:n.3114C>T',
                hgvsp=hl.null('str'),
                impact='MODIFIER',
                intron=hl.null('str'),
                lof=hl.null('str'),
                lof_filter=hl.null('str'),
                lof_flags=hl.null('str'),
                lof_info=hl.null('str'),
                minimised=1,
                polyphen_prediction=hl.null('str'),
                polyphen_score=hl.null('float64'),
                protein_end=hl.null('int32'),
                protein_id=hl.null('str'),
                protein_start=hl.null('int32'),
                sift_prediction=hl.null('str'),
                sift_score=hl.null('float64'),
                strand=-1,
                swissprot=hl.null('str'),
                transcript_id='ENST00000477976',
                trembl=hl.null('str'),
                uniparc=hl.null('str'),
                variant_allele='A',
            ),
            hl.struct(
                allele_num=1,
                amino_acids=hl.null('str'),
                biotype='processed_transcript',
                canonical=hl.null('int32'),
                ccds=hl.null('str'),
                cdna_end=hl.null('int32'),
                cdna_start=hl.null('int32'),
                cds_end=hl.null('int32'),
                cds_start=hl.null('int32'),
                codons=hl.null('str'),
                consequence_terms=hl.array(['downstream_gene_variant']),
                distance=4365,
                domains=hl.null('array<struct{db: str, name: str}>'),
                exon=hl.null('str'),
                gene_id='ENSG00000187634',
                gene_pheno=hl.null('int32'),
                gene_symbol='SAMD11',
                gene_symbol_source='HGNC',
                hgnc_id='28706',
                hgvs_offset=hl.null('int32'),
                hgvsc=hl.null('str'),
                hgvsp=hl.null('str'),
                impact='MODIFIER',
                intron=hl.null('str'),
                lof=hl.null('str'),
                lof_filter=hl.null('str'),
                lof_flags=hl.null('str'),
                lof_info=hl.null('str'),
                minimised=1,
                polyphen_prediction=hl.null('str'),
                polyphen_score=hl.null('float64'),
                protein_end=hl.null('int32'),
                protein_id=hl.null('str'),
                protein_start=hl.null('int32'),
                sift_prediction=hl.null('str'),
                sift_score=hl.null('float64'),
                strand=1,
                swissprot=hl.null('str'),
                transcript_id='ENST00000478729',
                trembl=hl.null('str'),
                uniparc=hl.null('str'),
                variant_allele='A',
            ),
            hl.struct(
                allele_num=1,
                amino_acids=hl.null('str'),
                biotype='retained_intron',
                canonical=hl.null('int32'),
                ccds=hl.null('str'),
                cdna_end=523,
                cdna_start=523,
                cds_end=hl.null('int32'),
                cds_start=hl.null('int32'),
                codons=hl.null('str'),
                consequence_terms=hl.array(
                    [
                        'non_coding_transcript_exon_variant',
                        'non_coding_transcript_variant',
                    ],
                ),
                distance=hl.null('int32'),
                domains=hl.null('array<struct{db: str, name: str}>'),
                exon='1/5',
                gene_id='ENSG00000188976',
                gene_pheno=hl.null('int32'),
                gene_symbol='NOC2L',
                gene_symbol_source='HGNC',
                hgnc_id='24517',
                hgvs_offset=hl.null('int32'),
                hgvsc='ENST00000483767.1:n.523C>T',
                hgvsp=hl.null('str'),
                impact='MODIFIER',
                intron=hl.null('str'),
                lof=hl.null('str'),
                lof_filter=hl.null('str'),
                lof_flags=hl.null('str'),
                lof_info=hl.null('str'),
                minimised=1,
                polyphen_prediction=hl.null('str'),
                polyphen_score=hl.null('float64'),
                protein_end=hl.null('int32'),
                protein_id=hl.null('str'),
                protein_start=hl.null('int32'),
                sift_prediction=hl.null('str'),
                sift_score=hl.null('float64'),
                strand=-1,
                swissprot=hl.null('str'),
                transcript_id='ENST00000483767',
                trembl=hl.null('str'),
                uniparc=hl.null('str'),
                variant_allele='A',
            ),
            hl.struct(
                allele_num=1,
                amino_acids=hl.null('str'),
                biotype='processed_transcript',
                canonical=hl.null('int32'),
                ccds=hl.null('str'),
                cdna_end=hl.null('int32'),
                cdna_start=hl.null('int32'),
                cds_end=hl.null('int32'),
                cds_start=hl.null('int32'),
                codons=hl.null('str'),
                consequence_terms=hl.array(['upstream_gene_variant']),
                distance=976,
                domains=hl.null('array<struct{db: str, name: str}>'),
                exon=hl.null('str'),
                gene_id='ENSG00000188976',
                gene_pheno=hl.null('int32'),
                gene_symbol='NOC2L',
                gene_symbol_source='HGNC',
                hgnc_id='24517',
                hgvs_offset=hl.null('int32'),
                hgvsc=hl.null('str'),
                hgvsp=hl.null('str'),
                impact='MODIFIER',
                intron=hl.null('str'),
                lof=hl.null('str'),
                lof_filter=hl.null('str'),
                lof_flags=hl.null('str'),
                lof_info=hl.null('str'),
                minimised=1,
                polyphen_prediction=hl.null('str'),
                polyphen_score=hl.null('float64'),
                protein_end=hl.null('int32'),
                protein_id=hl.null('str'),
                protein_start=hl.null('int32'),
                sift_prediction=hl.null('str'),
                sift_score=hl.null('float64'),
                strand=-1,
                swissprot=hl.null('str'),
                transcript_id='ENST00000496938',
                trembl=hl.null('str'),
                uniparc=hl.null('str'),
                variant_allele='A',
            ),
        ],
    ),
    variant_class='SNV',
)