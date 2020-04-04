############################################################
# This script reads all alignment files in an input directory
# and generates a basic RAxML commands for each.
############################################################

import sys, os, datetime, random

############################################################

print("#!/bin/bash")
# I like to print the bash shebang line so the output can be read as a
# bash script to run commands one at a time if necessary

print("# Example command generator")
# A descriptive message about what these commands are

indir = "/projects/project/aligns/"
outdir = "/projects/project/gene-trees/"
# Specify both the location of the input files and the desired
# location for the output files.

print("# PYTHON VERSION: " + ".".join(map(str, sys.version_info[:3])))
print("# Script call: " + " ".join(sys.argv))
print("# Runtime: " + datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S"))
print("# Input directory: " + indir)
print("# Output directory: " + outdir)
print("# ----------");
# Always good to include some runtime info for records

aa_model = "PROTGAMMAJTTF"
# The RAxML sequence evolution model for all runs.

for f in os.listdir(indir):
    if not f.endswith("-aln.fa"):
        continue;

    input_file = os.path.join(indir, f)
    # Input file.

    aln_name = os.path.splitext(f)[0]
    # Get the filename without the extension as the alignment name.

    output_directory = os.path.join(outdir, aln_name)
    # Output directory.

    if not os.path.isdir(output_directory):
        os.system("mkdir " + output_directory)
    # If the output directory doesn't exist, create it.

    seed = str(random.randint(1000000,999999999))
    # Generate the starting seed for RAxML.

    ####
    raxml_cmd = "raxml -f a" 
    # The RAxML command and the analysis to run.

    raxml_cmd += " -m " + aa_model
    # The sequence evolution model.

    raxml_cmd += " -p " + seed
    # The current starting seed.

    raxml_cmd += " -s " + input_file
    # The current input sequence file.

    raxml_cmd += " -n " + aln_name
    # The name of the job for RAxML.

    raxml_cmd += " -w " + output_directory
    # The location to which RAxML will write output files.
    # These lines build up the RAxML command. Include whatever options you need.
    # This can all be done on one line, but I broke it up for clarity.
    ####

    print(raxml_cmd)