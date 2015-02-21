# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# orthologue
# (c) 1998-2015 all rights reserved
#


# externals
import pyre
import webbrowser
# my superclass
from .Executive import Executive


# declaration
class Web(Executive, family='pyre.shells.web'):
    """
    A shell enables application interactivity over the web
    """


    # interface
    @pyre.export
    def launch(self, application, *args, **kwds):
        """
        Invoke the {application} behavior
        """
        # create a nexus
        nexus = pyre.nexus.node()
        # attach it to the application
        application.nexus = nexus
        # register it with the nexus
        nexus.services['web'] = 'http'
        # activate
        nexus.activate(application=application)

        # get the address of the web server
        address = nexus.services['web'].address
        # form a url
        url = 'http://localhost:{.port}/'.format(address)
        # launch the browser
        webbrowser.open(url)
        # get the nexus to do its thing
        nexus.serve()
        # and when the user is done interacting, launch the application
        status = application.main(*args, **kwds)
        # and exit
        return status


# end of file
