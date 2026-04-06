#!/usr/bin/env python3

print("#!/bin/bash")
print("SBATCH --job-name=loperez.test")
print("SBATCH --partition comp72")
print("SBATCH --nodes=1")
print("SBATCH --qos cloud")
print("SBATCH --cpus-per-task=32")
print("SBATCH --time=00:05:00")
print("SBATCH --output=%x.%j.out")
print("SBATCH --error=%x.%j.err")
print("SBATCH --mail-type=ALL")
print("BATCH --mail-user=loperez@uark.edu")

print("export OMP_NUM_THREADS=32")

print("module purge")
print("module load blast")

print("cd $SLURM_SUBMIT_DIR")

# blast watermelon.fsa against itself
print("blastn -query watermelon.fsa -subject watermelon.fsa > wat.vs.wat.blastn")
