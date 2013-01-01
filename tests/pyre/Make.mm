# -*- Makefile -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2013 all rights reserved
#


PROJECT = pyre

RECURSE_DIRS = \
    patterns \
    tracking \
    parsing \
    filesystem \
    xml \
    algebraic \
    calc \
    schema \
    units \
    constraints \
    records \
    tabular \
    codecs \
    config \
    framework \
    components \
    timers \
    weaver \
    db \
    ipc \
    platforms \
    shells \
    pyre

#--------------------------------------------------------------------------
#

all: 
	BLD_ACTION="all" $(MM) recurse

test::
	BLD_ACTION="test" $(MM) recurse

tidy::
	BLD_ACTION="tidy" $(MM) recurse

clean::
	BLD_ACTION="clean" $(MM) recurse

distclean::
	BLD_ACTION="distclean" $(MM) recurse


# end of file 
