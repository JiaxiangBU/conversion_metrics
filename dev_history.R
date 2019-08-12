file.copy("../mortgage_forecasts/LICENSE", ".")
package_name <- "conversion_metrics"

# once --------------------------------------------------------------------

file.copy("../mortgage_forecasts/setup.py", ".")
read_file("setup.py") %>% str_replace_all("mortgage_forecasts", package_name) %>% write_file("setup.py")
file.edit("setup.py")

file.copy("../mortgage_forecasts/version.py", ".")

file.copy("../mortgage_forecasts/meta.yaml", ".")
read_file("meta.yaml") %>% str_replace_all("mortgage_forecasts", package_name) %>% write_file("meta.yaml")

dir.create("conversion_metrics")
file.copy("../mortgage_forecasts/mortgage_forecasts/__init__.py", "conversion_metrics/", overwrite = TRUE)


# several python script ---------------------------------------------------

file.copy("../mortgage_forecasts/mortgage_forecasts/models.py", "conversion_metrics/ratio.py", overwrite = TRUE)
file.edit("conversion_metrics/ratio.py")

file.copy("../mortgage_forecasts/mortgage_forecasts/models.py", "conversion_metrics/plot.py", overwrite = TRUE)
file.edit("conversion_metrics/plot.py")


# init python script ------------------------------------------------------

file.edit("conversion_metrics/__init__.py")

use_readme_rmd()
file.copy("../mortgage_forecasts/README.Rmd", "README.Rmd", overwrite = TRUE)
file.edit("README.Rmd")

library(tidyverse)
read_file("README.Rmd") %>% str_replace_all("mortgage_forecasts", package_name) %>% write_file("README.Rmd")
rmarkdown::render("README.Rmd")


# build ------------------------------------------------------------

# conda build .

# /Users/vija/miniconda3/conda-bld/noarch
# conversion_metrics-1.0.0-py_1.tar.bz2
# anaconda login
# anaconda upload /Users/vija/miniconda3/conda-bld/noarch/conversion_metrics-1.0.0-py_1.tar.bz2


# readme ------------------------------------------------------------------

file.edit("README.Rmd")
rmarkdown::render("README.Rmd")
rstudioapi::viewer("README.html")
file.remove("README.html")
