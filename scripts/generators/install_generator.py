############################################################
# For Good lab Griz docs, 03.2020
# Generates "install.html"
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
	<div class="pure-u-24-24" id="header">Good lab Griz cluster docs &mdash; Software</div>

	{nav}

	<div class="pure-u-24-24" id="server_sep_div"></div>
	<div class="pure-g" id="griz_head_row">
		<div class="pure-u-4-24" id="margin"></div>
		<div class="pure-u-4-24" id="griz_img_cont">
			<img class="pure-img" id="griz_img" src="../img/logo/griz.png">
		</div>

		<div class="pure-u-12-24" id="griz_title">
			<h1>Installing software</h1>
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
						I think this is still being figured out. Likely, the recommended method will be to have a local 
						<a href="https://www.anaconda.com/" target="_blank">Anaconda</a> installation, from which you can install 
						multiple versions of bioinformatic software from <a href="https://anaconda.org/bioconda" target="_blank">bioconda</a>.
					</p>


					<a name="anaconda"></a>
					<div id="section_sep_top"></div>
					<div id="section_line"></div>
					<div id="section_sep_btm"></div>

					<h2>Installing Anaconda</h2>

					<p>
						To install <a href="https://www.anaconda.com/" target="_blank">Anaconda</a>, 
						download the latest version of the installer at the following link. 
					</p>

					<div id="msg_cont">
						<div id="msg">
							<div id="msg_banner">Important!</div>
							<div id="msg_text">
								<p>
									When downloading Anaconda to install on Griz, make sure you select "Linux" at the top. The website tries to 
									guess what you want to install based on your current OS, which may be different that the desired OS on the cluster.
								</p>
							</div>
						</div>
					</div>

					<p>
						<div id="imp_link_cont">
							<a id="imp_link" href="https://www.anaconda.com/distribution/#download-section" target="_blank">Anaconda Download</a>
						</div>
					</p>

					<p>
						Previous Anaconda versions can be found in their <a href="https://repo.anaconda.com/archive/" target="_blank">archive</a>, and
						official install docs can be found <a href="https://docs.anaconda.com/anaconda/install/linux/" target="blank">here</a>.
					</p>

					<p>
						Briefly, once the install file is in the location you wish to install Anaconda, you will simply type:
					</p>

					<code>bash [install file].sh</code>

					<p>
						Follow the prompts to complete installation.
					</p>


					<a name="env"></a>
					<div id="section_sep_top"></div>
					<div id="section_line"></div>
					<div id="section_sep_btm"></div>

					<h2>Anaconda environments</h2>

					<p>
						After installing Anaconda you will have to create and manage Anaconda envrionments. Envrionments can be powerful because they let you easily install
						and manage software locally. For instance, you could set up a main environment that is kept up to date with the latest versions
						of critical software, such as samtools, GATK, IQ-Tree, etc. But if you have a specific workflow that is dependent on an old version
						of, say, GATK, you could set up another enviornment with that version.
					</p>

					<p>
						Here are the official docs for managing conda enviornments: 
					</p>


					<div id="imp_link_cont">
						<a id="imp_link" href="https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html" target="_blank">Anaconda Environments</a>
					</div>

					<p>
						Below I will run through some of the basics.
					</p>


					<a name="env-start"></a>
					<div id="section_sep_top"></div>	
					<h4>01. Starting Anaconda</h4>
			
					<p>First, everytime you login, you will have to start Anaconda:</p>

					<code>source ~/anaconda3/bin/activate</code>


					<a name="env-create"></a>
					<div id="section_sep_top"></div>	
					<h4>02. Creating an environment</h4>

					<p>
						Your command prompt should now have the <code>(base)</code> prefix, indicating you are in the base Anaconda environment.
						Next you will need to create a new environment. You should name your environment something descriptive like "gatk3-env" or
						"biomain". For this example, I will call my main environment "biotools". To create the "biotools" environment type:
					</p>

					<code>conda create --name biotools</code>
						
					<p>
						Some information will print to the screen, and you will be asked to confirm creation of the environment. Confirm and then your environment
						should be created! The command prompt prefix should now be the name of your environment (<code>biotools</code> in this example).
					</p>

					<p>
						In the event that you encounter Permission denied or similar errors when creating an environment, you may provide the full path to
						the environment you want to create as the name:
					</p>

					<code>conda	create --name /path/to/anaconda3/envs/biotools</code>			
					

					<a name="env-start"></a>
					<div id="section_sep_top"></div>	
					<h4>03. Starting an environment</h4>

					<p>
						To start a particular enviornment, be sure Anaconda is running ((base) is in your prompt), and run:
					</p>

					<code>conda activate [env name]</code>

					<p>
						The command prompt prefix should now be the name of your environment and all the software installed in that environment should
						be available to you.
					</p>

					<div id="msg_cont">
						<div id="msg">
							<div id="rec_banner">Recommendation</div>
							<div id="rec_text">
								<p>
									I recommend adding the following commands to your <code>.bash_profile</code> file so they are run automatically everytime
									you log in.
								</p>
								<center><code>source ~/anaconda3/bin/activate</code></center>
								<center><code>conda activate [env name]</code></center>
								<p></p>

							</div>
						</div>
					</div>


					<a name="env-install"></a>
					<div id="section_sep_top"></div>	
					<h4>04. Installing software in an environment</h4>

					<p>
						To install software in this environment, search for the package you want on <a href="https://anaconda.org/bioconda" target="_blank">bioconda</a> 
						and run the appropriate command. For example, to install samtools:
					</p>

					<code>conda install -c bioconda samtools</code>

					<p>Install as much software as you like! It should all be self-contained within this environment.</p>

					<p>Note that if you need a specific version of a package installed, you can specify the version number when installing as follows:</p>

					<code>conda install -c bioconda samtools=1.9</code>

					<a name="env-exit"></a>
					<div id="section_sep_top"></div>	
					<h4>05. Exiting an environment</h4>

					<p>
						When you are in an environment and wish to exit it, simply type:
					</p>

					<code>conda deactivate</code>

					<p>
						If you are in an environment, this will take you to the (base) Anaconda state. If you are in (base), it will exit Anaconda.
					</p>	


					<a name="modules"></a>
					<div id="section_sep_top"></div>
					<div id="section_line"></div>
					<div id="section_sep_btm"></div>

					<h2>The module system and server-wide installs</h2>

					<p>
						There <em>is</em> a module system on Griz, but it seems like this won't be used. If you request something to be installed, 
						instead of server-wide installs, Griz is likely to follow the Carnation protocol. This means you email 
						the admins with your request, and they will	set up a separate conda environment specifically for it. 
						This is less than optimal for our purposes.
					</p>


					<a name="installs"></a>
					<div id="section_sep_top"></div>
					<div id="section_line"></div>
					<div id="section_sep_btm"></div>

					<h2>Building from source or installing binaries yourself</h2>

					<p>
						It is of course still possible to install software yourself locally if you wish to forego Anaconda, but there's no way to
						guarantee that all dependencies will be installed for a given piece of software.
					</p>


					<a name="r"></a>
					<div id="section_sep_top"></div>
					<div id="section_line"></div>
					<div id="section_sep_btm"></div>

					<h2>Installing & Using R</h2>

					<p>
						One of the administrators has a self-compiled version of R that has been optimized somehow. He recommends using this for now by running:
					</p>

					<code>source /share/apps/R-3.6.1/runNewR.sh</code>

					<p>
						However, I am uncertain how this will be maintained in the future. R is available as a module, but again I don't know how that will be maintained.
						Our best solution may be to install R ourselves. Fortunately, this is easy with Anaconda. Be sure you are in the environment in which you want to 
						run R and type:
					</p>

					<code>conda install -c bioconda r</code>

					<p>
						Package installations may be a bit slower and show some bioconda messages/warnings, but they should still work. Let me know if you run into any problems!
					</p>

					<div id="msg_cont">
						<div id="msg">
							<div id="rec_banner">Recommendation</div>
							<div id="rec_text">
								<p>
									It may be helpful to install R in a separate conda environment from your main one.
								</p>
								<center><code>source ~/anaconda3/bin/activate</code></center>
								<center><code>conda activate [env name]</code></center>
								<p></p>

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
pagefile = "install.html";
print("Generating " + pagefile + "...");
title = "Griz - Installing Software"

head = RC.readHead(title, pagefile, "griz");
nav = RC.readNav(pagefile, "griz");
footer = RC.readFooter();

outfilename = "../../griz/" + pagefile;

with open(outfilename, "w") as outfile:
    outfile.write(html_template.format(head=head, nav=nav, footer=footer));