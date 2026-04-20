#!/usr/bin/env python3

# Read and input the covid.fasta file
def read_fasta(fasta_file):
    genome_sequence = ""

    with open(fasta_file, "r") as f:
        header = next(f) 

        for line in f:
            line = line.strip()
            genome_sequence += line 

    return genome_sequence

# Read and parse covid.genes.gff3
def read_gff(gff_file, genome_sequence):
    results = []

    with open(gff_file, "r") as f:
        for line in f:

            if line.startswith("#"):
                continue

            columns = line.strip().split("\t")

            start = int(columns[3])
            end = int(columns[4])

            sequence = genome_sequence[start-1:end]

            attributes = columns[8]

            seq_id = ""
            for item in attributes.split(";"):
                if item.startswith("ID="):
                    seq_id = item.split("=")[1]

            results.append((seq_id, sequence))

    return results

# printing each feature: each line from the GFF3 file
def write_output(results):
    with open("covid_genes.fasta", "w") as out:
        for seq_id, sequence in results:
            out.write(">" + seq_id + "\n")
            out.write(sequence + "\n")
