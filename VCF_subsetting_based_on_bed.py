import csv
import sys
import os
def subset_vcf(invcf,inbed):
    """

    :param invcf: Give VCF file path
    :param inbed: Give BED file path(column 1 : chr<No.>,column2 : start position,column3 : end position)
    :return: Subset of VCF file based on genomic coordinates present in provided BED file
    """
    bed_tuples = []
    header=[]
    filtered_entries =[]
    outvcf = open("vcf_subset.vcf", 'w')
    """
    Reading user defined BED file 
    """
    with open(inbed) as my_bed:
        for bline in my_bed:
            bline = bline.strip().split("\t")
            bed_tuples.append(tuple(bline[:2]))
    """
    Reading user defined vcf file and storing header into seperate variable
    """
    with open(invcf, 'r') as my_vcf:
        for vline in my_vcf:
            if vline.startswith('#'):
                header.append(vline.strip("\n"))
                continue
            vline = vline.strip().split("\t")
            """
            Subsetting vcf file based on bed file
            """
            if tuple(vline[0:2]) in bed_tuples:
                filtered_entries.append(vline)
    """
    Writing subset vcf into new file named 'vcf_subset.vcf'
    """
    outvcf.write("\n".join(header))
    outvcf.write("\n")
    for entries in filtered_entries:
        outvcf.write("\t".join(entries))
        outvcf.write("\n")
"""
Calling a function
"""
subset_vcf(sys.argv[1],sys.argv[2])


