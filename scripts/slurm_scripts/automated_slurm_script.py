#!/usr/bin/env python3

print("#!/bin/bash")
import argparse

##----------------------accept and parse command line arguments
# create an argument parser object
parser = argparse.ArgumentParser(description="This script makes slurm script modifiable and allows for\
                                user to add arguments")

#add a positional argument, in this case, the the computer you want to run your slurm script on
parser.add_argument("partition", help="Choose computer")
parser.add_argument("nodes", help="Choose # of nodes to use to compute your script")
parser.add_argument("cpus", help="Choose cpus to dedicate to your script")
parser.add_argument("time", help="Choose amount of time your script will take")

args = parser.parse_args()

print("SBATCH --job-name=lb244.test")
print(f"SBATCH --partition= {args.partition}")
print(f"SBATCH --nodes= {args.nodes}")
print("SBATCH --qos cloud")
print(f"SBATCH --cpus-per-task= {args.cpus}")
print(f"SBATCH --time= {args.time}")
print("SBATCH --output=%x.%j.out")
print("SBATCH --error=%x.%j.err")
print("SBATCH --mail-type=ALL")
print("BATCH --mail-user=lb244@uark.edu")

print("export OMP_NUM_THREADS=32")

print("module purge")
print("module load blast")

print("cd $SLURM_SUBMIT_DIR")

# blast watermelon.fsa against itself
print("blastn -query watermelon.fsa -subject watermelon.fsa > wat.vs.wat.blastn")

