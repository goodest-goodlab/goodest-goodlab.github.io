############################################################
# For personal site, 11.19
# This generates the file "servers.html"
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


    <div class="pure-g" id="main_div_links">
	<div class="pure-u-24-24" id="header">Good lab computational resources</div>
	
	{nav}

		<div class="pure-u-24-24" id="server_sep_div"></div>
		<div class="pure-u-2-24" id="margin"></div>
		<div class="pure-u-20-24" id="link_text">
			<a name="musculus"></a>	
			<div class="pure-g">
					<div class="pure-u-2-24" id="margin"></div>
					<div class="pure-u-20-24" id="server_row">
						<div id="server_img_cont">
							<h1>Musculus</h1>
							<img class="pure-img" id="server_img" src="img/logo/musculus.png">
						</div>
						<div id="server_desc">
							<h1>musculus.dbs.umt.edu:22</h1>

							<table id="sum-tab">
								<tr><td class="td-label">Access: </td><td>Good lab</td></tr>
								<tr><td class="td-label">Purpose: </td><td>Main Good lab server for running jobs.</td></tr>
								<tr><td class="td-label">Operating System: </td><td>Linux version 4.4.0-135-generic</td></tr>
								<tr><td class="td-label">Processor: </td>
									<td>
										<b>32 threads: </b>
										<a href="https://ark.intel.com/content/www/us/en/ark/products/64590/intel-xeon-processor-e5-2650-20m-cache-2-00-ghz-8-00-gt-s-intel-qpi.html" target="_blank">
										Intel Xeon Processor E5-2650 @ 2GHz</a> (2 CPUs x 8 cores per CPU x 2 threads per core)
									</td>
								</tr>
								<tr><td class="td-label">Memory: </td><td>200GB</td></tr>
								<tr><td class="td-label">Storage:</td><td>One 40TB HDD containing one partition and several logical volumes</td></tr>
							</table>

							<center>
							<table id="vol-tab">
								<thead><th>Volume name</th><th>Path</th><th>Capactity</th></thead>
								<tr><td><em>home</em></td><td>/home</td><td>3TB</td></tr>
								<tr><td><em>data</em></td><td>/data</td><td>15TB</td></tr>
								<tr><td><em>scratch</em></td><td>/scratch/1</td><td>10TB</td></tr>
								<tr><td><em>morescratch</em></td><td>/scratch/2</td><td>2TB</td></tr>
							</table>
							</center>
						</div>
					</div>
					<div class="pure-u-2-24" id="margin"></div>
				</div>

				<div class="pure-u-24-24" id="server_sep_div"></div>
				<div class="pure-u-2-24" id="margin"></div>
				<div class="pure-u-20-24" id="server_line"></div>
				<div class="pure-u-2-24" id="margin"></div>
				
				<a name="lepus"></a>
				<div class="pure-g">
					<div class="pure-u-2-24" id="margin"></div>
					<div class="pure-u-20-24" id="server_row">
						<div id="server_img_cont">
							<h1>Lepus</h1>
							<img class="pure-img" id="server_img" src="img/logo/lepus.png">
						</div>
						<div id="server_desc">
							<h1>lepus.dbs.umt.edu:22</h1>

							<table id="sum-tab">
								<tr><td class="td-label">Access: </td><td>Good lab</td></tr>
								<tr><td class="td-label">Purpose: </td><td>Main Good lab server for active data storage.</td></tr>
								<tr><td class="td-label">Operating System: </td><td>Linux version 4.4.0-109-generic</td></tr>
								<tr><td class="td-label">Processor: </td>
									<td>
										<b>32 threads: </b>
										<a href="https://ark.intel.com/content/www/us/en/ark/products/64590/intel-xeon-processor-e5-2650-20m-cache-2-00-ghz-8-00-gt-s-intel-qpi.html" target="_blank">
											Intel Xeon Processor E5-2650 @ 2GHz</a> (2 CPUs x 8 cores per CPU x 2 threads per core)
									</td>
								</tr>
								<tr><td class="td-label">Memory: </td><td>200GB</td></tr>
								<tr><td class="td-label">Storage:</td>
									<td>
										30TB partition for data</br>
										2TB partition for users</br>
									</td>
								</tr>
							</table>

							<!--<center>
							<table id="vol-tab">
								<thead><th>Partition name</th><th>Path</th><th>Capactity</th></thead>
								<tr><td><em>home</em></td><td>/home</td><td>3.3TB</td></tr>
								<tr><td><em>data</em></td><td>/data</td><td>7.5TB</td></tr>
								<tr><td><em>scratch</em></td><td>/scratch/1</td><td>11TB</td></tr>
								<tr><td><em>scratch2</em></td><td>/scratch/2</td><td>3.7TB</td></tr>
								<tr><td><em>scratch3</em></td><td>/scratch/3</td><td>3.7TB</td></tr>
							</table>
							</center>-->
						</div>
					</div>
					<div class="pure-u-2-24" id="margin"></div>
				</div>

				<div class="pure-u-24-24" id="server_sep_div"></div>
				<div class="pure-u-2-24" id="margin"></div>
				<div class="pure-u-20-24" id="server_line"></div>
				<div class="pure-u-2-24" id="margin"></div>

				<a name="rattus"></a>	
				<div class="pure-g">
					<div class="pure-u-2-24" id="margin"></div>
					<div class="pure-u-20-24" id="server_row">
						<div id="server_img_cont">
							<h1>Rattus</h1>
							<img class="pure-img" id="server_img" src="img/logo/rat.png">
						</div>
						<div id="server_desc">
							<h1>lepus.dbs.umt.edu:22</h1>

							<table id="sum-tab">
								<tr><td class="td-label">Access: </td><td>Admin FTP access only</td></tr>
								<!-- <tr><td class="td-label">Operating System: </td><td></td></tr>
								<tr><td class="td-label">Processor: </td><td></td></tr>
								<tr><td class="td-label">Memory: </td><td></td></tr> -->
								<tr><td class="td-label">Storage:</td><td>12 HDD x 16TB (192TB) Network attached storage</td>
								</tr>
							</table>

							<!-- <center>
							<table id="vol-tab">
								<thead><th>Partition name</th><th>Path</th><th>Capactity</th></thead>
							</table>
							</center> -->
						</div>
					</div>
					<div class="pure-u-2-24" id="margin"></div>
				</div>

				<div class="pure-u-24-24" id="server_sep_div"></div>
				<div class="pure-u-2-24" id="margin"></div>
				<div class="pure-u-20-24" id="server_line"></div>
				<div class="pure-u-2-24" id="margin"></div>

				<a name="carnation"></a>	
				<div class="pure-g">
					<div class="pure-u-2-24" id="margin"></div>
					<div class="pure-u-20-24" id="server_row">
						<div id="server_img_cont">
							<h1><a href="http://hs.umt.edu/dbs/labs/genomics/bioinformatics/servers.php" target="_blank">Carnation</a></h1>
							<img class="pure-img" id="server_img" src="img/logo/carnation.png">
						</div>
						<div id="server_desc">
							<h1>carnation.dbs.umt.edu:2225</h1>

							<table id="sum-tab">
								<tr><td class="td-label">Access: </td><td><a href="http://hs.umt.edu/dbs/labs/genomics/default.php" target="_blank">Genomics Core Laboratory</a></td></tr>
								<tr><td class="td-label">Operating System: </td><td>Linux version 4.4.0-104-generic</td></tr>
								<tr><td class="td-label">Processor: </td>
									<td>
										<b>128 threads</b>: 
										<a href="https://ark.intel.com/content/www/us/en/ark/products/84680/intel-xeon-processor-e7-8860-v3-40m-cache-2-20-ghz.html" target="_blank">
										Intel Xeon CPU E7-8860 v3 @ 2.20GHz</a> (4 CPUs x 16 cores per CPU x 2 threads per core)
									</td>
								</tr>
								<tr><td class="td-label">Memory: </td><td>2TB</td></tr>
								<tr><td class="td-label">Storage:</td><td>200TB</td></tr>
								<tr><td class="td-label">Summary:</td><td><a href="http://hs.umt.edu/dbs/labs/genomics/bioinformatics/servers.php" target="_blank">http://hs.umt.edu/dbs/labs/genomics/bioinformatics/servers.php</a></td></tr>
							</table>

						</div>
					</div>
					<div class="pure-u-2-24" id="margin"></div>
				</div>

				<div class="pure-u-24-24" id="server_sep_div"></div>
				<div class="pure-u-2-24" id="margin"></div>
				<div class="pure-u-20-24" id="server_line"></div>
				<div class="pure-u-2-24" id="margin"></div>

				<a name="reincarnation"></a>	
				<div class="pure-g">
					<div class="pure-u-2-24" id="margin"></div>
					<div class="pure-u-20-24" id="server_row">
						<div id="server_img_cont">
							<h1>Reincarnation</h1>
							<img class="pure-img" id="server_img" src="img/logo/reincarnation.png">
						</div>
						<div id="server_desc">
							<h4>Now incorporated into the Griz cluster! See <a href="griz/nodes.html#reincarnation">Griz node info</a> for stats.</h4>
						</div>
					</div>
					<div class="pure-u-2-24" id="margin"></div>
				</div>


				<div class="pure-u-24-24" id="server_sep_div"></div>
				<div class="pure-u-2-24" id="margin"></div>
				<div class="pure-u-20-24" id="server_line"></div>
				<div class="pure-u-2-24" id="margin"></div>

				<a name="griz"></a>	
				<div class="pure-g">
					<div class="pure-u-2-24" id="margin"></div>
					<div class="pure-u-20-24" id="server_row">
						<div id="server_img_cont">
							<h1><a href="http://docs.gscc.umt.edu/overview/hardware/" target="_blank">Griz</a></h1>
							<img class="pure-img" id="server_img" src="img/logo/griz.png">
						</div>
						<div id="server_desc">
							<h1>login.gscc.umt.edu</h1>

							<table id="sum-tab">
								<tr><td class="td-label">Access: </td><td>Limited currently, University-wide eventually</td></tr>
								<tr><td class="td-label">Summary:</td><td><a href="http://docs.gscc.umt.edu/overview/hardware/" target="_blank">Griz docs</a></td></tr>
								<tr><td class="td-label">Login info: </td><td>NetID and password</td></tr>
								<tr><td class="td-label">Compute info: </td><td>See <a href="griz/nodes.html#reincarnation">Griz node info</a> for stats.</td></tr>
							</table>
						</div>
					</div>
					<div class="pure-u-2-24" id="margin"></div>
				</div>

				<div class="pure-g">
					<div class="pure-u-2-24" id="margin"></div>
					<div class="pure-u-20-24"><h2>Griz links</h2></div>
					<div class="pure-u-2-24" id="margin"></div>
				</div>


				<div class="pure-g" id="griz_links">
					<div class="pure-u-2-24" id="margin"></div>

					<div class="pure-u-3-24" id="griz_link_cont">
						<a href="griz/start.html">Getting Started</a>
					</div>

					<div class="pure-u-3-24" id="griz_link_cont">
						<a href="griz/files.html">Transfer & Store Files</a>
					</div>

					<div class="pure-u-3-24" id="griz_link_cont">
						<a href="griz/install.html">Installing Software</a>
					</div>

					<div class="pure-u-3-24" id="griz_link_cont">
						<a href="griz/jobs.html">Running Jobs</a>
					</div>

					<div class="pure-u-3-24" id="griz_link_cont">
						<a href="griz/nodes.html">Node Info</a>
					</div>

					<div class="pure-u-3-24" id="griz_link_cont">
						<a href="griz/links.html">Other Links</a>
					</div>

					<div class="pure-u-3-24" id="margin"></div>

				</div>

			</div>
		</div>
		<div class="pure-u-2-24" id="margin"></div>

		<div class="pure-u-24-24" id="sep_div"></div>

    {footer}
</body>
"""

######################
# Main block
######################
pagefile = "servers.html";
print("Generating " + pagefile + "...");
title = "Good lab - Servers"

head = RC.readHead(title, pagefile, "servers");
nav = RC.readNav(pagefile, "servers");
footer = RC.readFooter();

outfilename = "../../" + pagefile;

with open(outfilename, "w") as outfile:
    outfile.write(html_template.format(head=head, nav=nav, footer=footer));