#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2013 all rights reserved
#


"""
Verify that facilities get bound correctly when specified implicitly
"""


def test():
    import pyre

    # the job name converter
    def converter(name): return "relax"

    # declare a protocol
    class task(pyre.protocol):
        """a protocol"""
        @pyre.provides
        def do(self):
            """do something"""

    # declare a component
    class worker(pyre.component):
        """a component"""
        job = task(default="import:sample.whatever")
        job.converters = [ converter ]

    # check that task was bound according to our expectations from sample.py
    assert issubclass(worker.job, pyre.component)
    assert worker.job.__name__ == "relax"
    assert task.pyre_isCompatible(worker.job)

    return worker, task


# main
if __name__ == "__main__":
    test()


# end of file 
