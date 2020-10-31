############################################################
# For Good lab Griz docs, 03.2020
# Generates "start.html"
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
	<div class="pure-u-24-24" id="header">Good lab Griz cluster docs &mdash; Getting Started</div>

	{nav}

	<div class="pure-u-24-24" id="server_sep_div"></div>
	<div class="pure-g" id="griz_head_row">
		<div class="pure-u-4-24" id="margin"></div>
		<div class="pure-u-4-24" id="griz_img_cont">
			<img class="pure-img" id="griz_img" src="../img/logo/griz.png">
		</div>

		<div class="pure-u-12-24" id="griz_title">
			<h1>Logging in to Griz</h1>
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

					<a name="login"></a>	
					<p>
						Griz has a login node to interact with the cluster, either by ssh or FTP:
					</p>
<pre>
	Login node:	login.gscc.umt.edu
</pre>

					<p>
						This node can be used to navigate the file system and submit jobs. Do not submit jobs to this node.
					</p>

					<p>
						While the login node is available both on and off-campus, other resources may require you to be on-campus. For off-campus access, be sure
						to read up on UM's VPN resource:
					</p>

					<div id="imp_link_cont">
						<a id="imp_link" href="https://www.umt.edu/it/support/vpn/default.php" target="_blank">UM VPN Docs</a>
					</div>


					<a name="ssh-login"></a>
					<div id="section_sep_top"></div>
					<div id="section_line"></div>
					<div id="section_sep_btm"></div>

					<h2>SSH logins</h2>

					<p>
						To log in to Griz with a command line interface to navigate the file system and submit jobs, you will need an SSH client.
						On MacOS, Linux, and newer Windows installs an SSH client is pre-installed. Simply open your terminal and type:
					</p>

					<code>ssh [NetID as username]@[server name]</code>

					<p>Accept any fingerprint prompts and enter your password when prompted and you should be good to go!</p>

					<p>Explicitly, if I wanted to log in to the head node, I would type:</p>

					<code>ssh gt156213e@login.gscc.umt.edu</code>

					<p></p>

					<div id="msg_cont">
						<div id="msg">
							<div id="rec_banner">Recommendation</div>
							<div id="rec_text">
								<p>
									Though newer versions of Windows 10 have an SSH client pre-installed, I still prefer the PuTTY SSH client:
								</p>
								<div id="imp_link_cont">
									<a id="imp_link" href="https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html" target="_blank">PuTTY Download</a>
								</div>
								<p></p>

							</div>
						</div>
					</div>


					<a name="ftp-login"></a>
					<div id="section_sep_top"></div>
					<div id="section_line"></div>
					<div id="section_sep_btm"></div>
						
					<h2>FTP logins</h2>

					<p>
						For drag-and-drop file transfers, an FTP client may be preferred. I recommend 
						<a href="https://filezilla-project.org/" target="_blank">FileZilla</a> for MacOS and Linux and
						<a href="https://winscp.net/eng/index.php" target="_blank">WinSCP</a> for Windows.
					</p>

					<p>
						Usage is similar regardless of FTP client chosen. Simply find in the GUI where you can enter the username and 
						server address for the server you want to login to and connect. Enter your password when prompted. Then you should
						be able to drag and drop files between your local computer and the remote server via the FTP GUI.
					</p>

					<div id="msg_cont">
						<div id="msg">
							<div id="rec_banner">Recommendation</div>
							<div id="rec_text">
								<p>
									For both SSH and FTP logins, consider setting up public-key authentication to login. 
									This can provide enhanced security and ease of access compared to logging in with a password.
									See the following for in depth instructions:
								</p>
								<div id="imp_link_cont">
									<a id="imp_link" href="https://kb.iu.edu/d/aews" target="_blank">Set up SSH public-key authentication</a>
								</div>
								<p></p>
							</div>
						</div>
					</div>


					<a name="vnc-login"></a>
					<div id="section_sep_top"></div>
					<div id="section_line"></div>
					<div id="section_sep_btm"></div>

					<h2>Remote Desktop logins</h2>

					<p>
						Remote desktop logins can also be setup. Please contact one of the administrators to get it set up. I recommend the remote desktop software called
						X2Go:
					</p>
					
					<div id="imp_link_cont">
						<a id="imp_link" href="https://wiki.x2go.org/doku.php/download:start" target="_blank">X2Go Download</a>
					</div>

					<p>
						Using X2Go, you will be able to login to one of the nodes and be able to interact with the filesystem with 
						your mouse and keyboard as if you were sitting at the remote node with a monitor. You can even interact 
						with the <a href="jobs.html">SLURM job management software</a> from the remote desktop and open a terminal
						from within the remote desktop.
					</p>

					<p>
						This remote desktop software will prove useful in many situations. However, while some of you may be more 
						comfortable interacting with the cluster in this fashion, I highly recommend logging
						in through a command line interface with SSH!
					</p>

					<a name="screen"></a>
					<div id="section_sep_top"></div>
					<div id="section_line"></div>
					<div id="section_sep_btm"></div>

					<h2>Using <code>screen</code> to manage multiple command line interfaces</h2>

					<p>
						Programs like <code>screen</code> and <code>tmux</code> are bash programs that allow you to start new command line interface sessions while already
						logged in, essentially like opening a new tab in a browser. I have more experience with <code>screen</code> so that is what I will discuss here.
						The advantages of this are enormous. First, you can have multiple screens, allowing you to switch between different bash sessions without logging 
						in to the server with multiple terminals. Most importantly, jobs that you start within a screen <b>keep runnning even after you have logged out!</b>
						Screens are also accessible wherever you log in. So, you could start a job in a screen session from lab, log out, then go home and login from there, 
						start the screen session, and see the progress of the job. Screen has been one of the most helpful tools for me to manage multiple jobs from many
						locations.
					</p>

					<p>Below I will go through some basics, but here are some extensive <code>screen</code> docs:</p>

					<div id="imp_link_cont">
						<a id="imp_link" href="https://linux.die.net/man/1/screen" target="_blank">screen Docs</a>
					</div>


					<a name="screen-start"></a>	
					<div id="section_sep_top"></div>
					<h4>Starting a screen</h4>

					<p>To start a screen, simply type:</p>

					<code>screen</code>

					<p>
						You are now <b>attached</b> to a screen. This will clear your terminal window and open a new session within the same window you are using. Don't worry, your original login session is still
						there, just "minimized," for lack of a better term.
					</p>

					<p>Note that some <code>screen</code> instances may bring up a welcome message rather than taking you directly to a blank command prompt. Simply hit enter to dismiss this message.</p>

					<a name="screen-detach"></a>
					<div id="section_sep_top"></div>	
					<h4>Detach from a screen</h4>

					<p>To <b>detach</b> (or minimize) from the current screen session and return to your original login session, enter the following key combination:</p>

					<code>ctrl+a+d</code>

					<p>Your screen and any jobs running in it are still there! They have just been <b>detached</b>.</p>

					<p>Many <code>screen</code> commands start with the keystroke <code>ctrl+a</code>.</p>

					<a name="screen-attach"></a>
					<div id="section_sep_top"></div>	
					<h4>Attaching to a screen session</h4>

					<p>To <b>attach</b> to or <b>resume</b> a screen session from which you have previously deattached, type</p>

					<code>screen -r</code>

					<a name="screen-manage"></a>
					<div id="section_sep_top"></div>	
					<h4>Managing multiple screen sessions</h4>

					<p>
						There may be cases where you want to run multiple commands in the background on different screens. In this case, you can have multiple screen sessions open.
						While in your login session (i.e. while <b>not attached</b> to any screens), you can run the <code>screen</code> command as many times as you want to start
						separate screen sessions. This is like opening many tabs in your browser.
					</p>
					
					<div id="msg_cont">
						<div id="msg">
							<div id="msg_banner">Important!</div>
							<div id="msg_text">
								<p>
									Try not to start a new screen session while <b>attached</b> to a previous screen session! This can get confusing very quickly.
								</p>
							</div>
						</div>
					</div>

					<p>To view the status of your current screen sessions, type:</p>

					<code>screen -ls</code>

					<p>This should produce something like the following:</p>

