// -*- C++ -*-
//
// michael a.g. aïvázis
// orthologue
// (c) 1998-2017 all rights reserved
//

// exercise iterator construction
//   verify that all the parts are accessible through the public headers
//   verify constructor signatures

// portability
#include <portinfo>
// support
#include <pyre/grid.h>

// entry point
int main() {
    // fix the rep
    typedef std::array<int, 4> rep_t;
    // alias index and order
    typedef pyre::grid::index_t<rep_t> index_t;
    typedef pyre::grid::order_t<rep_t> order_t;
    typedef pyre::grid::slice_t<index_t, order_t> slice_t;
    // create a shortcut to my target iterator type
    typedef pyre::grid::iterator_t<slice_t> iterator_t;

    // make an ordering
    slice_t::order_type order {3, 2, 1, 0};
    // make a lower bound
    slice_t::index_type low {0, 0, 0, 0};
    // make an upper bound
    slice_t::index_type high {2, 3, 4, 5};
    // and some initial value for the iterator
    slice_t::index_type current {1, 1, 1, 1};
    // make a slice
    slice_t slice {low, high, order};

    // make an iterator with the default initial value
    iterator_t i1 {slice};
    // make an iterator with an initial value
    iterator_t i2 {current, slice};

    // all done
    return 0;
}

// end of file
