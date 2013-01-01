# -*- Makefile -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2013 all rights reserved
#
#


PROJECT = pyre

#--------------------------------------------------------------------------
#


all: test

test: sanity units misc

sanity:
	${PYTHON} ./sanity.py
	${PYTHON} ./exceptions.py

units:
	${PYTHON} ./one.py
	${PYTHON} ./algebra.py

misc:
	${PYTHON} ./parser.py
	${PYTHON} ./formatting.py


# end of file 
