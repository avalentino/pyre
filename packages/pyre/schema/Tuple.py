# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2013 all rights reserved
#


# superclass
from .Container import Container


# declaration
class Tuple(Container):
    """
    The tuple type declarator
    """


    # interface
    def coerce(cls, value, **kwds):
        """
        Convert {value} into a tuple
        """
        # easy enough; resist the temptation to optimize this by skipping the call to super: we
        # have to coerce every item in the container!
        return tuple(super().coerce(value, **kwds))


# end of file 
