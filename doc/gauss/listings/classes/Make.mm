# -*- Makefile -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2013 all rights reserved
#

PROJECT = pyre
PACKAGE = doc/gauss/classes

PROJ_TIDY += __pycache__

#--------------------------------------------------------------------------
#

all: test clean

test:
	${PYTHON} ./gauss.py

# end of file
