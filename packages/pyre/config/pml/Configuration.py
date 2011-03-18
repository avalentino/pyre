# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2011 all rights reserved
#


from .Node import Node
from ..Configuration import Configuration as Buffer


class Configuration(Node):
    """
    Handler for the top level tag in pml documents
    """

    # constants
    elements = ("component", "inventory", "bind")


    # interface
    def notify(self, parent, locator):
        """
        Let {parent} now that processing this configuration tag is complete
        """
        return parent.onConfiguration(self)


    # assignment handler
    def createAssignment(self, key, value, locator):
        """
        Process a binding of a property to a value
        """
        # create a new assignment event
        self.configuration.newAssignment(key=key, value=value, locator=locator)
        # nothing else, for now
        return


    def createConditionalAssignment(self, component, family, key, value, locator):
        """
        Process a binding of a property to a value
        """
        # create a new conditional assignment event
        self.configuration.newConditionalAssignment(
            component=component, family=family, key=key, value=value, locator=locator)
        # nothing else, for now
        return


    # meta methods
    def __init__(self, parent, attributes, locator, **kwds):
        super().__init__(**kwds)
        self.configuration = Buffer()
        return
    

# end of file
