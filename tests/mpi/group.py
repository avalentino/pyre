#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2013 all rights reserved
#


"""
Verify that communicator groups are accessible
"""


def test():
    # access the package
    import mpi
    # grab the world communicator
    world = mpi.world
    # access the world process group
    whole = world.group()

    # check that I can compute ranks correctly
    assert world.rank == whole.rank

    return


# main
if __name__ == "__main__":
    test()


# end of file 
