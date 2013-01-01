# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2013 all rights reserved
#


# externals
import numbers
from . import gsl # the extension


# the class declaration
class Vector:
    """
    A wrapper over a gsl vector
    """


    # types
    from .Permutation import Permutation as permutation


    # initialization
    def zero(self):
        """
        Set all my elements to zero
        """
        # zero me out
        gsl.vector_zero(self.data)
        # and return
        return self


    def fill(self, value):
        """
        Set all my elements to {value}
        """
        # fill
        gsl.vector_fill(self.data, value)
        # and return
        return self


    def basis(self, index):
        """
        Initialize me as a basis vector: all elements are set to zero except {index}, which is
        set to one
        """
        # initialize
        gsl.vector_basis(self.data, index)
        # and return
        return self


    def random(self, pdf):
        """
        Fill me with random numbers using the probability distribution {pdf}
        """
        # the {pdf} knows how to do this
        return pdf.vector(vector=self)


    def clone(self):
        """
        Allocate a new vector and initialize it using my values
        """
        # build the clone
        clone = type(self)(shape=self.shape)
        # have the extension initialize the clone
        gsl.vector_copy(clone.data, self.data)
        # and return it
        return clone


    def read(self, filename):
        """
        Read my values from {filename}
        """
        # read
        gsl.vector_read(self.data, filename)
        # and return
        return self


    def write(self, filename):
        """
        Write my values to {filename}
        """
        # write
        gsl.vector_write(self.data, filename)
        # and return
        return self


    def print(self, format='{:+12.5e}', width=100, indent=''):
        """
        Print my values using the given {format}
        """
        # print the left margin
        print('{} ['.format(indent), end=' ')
        # the values
        for value in self: print(format.format(value), end=' ')
        # the right margin
        print(']')
        # all done
        return


    # maxima and minima
    def max(self):
        """
        Compute my maximum value
        """
        # easy enough
        return gsl.vector_max(self.data)


    def min(self):
        """
        Compute my maximum value
        """
        # easy enough
        return gsl.vector_min(self.data)


    def minmax(self):
        """
        Compute my minimum and maximum values
        """
        # easy enough
        return gsl.vector_minmax(self.data)


    # statistics
    def sort(self):
        """
        In-place sort of the elements of a vector
        """
        # sort
        gsl.vector_sort(self.data)
        # and return myself
        return self


    def sortIndirect(self):
        """
        Construct the permutation that would sort me in ascending order
        """
        # get the permutation capsule
        pdata = gsl.vector_sortIndex(self.data)
        # build a permutation object and return it
        return self.permutation(shape=self.shape, data=pdata)


    def mean(self, weights=None):
        """
        Compute the mean value of my elements, weighted by the optional {weights}
        """
        # easy enough
        return gsl.vector_mean(self.data, weights.data if weights is not None else None)


    def median(self):
        """
        Compute the median value of my elements; only works on previously sorted vectors
        """
        # easy enough
        return gsl.vector_median(self.data)


    def variance(self, mean=None):
        """
        Compute the variance of my elements with respect to {mean}. If {mean} is {None}, it is
        computed on the fly
        """
        # easy enough
        return gsl.vector_variance(self.data, float(mean) if mean is not None else None)


    def sdev(self, mean=None):
        """
        Compute the mean value of my elements with respect to {mean}. If {mean} is {None}, it
        is computed on the fly
        """
        # easy enough
        return gsl.vector_sdev(self.data, float(mean) if mean is not None else None)


    # meta methods
    def __init__(self, shape, data=None, **kwds):
        super().__init__(**kwds)
        self.shape = shape
        self.data = gsl.vector_alloc(shape) if data is None else data
        return


    # container support
    def __len__(self): return self.shape


    def __iter__(self):
        # for each valid value of the index
        for index in range(self.shape):
            # produce the corresponding element
            yield gsl.vector_get(self.data, index)
        # no more
        return


    def __contains__(self, value):
        # faster than checking every element in python
        return gsl.vector_contains(self.data, value)


    def __getitem__(self, index):
        # assuming {index} is convertible into an integer, attempt to
        try:
            # get and return the element
            return gsl.vector_get(self.data, int(index))
        # if this fails
        except TypeError:
            # check whether {index} is a slice
            if type(index) is not slice:
                # if not, we are out of ideas
                raise TypeError(
                    'vector indices must be integers, not {.__name__}'.format(type(index)))
        # we have a slice, so return an appropriate value generator
        return self._slice(index)


    def __setitem__(self, index, value):
        # assuming {index} is convertible into an integer, attempt to
        try:
            # set the corresponding element to the provided value
            return gsl.vector_set(self.data, int(index), value)
        # if this fails
        except TypeError:
            # check whether {index} is a slice
            if type(index) is not slice:
                # if not, we are out of ideas
                raise TypeError(
                    'vector indices must be integers, not {.__name__}'.format(type(index)))
        # we have a slice; assume {value} is a compatible iterable
        try:
            # iterate over the slice and the values
            for i,v in zip(range(*index.indices(self.shape)), value):    
                # and set the corresponding vector element
                gsl.vector_set(self.data, i, v)
        except TypeError:
            raise TypeError('can only assign an iterable')

        # all done
        return


    # comparisons
    def __eq__(self, other):
        # type check
        if type(self) is not type(other): return NotImplemented
        # hand the request off to the extension module
        return gsl.vector_equal(self.data, other.data)


    def __ne__(self, other):
        return not (self == other)


    # in-place arithmetic
    def __iadd__(self, other):
        """
        In-place addition with the elements of {other}
        """
        # if other is a vector
        if type(other) is type(self):
            # do vector-vector addition
            gsl.vector_add(self.data, other.data)
            # and return
            return self
        # if other is a number
        if isinstance(other, numbers.Number):
            # do constant addition
            gsl.vector_shift(self.data, float(other))
            # and return
            return self
        # otherwise, let the interpreter know
        raise NotImplemented


    def __isub__(self, other):
        """
        In-place subtraction with the elements of {other}
        """
        # if other is a vector
        if type(other) is type(self):
            # do vector-vector subtraction
            gsl.vector_sub(self.data, other.data)
            # and return
            return self
        # if other is a number
        if isinstance(other, numbers.Number):
            # do constant subtraction
            gsl.vector_shift(self.data, -float(other))
            # and return
            return self
        # otherwise, let the interpreter know
        raise NotImplemented


    def __imul__(self, other):
        """
        In-place multiplication with the elements of {other}
        """
        # if other is a vector
        if type(other) is type(self):
            # do vector-vector multiplication
            gsl.vector_mul(self.data, other.data)
            # and return
            return self
        # if other is a number
        if isinstance(other, numbers.Number):
            # do scaling by constant
            gsl.vector_scale(self.data, float(other))
            # and return
            return self
        # otherwise, let the interpreter know
        raise NotImplemented


    def __itruediv__(self, other):
        """
        In-place addition with the elements of {other}
        """
        # if other is a vector
        if type(other) is type(self):
            # do vector-vector division
            gsl.vector_div(self.data, other.data)
            # and return
            return self
        # if other is a number
        if isinstance(other, numbers.Number):
            # do scaling by constant
            gsl.vector_scale(self.data, 1/float(other))
            # and return
            return self
        # otherwise, let the interpreter know
        raise NotImplemented


    # implementation details
    def _slice(self, index):
        """
        Build a generator that yields the values described in the {index}
        """
        # iterate over the indices
        for i in range(*index.indices(self.shape)):
            # yield the corresponding value
            yield gsl.vector_get(self.data, i)
        # all done
        return


    # private data
    data = None


# end of file 
