# -*- Makefile -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2010 all rights reserved
#


PROJECT = pyre
PACKAGE = constraints
PROJ_DISTCLEAN = $(EXPORT_MODULEDIR)/$(PACKAGE)


#--------------------------------------------------------------------------
#

all: export

#--------------------------------------------------------------------------
# export

EXPORT_PYTHON_MODULES = \
    And.py \
    Between.py \
    Constraint.py \
    Equal.py \
    Greater.py \
    GreaterEqual.py \
    Less.py \
    LessEqual.py \
    Like.py \
    Not.py \
    Or.py \
    Set.py \
    Subset.py \
    __init__.py


export:: export-package-python-modules


# end of file 
