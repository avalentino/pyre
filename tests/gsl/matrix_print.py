#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2013 all rights reserved
#


"""
Make a matrix, fill it with a constant, and print it
"""


def test():
    # package access
    import gsl
    # make a matrix
    m = gsl.matrix(shape=(3,3))
    # set it to some value
    m.fill(value=2)
    # print it
    m.print(indent=' '*4)
    # all done
    return m


# main
if __name__ == "__main__":
    test()


# end of file 
