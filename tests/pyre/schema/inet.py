#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2013 all rights reserved
#


"""
Exercise the internet address parser
"""


def test():
    # get the package parts
    from pyre.schema.INet import (
        INet as inet,
        IPv4 as ipv4,
        Unix as unix)

    # positive tests
    # ip4 with full information
    address = inet.coerce("ip4:pyre.caltech.edu:50000")
    assert address.family == ipv4.family
    assert address.host == "pyre.caltech.edu"
    assert address.port == 50000
    assert address.value == ("pyre.caltech.edu", 50000)

    # ip4 with no family
    address = inet.coerce("pyre.caltech.edu:50000")
    assert address.family == ipv4.family
    assert address.host == "pyre.caltech.edu"
    assert address.port == 50000
    assert address.value == ("pyre.caltech.edu", 50000)

    # ip4 with no port
    address = inet.coerce("ip4:pyre.caltech.edu")
    assert address.family == ipv4.family
    assert address.host == "pyre.caltech.edu"
    assert address.port == 0
    assert address.value == ("pyre.caltech.edu", 0)

    # ip4 with no family or port
    address = inet.coerce("pyre.caltech.edu")
    assert address.family == ipv4.family
    assert address.host == "pyre.caltech.edu"
    assert address.port == 0
    assert address.value == ("pyre.caltech.edu", 0)

    # unix
    address = inet.coerce("unix:/tmp/.s.5394")
    assert address.family == unix.family
    assert address.path == "/tmp/.s.5394"
    assert address.value == "/tmp/.s.5394"
    
    address = inet.coerce("local:/tmp/.s.5394")
    assert address.family == unix.family
    assert address.path == "/tmp/.s.5394"
    assert address.value == "/tmp/.s.5394"
    
    return


# main
if __name__ == "__main__":
    # skip pyre initialization since we don't rely on the executive
    pyre_noboot = True
    # do...
    test()


# end of file 
