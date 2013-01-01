# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2013 all rights reserved
#


# packages
import collections


# super-classes
from .Channel import Channel
from .Diagnostic import Diagnostic


# declaration
class Info(Diagnostic, Channel):
    """
    This class is the implementation of the info channel
    """

    # public data
    severity = "info"

    # class private data
    _index = collections.defaultdict(Channel.Enabled)


# end of file 
