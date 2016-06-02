# -*- Makefile -*-
#
# authors:
#   Michael Aïvázis <michael.aivazis@para-sim.com>
#   Raúl Radovitzky <raul.radovitzky@para-sim.com>
#
# (c) 2013-2016 all rights reserved
#


# project settings
include {project.name}.def
# the package
PACKAGE = graphics

# the location
EXPORT_WEBDIR = $(EXPORT_ROOT)/web/www/$(PROJECT)/$(PACKAGE)
# the exported items
EXPORT_WEB = *.png

# targets
all: export

export:: export-web

live: live-web-package

# end of file
