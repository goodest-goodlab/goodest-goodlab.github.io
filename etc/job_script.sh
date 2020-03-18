#!/bin/bash
#SBATCH --job-name=[job name]
#SBATCH --output="/path/to/desired/directory/%x-%j.out"
#SBATCH --mail-user=[your email]
#SBATCH --mail-type=ALL
#SBATCH --partition=good_lab_cpu
#SBATCH --nodes=1
#SBATCH --ntasks=4
#SBATCH --mem=96000
#SBATCH --time=2:30:00 # How long should they run
## This is all information for SLURM. It should all appear at the top of
## the script before your commands to run. SLURM understands lines 
## beginning with ## as a comment.

## Command(s) to run:

source ~/bin/anaconda3/bin/activate
conda activate biotools
# Make sure the environment with the software you need is activated.

cd /mnt/beegfs/gt156213e/
wgsim -N1000 -S1 genomes/NC_008253_1K.fna simulated_reads/sim_reads.fq /dev/null
bowtie2 -x indexes/e_coli -U simulated_reads/sim_reads.fq -S alignments/sim_reads_aligned.sam
samtools view -b -S -o alignments/sim_reads_aligned.bam alignments/sim_reads_aligned.sam
samtools view -c -f 4 alignments/sim_reads_aligned.bam
samtools view -q 42 -c alignments/sim_reads_aligned.bam



# ------------------------------------
# Explanations of SLURM options above:
# --job-name:	A name to give your job that will appear in the queue.
# --output:	    Location for SLURM to write log files. Default is same location as job script. %x represents job name and %j represents job ID.
# --mail-user:	An email address to receive updates from SLURM about job progress.
# --mail-type:	What type of email updates you'd like to receive (NONE, BEGIN, END, FAIL, ALL).
# --partition:	The type of node you want to run your job on. See <a href="nodes.html">Node info</a>.
# --nodes:	    Minimum number of nodes you will need for the job.
# --ntasks:	    Number of threads(?) you need for your job.
# --mem:		The amount of memory you need for you job. Default unit is MB.
# --time: 	    The amount of time needed for your job to run. <b>Ignore for now!</b>