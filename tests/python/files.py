#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2013 all rights reserved
#


"""
Check whether file iterators are synchronized with independent accesses to the file object
"""


def test():
    single = 0
    with open('files.py') as f:
        for line in f:
            single += 1

    double = 0
    with open('files.py') as f:
        for line in f:
            double += 1
            extra = f.readline()
            double += 1

    assert single == double

    return


# main
if __name__ == "__main__":
    test()


# end of file 