<pre>
	gregg_thomas@ecae4883a231:~$ screen -ls
	There are screens on:
			3793335.pts-9.ecae4883a231      (03/18/20 17:36:45)     (Detached)
			2016601.mq      (02/05/20 18:37:44)     (Detached)
			3968059.fastq   (01/25/20 20:16:16)     (Detached)
	3 Sockets in /var/run/screen/S-gregg_thomas.
</pre>

					<p>
						Note that every screen has an ID number and a name in the format <code>[id number.name]</code>. By default, the names given to screens are not human readable.
						To change the <b>name</b> of a screen session, you can run the following:
					</p>

					<code>screen -S [id number] -X sessionname [desired name]</code>

					<p>For instance, if I want to rename the first screen listed above to something more meaningful, I could run:</p>

					<code>screen -S 3793335 -X sessionname test</code>

					<p>Which results in the following when running <code>screen -ls</code>:

<pre>
	gregg_thomas@ecae4883a231:~$ screen -ls
	There are screens on:
			3793335.test    (03/18/20 17:36:46)     (Detached)
			2016601.mq      (02/05/20 18:37:45)     (Detached)
			3968059.fastq   (01/25/20 20:16:17)     (Detached)
	3 Sockets in /var/run/screen/S-gregg_thomas.
</pre>

					<p>Much better!</p>

					<p>With multiple screens running and you want to <b>attach</b> to one of them, you can specify the name of that screen when resuming:</p>

					<code>screen -r test</code>

					<p>
						When you are <b>attached</b> to a screen and wish to switch to another one, simply exit the current screen with <code>ctrl+a+d</code> and then <b>attach</b> to the 
						desired screen.
					</p>

					<div id="msg_cont">
						<div id="msg">
							<div id="msg_banner">Important!</div>
							<div id="msg_text">
								<p>
									If you log out or your connection is interrupted while still <b>attached</b> to a screen, you may be unable to resume it when you log back
									in. In this case, to resume this screen, add the <b>detach</b> flag to the resume command:
								</p>
								<center><code>screen -r -d [screen name]</code></center>
								<p></p>
							</div>
						</div>
					</div>


					<a name="parallel"></a>	
					<div id="section_sep_top"></div>
					<div id="section_line"></div>
					<div id="section_sep_btm"></div>

					<h2>Using <code>parallel</code> to speed up your workflows</h2>

					<p>
						Many times in bioinformatic workflows, we may find ourselves running the same program on tens to thousands of samples (i.e. building gene trees, 
						mapping reads from many individuals, etc.). Even worse, sometimes the programs we are running can be very slow and are not multi-threaded. In this
						case, it is up to us to speed up the workflow.
					</p>

					<p><a href="https://www.gnu.org/software/parallel/" target="_blank">GNU parallel</a> can be a big help in these situations.</p>

					<p><code>parallel</code> is an extremely versatile program, but I will go over the easiest way to run multiple commands in parallel.</p>

					<a name="parallel-gen"></a>
					<div id="section_sep_top"></div>
					<h4>01. Writing a python script to generate commands</h4>

					<p>
						Lets say I have thousands of alignment files from which I want to make gene trees. I have all of my alignments in the same directory, and want
						to run <a href="https://cme.h-its.org/exelixis/web/software/raxml/index.html" target="_blank">RAxML</a> on all of them. I would first write a simple
						python script that generates and prints the RAxML command for each alignment file. Here is an example of a basic command generator script for this 
						purpose:
					</p>

					<div id="imp_link_cont">
						<a id="imp_link" href="../etc/example_cmd_generator.py" target="_blank">Download Example Script</a>
					</div>


