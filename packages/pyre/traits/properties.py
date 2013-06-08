# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2013 all rights reserved
#


"""
This package provides access to the factories for typed properties
"""

# get the typed class
from .Property import Property as property

# for convenience, expose the typed ones
# the simple ones
bool = property.bool
decimal = property.decimal
float = property.float
inet = property.inet
int = property.int
identity = property.identity
str = property.str

# the more complex types
date = property.date
dimensional = property.dimensional
time = property.time
uri = property.uri

# containers
array = property.array
list = property.list
set = property.set
tuple = property.tuple

# meta
istream = property.istream
ostream = property.ostream

from .Facility import Facility as facility

# meta-properties: trait descriptors for homogeneous containers; these require other trait
# descriptors to specify the type of the contents
from .Dict import Dict as dict


# common meta-descriptors
def strings(default=list, **kwds):
    """
    A list of strings
    """
    # build a descriptor that describes a list of strings
    return list(schema=str(), default=default, **kwds)


def paths(default=list, **kwds):
    """
    A list of URIs
    """
    # build a descriptor that describes a list of uris and return it
    return list(schema=uri(), default=default, **kwds)


def catalog(**kwds):
    """
    A {dict} of {list}s
    """
    return dict(schema=list(**kwds))


# end of file 
