#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2013 all rights reserved
#


"""
Exercise {dtrsv}
"""


def test():
    # get the package
    import gsl

    # the vector x
    x = gsl.vector(shape=3)
    x[0], x[1], x[2] = 1,2,3
    # the matrix A
    A = gsl.matrix(shape=(3,3)).identity()

    # compute the form
    y = gsl.blas.dtrsv(A.upperTriangular, A.opTrans, A.unitDiagonal, A, x.clone())
    
    # check
    # print(tuple(y))
    assert tuple(y) == tuple(x)

    # all done
    return


# main
if __name__ == "__main__":
    test()


# end of file 
