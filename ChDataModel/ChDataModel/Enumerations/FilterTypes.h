/**
 * @file FilterTypes.h
 *
 * Created on: May 23, 2013
 *     Author: Pavel Binko
 */

#ifndef FILTERTYPES_H_
#define FILTERTYPES_H_


#include <boost/mpl/for_each.hpp>
#include <boost/mpl/iterator_range.hpp>
#include <boost/mpl/range_c.hpp>

#include <iostream>

#include "ElementsKernel/ElementsException.h"


namespace ChDataModel {

//-----------------------------------------------------------------------------

/**
 * FilterTypes are :
 * - EUCLID - "sum" of the efficiencies of OPTICS, FILTER, CCD (total filter efficiency)
 * - OPTICS - efficiency of the optics (telescope)
 * - FILTER - efficiency of the filter (filter curve)
 * - CCD    - efficiency of the CCD
 */
enum class FilterTypes {
  None,          // None stands for something like NaN (not a number)
  EUCLID,        // Valid values
  OPTICS,
  FILTER,
  CCD,
  Last,          // Last actually comes after the last element
  First=EUCLID   // First points to the first valid element
};


//-----------------------------------------------------------------------------
// The following 4 definitions are needed for the loops, e.g. :
//   - for( const auto& e : FilterTypes() )
//   - for( FilterTypes e=FilterTypes::First; e!=FilterTypes::Last; ++e )

inline FilterTypes operator++( FilterTypes& x ) { return x = (FilterTypes)(((int)(x) + 1)); }
//inline FilterTypes operator++(FilterTypes& x) { return x = (FilterTypes)(std::underlying_type<FilterTypes>::type(x) + 1); }
inline FilterTypes operator*(FilterTypes c) {return c;}
inline FilterTypes begin(FilterTypes /* r */ ) {return FilterTypes::First;}
inline FilterTypes end(FilterTypes /* r */ )   {return FilterTypes::Last;}


inline std::ostream& operator << ( std::ostream& stream, const FilterTypes & filterType ) {
  switch (filterType) {
    case FilterTypes::None:          stream << "None";               break;
    case FilterTypes::EUCLID:        stream << "EUCLID";             break;
    case FilterTypes::OPTICS:        stream << "OPTICS";             break;
    case FilterTypes::FILTER:        stream << "FILTER";             break;
    case FilterTypes::CCD:           stream << "CCD";                break;
    case FilterTypes::Last:          stream << "Last is undefined."; break;
  };
  return stream;
}

inline std::string filterTypes2string( const FilterTypes & filterType )   {
  std::string s;
  switch (filterType) {
    case FilterTypes::None:          s = "None";                     break;
    case FilterTypes::EUCLID:        s = "EUCLID";                   break;
    case FilterTypes::OPTICS:        s = "OPTICS";                   break;
    case FilterTypes::FILTER:        s = "FILTER";                   break;
    case FilterTypes::CCD:           s = "CCD";                      break;
    case FilterTypes::Last:          s = "Last is undefined.";       break;
  };
  return s;
}

inline FilterTypes string2filterTypes( const std::string & s )   {
  FilterTypes filterType;
  if     ( "None"       == s )           filterType = FilterTypes::None;
  else if( "EUCLID"     == s )           filterType = FilterTypes::EUCLID;
  else if( "OPTICS"     == s )           filterType = FilterTypes::OPTICS;
  else if( "FILTER"     == s )           filterType = FilterTypes::FILTER;
  else if( "CCD"        == s )           filterType = FilterTypes::CCD;
  else throw ElementsException("DataModel::DataModel : Unknown filter type : " + s );

  return filterType;
}

//-----------------------------------------------------------------------------

} /* namespace ChDataModel */
#endif /* FILTERTYPES_H_ */
