# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2012 all rights reserved
#


# superclasses
from .Descriptor import Descriptor
from ..components.Executive import Executive


# class declaration
class Trait(Descriptor, Executive):
    """
    This is the base class for component features that form their public interface

    Traits extend the notion of a class attribute to an object that is capabable of
    capturing information about the attribute that has no natural resting place as part of a
    normal class declaration.

    Traits enable end-user configurable state, for both simple attributes and references to
    more elaborate objects, such as other components. Individual inventory items need a name
    that enables access to the associated information, per-instance actual storage for the
    attribute value, and additional meta data, such as reasonable default values when the
    attribute is not explictly given a value during configuration, and the set of constraints
    it should satisfy before it is considered a legal value.
    """


    # framework data
    # predicate that indicates whether this trait is subject to runtime configuration
    isConfigurable = False


# end of file 
