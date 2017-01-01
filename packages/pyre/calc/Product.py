# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# orthologue
# (c) 1998-2017 all rights reserved
#


import operator
import functools


class Product:
    """
    The representation of the product of nodes
    """


    # interface
    def getValue(self):
        """
        Compute and return my value
        """
        # compute and return my value
        return functools.reduce(operator.mul, (op.value for op in self.operands))


# end of file
