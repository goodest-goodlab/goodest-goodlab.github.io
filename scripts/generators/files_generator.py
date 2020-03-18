############################################################
# For Good lab Griz docs, 03.2020
# Generates "files.html"
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
	<div class="pure-u-24-24" id="header">Good lab Griz cluster docs &mdash; File info</div>

	{nav}

	<div class="pure-u-24-24" id="server_sep_div"></div>
	<div class="pure-g" id="griz_head_row">
		<div class="pure-u-4-24" id="margin"></div>
		<div class="pure-u-4-24" id="griz_img_cont">
			<img class="pure-img" id="griz_img" src="../img/logo/griz.png">
		</div>

		<div class="pure-u-12-24" id="griz_title">
			<h1>Transferring and Storing files</h1>
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
				
					<a name="store"></a>
					<div id="section_sep_top"></div>
					<div id="section_sep_btm"></div>
					<h2>Storing files on Griz</h2>

					<p>Currently, the main storage space on the Griz cluster is the 
						<a href="https://www.beegfs.io/content/" target="_blank"><code>beegfs</code></a> file system. This system has 800TB of 
						storage and will likely turn into scratch space in the future. In the meantime, we have a pretty free reign here, so go 
						ahead and make a folder there and store stuff.
					</p>

					<div id="msg_cont">
						<div id="msg">
							<div id="msg_banner">Important!</div>
							<div id="msg_text">
								<p>Make sure this isn't the only place you are storing your data! Best practice is to have at least 2 backups.</p>
							</div>
						</div>
					</div>

					<p>Navigate to /mnt/beegfs/:</p>

					<code>cd /mnt/beegfs/</code>

					<p>Create a directory the same as your username (NetID):</p>

					<code>mkdir gt156213e</code>

					<p>And enjoy the space!</p>


					<a name="transfer"></a>	
					<div id="section_sep_top"></div>
					<div id="section_line"></div>
					<div id="section_sep_btm"></div>

					<h2>Transferring files to Griz</h2>

					<p>
						Typical command line tools like <code>rsync</code> and <code>sftp</code> may be your best option for transferring files to 
						and from Griz. For example, a typical rsync command looks like this:
					</p>

					<code>rsync -azvh [username]@[server address]:[location on remote server] [desired destination on local server]</code>

					<p>
						As an explicit example, lets say I wanted to transfer a file called "data" in my home directory on Musculus to my 
						home directory on Griz:
					</p>

					<code>rsync -azvh gregg_thomas@musculus.dbs.umt.edu:/home/gregg_thomas/data/ /home/gt156213e/.</code>

					<p>
						The <code>.</code> at the end indicates I want the same file/directory name in th destination. 
						Alternateively, if I just want to transfer to my current working directory, I can just put a <code>.</code> as the destination:
					</p>

					<code>rsync -azvh gregg_thomas@musculus.dbs.umt.edu:/home/gregg_thomas/data/ .</code>

					<p>When transferring files from Carnation, the port for the Good Lab docker container needs to be specified as follows:</p>

					<code>rsync -avzh -e 'ssh -p 2225' gregg_thomas@carnation.dbs.umt.edu:/home/gregg_thomas/data/ .</code>

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
pagefile = "files.html";
print("Generating " + pagefile + "...");
title = "Griz - File Info"

head = RC.readHead(title, pagefile, "griz");
nav = RC.readNav(pagefile, "griz");
footer = RC.readFooter();

outfilename = "../../griz/" + pagefile;

with open(outfilename, "w") as outfile:
    outfile.write(html_template.format(head=head, nav=nav, footer=footer));