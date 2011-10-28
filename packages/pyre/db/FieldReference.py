# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2011 all rights reserved
#


from .Entry import Entry


class FieldReference(Entry):
    """
    A field decorator that encapsulates references to table fields

    This class is endowed with the full algebra from {pyre.algebraic} in order to support
    expressions involving table fields. Such expressions can be used to formulate constraints
    or to specify fields in views
    """


    # public data
    table = None # the table class
    field = None # the field descriptor


    # interface
    def project(self, table):
        """
        Build a reference to {table} that points to the same field as i do
        """
        return FieldReference(table=table, field=self.field)


    # meta methods
    def __init__(self, table, field, **kwds):
        super().__init__(**kwds)

        self.table = table
        self.field = field

        return


    def __str__(self):
        """
        Convert the field reference to an expression
        """
        # if i am bound to a specific field
        if self.field is not None:
            # include its name in the generated expression
            return "{0.table.pyre_name}.{0.field.name}".format(self)
        # otherwise, just refer to the table
        return "{0.table.pyre_name}".format(self)


# end of file 
