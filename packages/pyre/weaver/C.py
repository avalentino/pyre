# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2011 all rights reserved
#


# access to the pyre package
import pyre
# my ancestor
from .BlockMill import BlockMill


# my declaration
class C(BlockMill):
    """
    Support for C
    """


    # traits
    languageMarker = pyre.properties.str(default='C')
    languageMarker.doc = "the variant to use in the language marker"

    
    # meta methods
    def __init__(self, **kwds):
        super().__init__(startBlock='/*', commentMarker=' *', endBlock='*/', **kwds)
        return


# end of file 
