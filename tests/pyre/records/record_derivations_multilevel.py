#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# michael a.g. aïvázis
# california institute of technology
# (c) 1998-2011 all rights reserved
#


"""
Create a record that has a derived field
"""


import pyre.records


class item(pyre.records.record):
    """
    A sample record
    """
    production = pyre.records.field()
    production.type = pyre.schema.float

    shipping = pyre.records.field()
    shipping.type = pyre.schema.float

    cost = production + shipping
    price = 2 * cost


def test():
    # explore the record class
    assert isinstance(item.production, pyre.records.field)
    assert isinstance(item.shipping, pyre.records.field)
    assert isinstance(item.cost, pyre.records.derivation)
    assert isinstance(item.price, pyre.records.derivation)

    assert item.pyre_items == (item.production, item.shipping, item.cost, item.price)
    assert item.pyre_fields == (item.production, item.shipping)
    assert item.pyre_derivations == (item.cost, item.price)

    assert item.pyre_index[item.production] == 0
    assert item.pyre_index[item.shipping] == 1
    assert item.pyre_index[item.cost] == 2
    assert item.pyre_index[item.price] == 3

    # now instantiate one
    sample = item(production=0.8, shipping=0.2)
    # check
    assert sample.production == 0.8
    assert sample.shipping == 0.2
    assert sample.cost == 1.0
    assert sample.price == 2.0
    
    return sample


# main
if __name__ == "__main__":
    test()


# end of file 
