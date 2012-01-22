# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis, leif strand
# california institute of technology
# (c) 1998-2012 all rights reserved
#


# externals
import socket
# my interface
from .Socket import Socket


# declaration
class SocketTCP(Socket):
    """
    A channel that uses TCP sockets as the communication mechanism
    """


    # types
    from ..schema.INet import INet as inet


    # life cycle management
    @classmethod
    def open(cls, existing=None, address=None, **kwds):
        """
        Create a socket channel
        """
        # if an already connected {socket} was given
        if existing is not None:
            # just wrap and return
            return cls(socket=existing, **kwds)

        # if {address} is a string
        if isinstance(address, str):
            # get the inet parser to convert it to an actual address
            address = cls.inet.parser.parse(address)
        # make a low level socket
        s = socket.socket(address.family)
        # connect
        s.connect(address.value)
        # wrap it up
        channel = cls(socket=s, **kwds)
        # attach the address
        channel.address = address
        # and return it
        return channel


    # input/output
    def read(self, count):
        """
        Read {count} bytes from my input channel
        """
        # read bytes
        bstr = self.socket.recv(count)
        # in as many attempts as it takes
        while len(bstr) < count: bstr += self.socket.recv(count-len(bstr))
        # and return them
        return bstr


    def write(self, bstr):
        """
        Write the bytes in {bstr} to my output channel
        """
        # make sure the entire byte string is delivered
        self.socket.sendall(bstr)
        # and return the number of bytes sent
        return len(bstr)


# end of file 
