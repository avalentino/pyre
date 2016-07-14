// -*- C++ -*-
// -*- coding: utf-8 -*-
//
// michael a.g. aïvázis
// orthologue
// (c) 1998-2016 all rights reserved
//

// code guard
#if !defined(pyre_grid_Layout_h)
#define pyre_grid_Layout_h


// declaration
template <typename repT>
class pyre::grid::Layout {
    // types
public:
    // the container with the index order
    typedef repT rep_type;
    // for sizing things
    typedef typename rep_type::size_type size_type;
    // the base type of my values
    typedef typename rep_type::value_type value_type;

    // meta-methods
public:
    // the constructor is a variadic template; it enables construction of the rep using
    // initializer lists
    template <typename... argT> inline Layout(argT... arg);

    // interface
public:
    // size
    inline constexpr auto size() const;

    // indexed access
    inline auto operator[](size_type item) const;

    // support for ranged for loops
    inline auto begin() const;
    inline auto end() const;

    // implementation details
private:
    const rep_type _layout;
};


#endif

// end of file
