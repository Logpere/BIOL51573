#!/usr/bin/env python3

import argparse
import gff_functions

def get_args():
    parser = argparse.ArgumentParser(description="Parse FASTA and GFF")

    parser.add_argument("fasta_file")
    parser.add_argument("gff_file")

    return parser.parse_args()

def main():
    args = get_args()

    genome_sequence = gff_functions.read_fasta(args.fasta_file)

    results = gff_functions.read_gff(args.gff_file, genome_sequence)

    gff_functions.write_output(results)

if __name__ == "__main__":
    main()