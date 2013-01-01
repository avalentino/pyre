# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2013 all rights reserved
#


"""
Definitions for all the exceptions raised by this package
"""


# violation notification
# constraints throw exceptions rather than return True|False
from ..framework.exceptions import FrameworkError


class ConstraintViolationError(FrameworkError):
    """
    Exception used to indicate that a constraint is violated

    Instead of being functions that return booleans, constraints throw exceptions when they are
    violated. This design choice is motivated by the observation that it is not always possible
    to handle a constraint violation locally, since the caller may not have enough information
    to handle the failure.
    """

    def __init__(self, constraint, value, **kwds):
        msg  = "{0.value!r} violates the constraint ({0.constraint})"
        super().__init__(description=msg, **kwds)
        self.constraint = constraint
        self.value = value
        return



# end of file 
