# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# orthologue
# (c) 1998-2017 all rights reserved
#


class Sum:
    """
    The representation of the sum of nodes
    """

    # interface
    def getValue(self):
        """
        Compute and return my value
        """
        return sum(operand.value for operand in self.operands)


# end of file
