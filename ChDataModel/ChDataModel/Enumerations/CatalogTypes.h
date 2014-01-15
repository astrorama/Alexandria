/**
 * @file CatalogTypes.h
 *
 * Created on: May 23, 2013
 *     Author: Pavel Binko
 */

#ifndef CATALOGTYPES_H_
#define CATALOGTYPES_H_


#include <boost/mpl/for_each.hpp>
#include <boost/mpl/iterator_range.hpp>
#include <boost/mpl/range_c.hpp>

#include <iostream>

#include "ElementsKernel/ElementsException.h"


/**
 * EnumIterator allows to use this general syntax of a loop, e.g. :
 *
 *   for( const auto& e : getRange<COLOR>() )
 *
 * The condition is, that enum classes must define the First and Last element
 * like the standard values in Boost, e.g. :
 *
 *   enum class COLOR {
 *     Blue, Red, Green, Purple,
 *     Last,        // Last actually comes after the last element
 *     First=Blue   // First points to the first element
 *   };
 */


namespace ChDataModel {

//-----------------------------------------------------------------------------

/**
 *
 */
enum class CatalogTypes {
  ALL_SOURCES,
  STAR,
  GALAXY,
  Last,
  First=ALL_SOURCES
};

//-----------------------------------------------------------------------------

inline CatalogTypes operator++( CatalogTypes& x ) { return x = (CatalogTypes)(((int)(x) + 1)); }
//inline CatalogTypes operator++(CatalogTypes& x) { return x = (CatalogTypes)(std::underlying_type<CatalogTypes>::type(x) + 1); }
inline CatalogTypes operator*(CatalogTypes c) {return c;}
inline CatalogTypes begin(CatalogTypes /* r */) {return CatalogTypes::First;}
inline CatalogTypes end(CatalogTypes /* r */)   {return CatalogTypes::Last;}

//-----------------------------------------------------------------------------

inline std::ostream& operator << ( std::ostream& stream, const CatalogTypes & surveyName ) {
  switch (surveyName) {
    case CatalogTypes::ALL_SOURCES:      stream << "ALL_SOURCES";           break;
    case CatalogTypes::STAR:             stream << "STAR";                  break;
    case CatalogTypes::GALAXY:           stream << "GALAXY";                break;
    case CatalogTypes::Last:             stream << "Last is undefined.";    break;
  };
  return stream;
}

//-----------------------------------------------------------------------------

inline std::string catalogTypes2string( const CatalogTypes & surveyName )   {
  std::string s;
  switch (surveyName) {
    case CatalogTypes::ALL_SOURCES:      s = "ALL_SOURCES";                 break;
    case CatalogTypes::STAR:             s = "STAR";                        break;
    case CatalogTypes::GALAXY:           s = "GALAXY";                      break;
    case CatalogTypes::Last:             s = "Last is undefined.";          break;
  };
  return s;
}

//-----------------------------------------------------------------------------

inline CatalogTypes string2catalogTypes( const std::string & s )   {
  CatalogTypes catalogType;
  if     ( "ALL_SOURCES" == s )          catalogType = CatalogTypes::ALL_SOURCES;
  else if( "STAR"        == s )          catalogType = CatalogTypes::STAR;
  else if( "GALAXY"      == s )          catalogType = CatalogTypes::GALAXY;
  else throw ElementsException("DataModel::DataModel : Unknown survey name : " + s );

  return catalogType;
}

//-----------------------------------------------------------------------------

} /* namespace ChDataModel */
#endif /* CATALOGTYPES_H_ */
