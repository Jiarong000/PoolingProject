import os
import numpy as np
from cyvcf2 import VCF, Writer


for variant in VCF('/Users/emilielaurent/Documents/UniHT2019_period2/AppliedBioinformatics/code/ALL.chr20.snps.gt.chunk1000.vcf.gz'):  # or VCF('some.bcf')
    # x = variant.INFO.get('AF') #variant.ALT # e.g. REF='A', ALT=['C', 'T']
    genotype = variant.genotypes
    allel_freq = variant.INFO.get('AF')

    print(genotype)

# np.ndarray
#     variant.CHROM, variant.start, variant.end, variant.ID, \
#                 variant.FILTER, variant.QUAL
#
#     # numpy arrays of specific things we pull from the sample fields.
#     # gt_types is array of 0,1,2,3==HOM_REF, HET, UNKNOWN, HOM_ALT
#     variant.gt_types, variant.gt_ref_depths, variant.gt_alt_depths # numpy arrays
#     variant.gt_phases, variant.gt_quals, variant.gt_bases # numpy array
#
#
#     ## INFO Field.
#     ## extract from the info field by it's name:
#     variant.INFO.get('DP') # int
#     variant.INFO.get('FS') # float
#     variant.INFO.get('AC') # float
#
#     # convert back to a string.
#     str(variant)
#
#
#     # ## per-sample info...
#     # # Get a numpy array of the depth per sample:
#     # dp = variant.format('DP')
#     # # or of any other format field:
#     # sb = variant.format('SB')
#     # assert sb.shape == (n_samples, 4) # 4-values per

# to do a region-query:
#
# vcf = VCF('some.vcf.gz')
# for v in vcf('11:435345-556565'):
#     if v.INFO["AF"] > 0.1: continue
#     print(str(v))
#
#     # single sample of 0|1 in vcf becomes [[0, 1, True]]
#     # 2 samples of 0/0 and 1|1 would be [[0, 0, False], [1, 1, True]]
#     print v.genotypes
