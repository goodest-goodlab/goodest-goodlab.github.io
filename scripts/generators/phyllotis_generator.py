############################################################
# For ConGen2020 site, 08.20
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
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1">	
        <link rel='shortcut icon' href='img/favicon.ico' type='image/x-icon'/ >
        <link type="text/css" rel="stylesheet" href="../css/global.css"  media="screen,projection" />
        <link type="text/css" rel="stylesheet" href="../css/grid.css"  media="screen,projection" />
        <link type="text/css" rel="stylesheet" href="../css/pure.css"  media="screen,projection" />
        <link href="https://fonts.googleapis.com/css?family=Lato:300" rel="stylesheet"> 
        <title>Phyllotis genome</title>
    </head>

<body>
    <div class="row" id="header">Phyllotis xanthopygus genome resources</div>
    {nav}

    <div class="row" id="sep_div"></div>
    <div class="row" id="link-row">
    <div class="col-6-24" id="margin"></div>
    <div class="col-12-24" id="link-col">
        <h2>Genome assembly</h2>
        <ul>
            <li><h4><a href="UNI1803_hifiasm_hirise_report.html">hifiasm hirise assembly report</a></h4></li>
            <li><h4><a href="hifiasm_tad_report.html">hifiasm TAD report</a></h4></li>
            <li><h4><a href="UNI1803_peregrine_hirise_report.html">Peregrine hirise assembly report</a></h4></li>
            <li><h4><a href="peregrine_tad_report.html">Peregeine TAD report</a></h4></li>
            <li><h4><a href="DTG-OmniC-263_R1_001_fastqc.html">OmniC read pair 1 FastQC report</a></h4></li>
            <li><h4><a href="DTG-OmniC-263_R2_001_fastqc.html">OmniC read pair 2 FastQC report</a></h4></li>
            <li><h4><a href="annotation.html">Annotation stats</a></h4></li>
        </ul>
    </div>
    <div class="col-6-24" id="margin"></div>
    </div>

    <div class="col-6-24" id="margin"></div>
    <div class="col-12-24" id="link-col">
        <h2>Phyllotis population samples</h2>
        <ul>
            <li><h4><a href="multiqc_report_trimming.html">Read quality</a></h4></li>
            <li><h4><a href="multiqc_report_raw_bams.html">Mapping report</a></h4></li>
        </ul>
    </div>
    <div class="col-6-24" id="margin"></div>
    </div>

    <div class="row" id="sep_div"></div>
    <div class="row" id="img-row">
        <div class="col-8-24" id="margin"></div>
        <div class="col-8-24" id="img-col">
            <div id="img-cont">
                <img id="hero-img" src="../img/phyllotis-xanthopygus.jpg">
            </div>
            <center><span class="fig-caption"><a href="https://www.sciencenews.org/article/south-american-mouse-world-highest-dwelling-mammal" target="_blank">Source</a></a></span></center>
        </div>
        <div class="col-8-24" id="margin"></div>
    </div>
    <div class="row" id="sep_div"></div>
    <div class="row" id="sep_div"></div>
    <div class="row" id="sep_div"></div>

    {footer}

</body>
</html>
"""

######################
# Main block
######################
pagefile = "phyllotis/index.html";
print("Generating " + pagefile + "...");
title = "Good lab"

head = RC.readHead(title, pagefile, "servers");
nav = RC.readNav(pagefile, "main");
footer = RC.readFooter();

outfilename = "../../" + pagefile;

with open(outfilename, "w") as outfile:
    outfile.write(html_template.format(head=head, nav=nav, footer=footer));