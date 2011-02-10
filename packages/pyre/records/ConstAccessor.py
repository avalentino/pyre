# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2011 all rights reserved
#


class ConstAccessor:
    """
    Descriptor that provides access to a record item
    """


    # public data
    index = None # the index of my value in the data tuple
    field = None # the field with the meta data


    # meta methods
    def __init__(self, index, field, **kwds):
        super().__init__(**kwds)
        self.index = index
        self.field = field
        return


    # descriptor interface
    def __get__(self, record, cls):
        """
        Retrieve the value of my field from {record}
        """
        try:
            return record[self.index]
        except TypeError:
            return self.field


# end of file 
