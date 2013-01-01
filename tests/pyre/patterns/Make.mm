# -*- Makefile -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2013 all rights reserved
#


PROJECT = pyre

#--------------------------------------------------------------------------
#

all: test

test: sanity utils patterns

sanity:
	${PYTHON} ./sanity.py

utils:
	${PYTHON} ./powerset.py

patterns:
	${PYTHON} ./classifier.py
	${PYTHON} ./extent.py
	${PYTHON} ./named.py
	${PYTHON} ./observable.py
	${PYTHON} ./pathhash.py
	${PYTHON} ./singleton.py


# end of file 
