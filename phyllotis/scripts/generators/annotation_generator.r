############################################################
# For rodent web, 01.20
# This generates the file "annotation.html"
############################################################


cat("Rendering annotation.rmd/html\n")
Sys.setenv(RSTUDIO_PANDOC="C:/Program Files/RStudio/bin/pandoc/")
library(rmarkdown)
setwd("C:/bin/goodest-goodlab.github.io/phyllotis/scripts/generators")
output_dir = "../.."
render("../markdown/annotation.rmd", output_dir = output_dir, params = list(output_dir = output_dir), quiet = TRUE)