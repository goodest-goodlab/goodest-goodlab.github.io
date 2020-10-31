############################################################
# For Good lab Griz docs, 03.2020
# Generates "jobs.html"
############################################################

import sys, os
sys.path.append('..')
import lib.read_chunks as RC

######################
# HTML template
######################

html_template = """
<!doctype html>
    {head}

<body>
	<div class="pure-u-24-24" id="header">Good lab Griz cluster docs &mdash; Running Jobs</div>

	{nav}

	<div class="pure-u-24-24" id="server_sep_div"></div>
	<div class="pure-g" id="griz_head_row">
		<div class="pure-u-4-24" id="margin"></div>
		<div class="pure-u-4-24" id="griz_img_cont">
			<img class="pure-img" id="griz_img" src="../img/logo/griz.png">
		</div>

		<div class="pure-u-12-24" id="griz_title">
			<h1>Job management with <span id="hidden">SLURM<img src="../img/extra/slurm.png"></span></h1>
		</div>
		<div class="pure-u-4-24" id="margin"></div>
	</div>

	<div class="pure-g" id="griz_main_div">
		<div class="pure-u-24-24" id="server_sep_div"></div>
		<div class="pure-u-2-24" id="margin"></div>
		<div class="pure-u-20-24" id="griz_main_row">

		<div class="pure-g">
			<div class="pure-u-2-24" id="margin"></div>
			<div class="pure-u-20-24" id="server_row">
				<div id="griz_node_desc">
					<p>
						Griz uses the <a href="https://slurm.schedmd.com/" target="_blank">SLURM Workload Manager</a> to distribute resources 
						and schedule jobs. What this means is that in order to run computational or memory intensive jobs, you will have to 
						submit a job script with all the resources you need for that job and all the commands you would like to run. Below I
						will outline an example job script and also show how to connect to a compute node interactively.
					</p>

					<div id="msg_cont">
						<div id="msg">
							<div id="msg_banner">Important!</div>
							<div id="msg_text">
								<p>
									Currently, during this test phase, we have no limits on resources we can request or time to run jobs, but this will likely change
									when the server is out of testing!
								</p>
							</div>
						</div>
					</div>

					<p>
						
					</p>

					<a name="example"></a>
					<div id="section_sep_top"></div>
					<div id="section_line"></div>
					<div id="section_sep_btm"></div>

					<h2>Example job script &mdash; <a href="../etc/job_script.sh" download>Download</a></h2>

					<p>
						I am still learning the SLURM system (old University used TORQUE), so I am open to feedback about best practices!
					</p>

					<p>Below is a basic job script called <code>job_script.sh</code>:</p>

<pre>
	#!/bin/bash
	#SBATCH --job-name=[job name]
	#SBATCH --output="/path/to/desired/directory/%x-%j.out"
	#SBATCH --mail-user=[your email]
	#SBATCH --mail-type=ALL
	#SBATCH --partition=good_lab_cpu
	#SBATCH --nodes=1
	#SBATCH --ntasks=1
	#SBATCH --cpus-per-task=4
	#SBATCH --mem=96000
	#SBATCH --time=2:30:00 # How long should they run
	## Above is all information for SLURM. It should all appear at the top of
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
</pre>

					<p>Full documentation of the <code>sbatch</code> options can be found at the following link:</p>

					<div id="imp_link_cont">
						<a id="imp_link" href="https://slurm.schedmd.com/sbatch.html" target="_blank">SLURM sbatch Docs</a>
					</div>

					<p>Briefly, the options above are:</p>

<pre>
	--job-name:	A name to give your job that will appear in the queue.
	--output:	Location for SLURM to write log files. Default is same location as job script. %x represents job name and %j represents job ID.
	--mail-user:	An email address to receive updates from SLURM about job progress.
	--mail-type:	What type of email updates you'd like to receive (NONE, BEGIN, END, FAIL, ALL).
	--partition:	The type of node you want to run your job on. See <a href="nodes.html">Node info</a>.
	--nodes:	Number of nodes you will need for the job.
	--ntasks:	Number of tasks you need for your job. Each command is a task. If you run commands with parallel or srun, set this to be the number of commands you want to run simultaneously.
	--cpus-per-task:Number of threads available for each command. If you run a program that is multithreaded, set this to be the number of threads specified by that program.
	--mem:		The amount of memory you need for you job. Default unit is MB.
	--time: 	The amount of time needed for your job to run. <b>Ignore for now!</b>
</pre>


					<a name="submit"></a>
					<div id="section_sep_top"></div>
					<div id="section_line"></div>
					<div id="section_sep_btm"></div>

					<h2>Submitting your job script</h2>

					<p>Job scripts are submitted with the <code>sbatch</code> command:</p>

					<code>sbatch job_script.sh</code>

					<p>
						SLURM will read the options in the header of the file and assign resources accordingly before executing the desired commands.
						Jobs will be assigned an ID and a log file will be written in the same location as the job script called <code>[job id].out</code>.
						Check this file if you encounter errors during your run.
					</p>


					<a name="monitor"></a>
					<div id="section_sep_top"></div>
					<div id="section_line"></div>
					<div id="section_sep_btm"></div>

					<h2>Monitoring jobs</h2>
					
					<p>The status of running jobs can be checked by running <code>squeue</code>.</p>

					<p>A job can be cancelled by running <code>scancel [job id]</code></p>

					<p>
						I have also provided a script called <code>sres</code> that checks node resource availability in the <a href="https://github.com/goodest-goodlab/good-utils> target="_blank">good-utils</a>
						repository. Simply clone the repository and add it to your $PATH to run:
					</p>

					<p>By default <code>sres</code> prints information for all Good Lab partitions. You can provide it with the name of a particular partition to print out info only for that one</p>

					<p>For example:</p>

					<code>sres good_lab_cpu</code>

					<p>should produce the following output:</p>

<pre>NODE NAME     PARTITION(S)                    TOTAL CPUs    ALLOCATED CPUs    FREE CPUs    TOTAL MEM (MB)    ALLOCATED MEM (MB)    FREE MEM (MB)    STATE
compute-0-1   good_lab_cpu,good_lab_large_cpu 72            0                 72           772439            0                     765683           IDLE
compute-0-2   good_lab_cpu,good_lab_large_cpu 72            0                 72           772439            0                     755300           IDLE
compute-0-3   good_lab_cpu,good_lab_large_cpu 72            0                 72           772439            0                     692035           IDLE
compute-0-4   good_lab_cpu,good_lab_large_cpu 72            0                 72           772439            0                     722757           IDLE
compute-0-5   good_lab_cpu,good_lab_large_cpu 72            0                 72           772439            0                     765922           IDLE
compute-0-6   good_lab_cpu,good_lab_large_cpu 72            0                 72           772439            0                     752593           IDLE
compute-0-7   good_lab_cpu,good_lab_large_cpu 72            0                 72           772439            0                     753552           IDLE
compute-0-8   good_lab_cpu,good_lab_large_cpu 72            69                3            772439            0                     23577            MIXED
</pre

					<a name="interact"></a>
					<div id="section_sep_top"></div>
					<div id="section_line"></div>
					<div id="section_sep_btm"></div>

					<h2>Running commands on a compute node interactively</h2>

					<p>
						In some instances, it may be preferable to allocate resources on a compute node and run commands manually rather than through a job
						script. This can be especially useful for debugging and testing workflows, and can be effectively combined with 
						<a href="https://kb.iu.edu/d/acuy" target="_blank"><code>screen</code></a>.
					</p>

					<p>To run commands interactively, use <code>salloc</code>:</p>

					<code>salloc -p good_lab_cpu -N1 --exclusive srun --pty bash</code>

					<p>
						This will allocate one good_lab_cpu node for interactive commands. Many more options are available for <code>salloc</code>. 
						See the following docs for more info
					</p>

					<p>
						<div id="imp_link_cont">
							<a id="imp_link" href="https://slurm.schedmd.com/salloc.html" target="_blank">SLURM salloc Docs</a>
						</div>
					</p>

					<div id="msg_cont">
						<div id="msg">
							<div id="msg_banner">Important!</div>
							<div id="msg_text">
								<p>
									Be aware that if you request resources with <code>salloc</code> that are unavailable, you may be waiting in queue 
									even for an interactive session
								</p>
							</div>
						</div>
					</div>

					<p></p>

					<!-- <div id="msg_cont">
						<div id="msg">
							<div id="rec_banner">Recommendation</div>
							<div id="rec_text">
								<p>
									Include this function in your <code>.bash_profile</code> to quickly start a basic interactive compute node:
								</p>

<pre>
	{func}
</pre>
								<p>
									Using this, you can run the command <code>interact</code> to start a session on a good_lab_cpu by default.
									Run <code>interact [node type]</code> to specify a different node type (i.e. <code>interact good_lab_reincarnation</code>).
								</p>

							</div>
						</div>
					</div> -->

					<div id="msg_cont">
						<div id="msg">
							<div id="rec_banner">Recommendation</div>
							<div id="rec_text">
								<p>
									Download the <a href="https://github.com/goodest-goodlab/good-utils> target="_blank">good-utils</a> repository, which includes 
									the <code>interact</code> command to request interactive node allocations. Use <code>interact -h</code> to see its usage.
								</p>
							</div>
						</div>
					</div>


				</div>
			</div>
		</div>
	</div>

	<div class="pure-u-24-24" id="sep_div"></div>


    {footer}
</body>
"""

######################
# Main block
######################
pagefile = "jobs.html";
print("Generating " + pagefile + "...");
title = "Griz - Running Jobs"

head = RC.readHead(title, pagefile, "griz");
nav = RC.readNav(pagefile, "griz");
footer = RC.readFooter();

outfilename = "../../griz/" + pagefile;

func = "function interact () {\n\t\tn=${1:-\"good_lab_cpu\"}\n\t\techo \"Starting a $n node\"\n\t\tsalloc -p $n -N1 --exclusive srun --pty bash\n\t}\n\texport interact\n\t# Start an interactive node"

with open(outfilename, "w") as outfile:
    outfile.write(html_template.format(head=head, nav=nav, func=func, footer=footer));