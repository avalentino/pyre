// -*- coding: utf-8 -*-
//
// michael a.g. aïvázis
// california institute of technology
// (c) 1998-2011 all rights reserved
//


// for the build system
#include <portinfo>

// packages
#include <assert.h>
// access to the packages used by Index
#include <map>
#include <string>
#include <cstdlib>

// access to the low level header files
#include <pyre/journal/State.h>
#include <pyre/journal/Index.h>

// convenience
typedef pyre::journal::Index< pyre::journal::State<true> > critical_t;
typedef pyre::journal::Index< pyre::journal::State<false> > boring_t;

// main program
int main() {

    // instantiate an index of state objects that are on by default
    critical_t critical;
    // request a key that is not there
    critical_t::value_t & on = critical.lookup("critical", "test");
    // verify that this is on by default
    assert(on.state() == true);
    // turn it off
    on.deactivate();
    // ask for it again, this time read only
    critical_t::value_t on_after = critical.lookup("critical", "test");
    // verify that it is now off
    assert(on_after.state() == false);

    // instantiate an index of state objects that are off by default
    boring_t boring;
    // request a key that is not there
    boring_t::value_t & off = boring.lookup("boring", "test");
    // verify that this is off by default
    assert(off.state() == false);
    // turn it on
    off.activate();
    // ask for it again, this time read only
    boring_t::value_t off_after = boring.lookup("boring", "test");
    // verify that it is now on
    assert(off_after.state() == true);

    // all done
    return 0;
}

// end of file
