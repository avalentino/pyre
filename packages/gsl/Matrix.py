# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2012 all rights reserved
#


# externals
import numbers
from . import gsl # the extension


# the class declaration
class Matrix:
    """
    A wrapper over a gsl matrix
    """

    # types
    from .Vector import Vector as vector

    # constants
    upperTriangular = 1
    lowerTriangular = 0


    # public data
    @property
    def columns(self):
        """
        Get the number of columns
        """
        return self.shape[1]

    @property
    def rows(self):
        """
        Get the number of rows
        """
        return self.shape[0]


    # initialization
    def zero(self):
        """
        Set all my elements to zero
        """
        # zero me out
        gsl.matrix_zero(self.data)
        # and return
        return self


    def fill(self, value):
        """
        Set all my elements to {value}
        """
        # fill
        gsl.matrix_fill(self.data, value)
        # and return
        return self


    def identity(self):
        """
        Initialize me as an identity matrix: all elements are set to zero except along the
        diagonal, which are set to one
        """
        # initialize
        gsl.matrix_identity(self.data)
        # and return
        return self


    def random(self, pdf):
        """
        Fill me with random numbers using the probability distribution {pdf}
        """
        # the {pdf} knows how to do this
        return pdf.matrix(matrix=self)


    def clone(self):
        """
        Allocate a new matrix and initialize it using my values
        """
        # build the clone
        clone = type(self)(shape=self.shape)
        # have the extension initialize the clone
        gsl.matrix_copy(clone.data, self.data)
        # and return it
        return clone

    # matrix operations
    def transpose(self, destination=None):
        """
        Compute the transpose of a matrix. 

        If {destination} is {None} and the matrix is square, the operation happens
        in-place. Otherwise, the transpose is stored in {destination}, which is assumed to be
        shaped correctly.
        """
        # if we have a {destination}
        if destination is not None:
            # do the transpose
            gsl.matrix_transpose(self.data, destination.data)
            # and return the destination matrix
            return destination
        # otherwise
        gsl.matrix_transpose(self.data, None)
        # and return myself
        return self


    # slicing
    def getRow(self, index):
        """
        Return a view to the requested row
        """
        # let the extension do its thing
        capsule = gsl.matrix_get_row(self.data, index)
        # build a vector and return it
        return self.vector(shape=self.columns, data=capsule)


    def getColumn(self, index):
        """
        Return a view to the requested column
        """
        # let the extension do its thing
        capsule = gsl.matrix_get_col(self.data, index)
        # build a vector and return it
        return self.vector(shape=self.rows, data=capsule)


    # maxima and minima
    def max(self):
        """
        Compute my maximum value
        """
        # easy enough
        return gsl.matrix_max(self.data)


    def min(self):
        """
        Compute my maximum value
        """
        # easy enough
        return gsl.matrix_min(self.data)


    def minmax(self):
        """
        Compute my minimum and maximum values
        """
        # easy enough
        return gsl.matrix_minmax(self.data)


    # meta methods
    def __init__(self, shape, data=None, **kwds):
        super().__init__(**kwds)
        self.shape = shape
        self.data = gsl.matrix_alloc(shape) if data is None else data
        return


    # container support
    def __iter__(self):
        # unpack the shape
        index0, index1 = self.shape
        # iterate over all the elements
        for i in range(index0):
            for j in range(index1):
                yield gsl.matrix_get(self.data, (i, j))
        # all done
        return


    def __contains__(self, value):
        # faster than checking every element in python
        return gsl.matrix_contains(self.data, value)


    def __getitem__(self, index):
        # get and return the element
        return gsl.matrix_get(self.data, index)


    def __setitem__(self, index, value):
        # set the element to the requested value
        return gsl.matrix_set(self.data, index, value)


    # comparisons
    def __eq__(self, other):
        # type check
        if type(self) is not type(other): return NotImplemented
        # hand the request off to the extension module
        return gsl.matrix_equal(self.data, other.data)


    def __ne__(self, other):
        return not (self == other)


    # in-place arithmetic
    def __iadd__(self, other):
        """
        In-place addition with the elements of {other}
        """
        # if other is a matrix
        if type(other) is type(self):
            # do matrix-matrix addition
            gsl.matrix_add(self.data, other.data)
            # and return
            return self
        # if other is a number
        if isinstance(other, numbers.Number):
            # do constant addition
            gsl.matrix_shift(self.data, float(other))
            # and return
            return self
        # otherwise, let the interpreter know
        raise NotImplemented


    def __isub__(self, other):
        """
        In-place subtraction with the elements of {other}
        """
        # if other is a matrix
        if type(other) is type(self):
            # do matrix-matrix subtraction
            gsl.matrix_sub(self.data, other.data)
            # and return
            return self
        # if other is a number
        if isinstance(other, numbers.Number):
            # do constant subtraction
            gsl.matrix_shift(self.data, -float(other))
            # and return
            return self
        # otherwise, let the interpreter know
        raise NotImplemented


    def __imul__(self, other):
        """
        In-place multiplication with the elements of {other}
        """
        # if other is a matrix
        if type(other) is type(self):
            # do matrix-matrix multiplication
            gsl.matrix_mul(self.data, other.data)
            # and return
            return self
        # if other is a number
        if isinstance(other, numbers.Number):
            # do scaling by constant
            gsl.matrix_scale(self.data, float(other))
            # and return
            return self
        # otherwise, let the interpreter know
        raise NotImplemented


    def __itruediv__(self, other):
        """
        In-place addition with the elements of {other}
        """
        # if other is a matrix
        if type(other) is type(self):
            # do matrix-matrix division
            gsl.matrix_div(self.data, other.data)
            # and return
            return self
        # if other is a number
        if isinstance(other, numbers.Number):
            # do scaling by constant
            gsl.matrix_scale(self.data, 1/float(other))
            # and return
            return self
        # otherwise, let the interpreter know
        raise NotImplemented


    # private data
    data = None
    shape = (0,0)


# end of file 