<pre>
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
</pre>

					<p>Run this script and redirect the output to a file to generate a shell script that can execute all of these commands:</p>

					<code>python example_cmd_generator.py > raxml_cmds.sh</code>

					<p>Now you have a shell script to run these commands and, importantly, you can use <code>parallel</code> to run them in parallel!</p>

					<p>
						Note that you can use this sort of script for any type of command you have to run multiple times, not just RAxML. Say I had many samples that
						I needed to map with BWA, I could simply replace the steps constructing the RAxML command with those appropriate for BWA.
					</p>
						

					<a name="parallel-run"></a>
					<div id="section_sep_top"></div>
					<h4>02. Executing commands in a file in parallel with <code>parallel</code></h4>

					<p>
						With a file containing many commands, one per line, like the one we generated above, we can execute those commands
						in parallel very easily with:
					</p>

					<code>parallel -j 20 < raxml_cmds.sh</code>

					<p>
						Easy! <code>-j 20</code> indicates we want to use 20 threads to run 20 commands at a time. Change this to whatever number
						you want/however many threads are available. <code>< [filename]</code> means we are feeding the lines from that file 
						into the given command
					</p>

					<div id="msg_cont">
						<div id="msg">
							<div id="msg_banner">Important!</div>
							<div id="msg_text">
								<p>
									Currently the Griz head and login nodes do not have server-wide installs of GNU parallel, but the
									compute nodes do, so you will be able to run jobs that call <code>parallel</code>. To debug these
									workflows, you could <a href="https://www.gnu.org/software/parallel/" target="_blank">download</a>
									and install GNU parallel in your home directory, <a href=https://anaconda.org/conda-forge/parallel">install GNU Parallel from conda</a> 
									(recommended), or login to a compute node interactively (see:
									<a href="jobs.html">Running Jobs</a>.)
								</p>
							</div>
						</div>
					</div>

					<div class="pure-u-24-24" id="sep_div"></div>

					<div id="msg_cont">
						<div id="msg">
							<div id="msg_banner">Important!</div>
							<div id="msg_text">
								<p>
									When submitting jobs to a Griz node that use <code>parallel</code>, the number of <b>tasks</b> should
									match the number of parallel jobs (<code>-j</code>), not the number of cpus.
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
pagefile = "start.html";
print("Generating " + pagefile + "...");
title = "Griz - Getting Started"

head = RC.readHead(title, pagefile, "griz");
nav = RC.readNav(pagefile, "griz");
footer = RC.readFooter();

outfilename = "../../griz/" + pagefile;

with open(outfilename, "w") as outfile:
    outfile.write(html_template.format(head=head, nav=nav, footer=footer));