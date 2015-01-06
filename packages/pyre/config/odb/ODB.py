# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# orthologue
# (c) 1998-2015 all rights reserved
#


# access to the locator factories
from ... import tracking
# and my ancestors
from ..Loader import Loader


class ODB(Loader):
    """
    This component codec recognizes uris of the form

        vfs:/path/module.py/factory#name
        file:/path/module.py/factory#name

    which is interpreted as a request to import the file {module.py} from the indicated path,
    look for the symbol {factory}, and optionally instantiate whatever component class is
    recovered using {name}
    """


    # type
    from .Shelf import Shelf as shelf


    # constants
    separator = '/'
    schemes = ('vfs', 'file')


    # interface
    @classmethod
    def load(cls, executive, uri, **kwds):
        """
        Interpret {uri} as a shelf to be loaded
        """
        # get the fileserver
        fs = executive.fileserver
        # ask it to
        try:
            # print("ODB.load: uri={.uri!r}".format(uri))
            # open the {uri}
            stream = fs.open(uri=uri)
        # if anything goes wrong
        except fs.GenericError as error:
            # report it as a loading error
            raise cls.LoadingError(codec=cls, uri=uri) from error
        # build a new shelf
        shelf = cls.shelf(stream=stream, uri=uri, locator=tracking.file(source=str(uri)))
        # and return it
        return shelf


    @classmethod
    def register(cls, index):
        """
        Register my schemes with the {index}
        """
        # update the index with my schemes
        index.update((scheme, cls) for scheme in cls.schemes)
        # all done
        return


    @classmethod
    def locateShelves(cls, protocol, uri, symbol, **kwds):
        """
        Locate candidate shelves from the given {uri}
        """
        # if the {uri} has an {address}
        if uri.address:
            # try it first
            # print("ODB.locateShelves: uri={.uri!r}".format(uri))
            yield uri
            # try adding a '.py' to it
            extended = uri.clone()
            extended.address += '.py'
            yield extended

        # if the uri scheme was 'file'
        if uri.scheme == 'file':
            # there is nothing else to try
            return

        # otherwise, if there is a valid {protocol}
        if protocol:
            # get it to provide some candidates from the virtual filesystem
            yield from protocol.pyre_formCandidates(uri=uri, symbol=symbol, **kwds)

        # no more ideas
        return


# end of file
