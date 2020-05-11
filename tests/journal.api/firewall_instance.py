#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis <michael.aivazis@para-sim.com>
# (c) 1998-2020 all rights reserved


def test():
    """
    Verify the channel initial state
    """
    # access
    import journal

    # make a channel
    channel = journal.firewall(name="tests.journal.firewall")
    # verify the channel name
    assert channel.name == "tests.journal.firewall"
    # the verbosity should be at the default level
    assert channel.verbosity == 1
    # the channel should be active
    assert channel.active == True
    # and fatal
    assert channel.fatal == True

    # the page should be empty
    assert tuple(channel.page) == ()
    # verify the metadata
    assert channel.notes["application"] == "journal"
    assert channel.notes["channel"] == channel.name
    assert channel.notes["severity"] == channel.severity

    # all done
    return


# main
if __name__ == "__main__":
    # run the test
    test()


# end of file
