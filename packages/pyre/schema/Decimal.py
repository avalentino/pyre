# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2011 all rights reserved
#


# access the decimal package
import decimal
# and my superclass
from .Type import Type


class Decimal(Type):
    """
    A class declarator for fixed point numbers
    """


    # interface
    @classmethod
    def pyre_cast(cls, value, **kwds):
        """
        Attempt to convert {value} into a decimal
        """
        # attempt to cast {value} into a decimal
        return decimal.Decimal(value)


# end of file 
