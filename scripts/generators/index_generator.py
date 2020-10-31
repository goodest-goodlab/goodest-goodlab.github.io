############################################################
# For personal site, 03.20
# This generates the file "index.html"
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
	<div class="pure-u-24-24" id="header">Goodest Good lab</div>
	
	{nav}

		<div class="pure-u-24-24" id="server_sep_div"></div>
		<div class="pure-u-2-24" id="margin"></div>
		<div class="pure-u-20-24" id="link_text">
            <h1>Web resources for the Good Lab!</h1>

			
		</div>
        <div class="pure-u-2-24" id="margin"></div>

		<div class="pure-u-24-24" id="sep_div"></div>

    {footer}
</body>
"""

######################
# Main block
######################
pagefile = "index.html";
print("Generating " + pagefile + "...");
title = "Good lab"

head = RC.readHead(title, pagefile, "servers");
nav = RC.readNav(pagefile, "main");
footer = RC.readFooter();

outfilename = "../../" + pagefile;

with open(outfilename, "w") as outfile:
    outfile.write(html_template.format(head=head, nav=nav, footer=footer));