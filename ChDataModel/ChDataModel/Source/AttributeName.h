/**
 * @file AttributeName.h
 *
 * Created on: Jan 16, 2014
 *     Author: Pierre Dubath
 */
#ifndef ATTRIBUTENAME_H_
#define ATTRIBUTENAME_H_


#include <boost/mpl/for_each.hpp>
#include <boost/mpl/iterator_range.hpp>
#include <boost/mpl/range_c.hpp>

#include <iostream>

#include "ElementsKernel/ElementsException.h"


namespace ChDataModel {

//-----------------------------------------------------------------------------

/**
 *  Name of all possible source attributes
 */
enum class AttributeName {
  None,
  COORDINATES,
  PHOTOMETRY_MAP,
  SPECTROSCOPIC_REDSHIFT,
  AGN_FLAG,
  Last,
  First=COORDINATES
};


//-----------------------------------------------------------------------------

inline AttributeName operator++( AttributeName& x ) { return x = (AttributeName)(((int)(x) + 1)); }
//inline attributeNames operator++(attributeNames& x) { return x = (attributeNames)(std::underlying_type<attributeNames>::type(x) + 1); }
inline AttributeName operator*(AttributeName c) {return c;}
inline AttributeName begin(AttributeName /* r */) {return AttributeName::First;}
inline AttributeName end(AttributeName /* r */)   {return AttributeName::Last;}

//-----------------------------------------------------------------------------

inline std::ostream& operator << ( std::ostream& stream, const AttributeName & attributeName ) {
  switch (attributeName) {
    case AttributeName::None:          stream << "None";                  break;
    case AttributeName::COORDINATES:   stream << "COORDINATES";                  break;
    case AttributeName::PHOTOMETRY_MAP:    stream << "PHOTOMETRY_MAP";          break;
    case AttributeName::SPECTROSCOPIC_REDSHIFT:  stream << "SPECTROSCOPIC_REDSHIFT";        break;
    case AttributeName::AGN_FLAG:      stream << "AGN_FLAG";        break;
    case AttributeName::Last:            stream << "Last is undefined.";    break;
  };
  return stream;
}

//-----------------------------------------------------------------------------

inline std::string attributeName2string( const AttributeName & attributeName )   {
  std::string s;
  switch (attributeName) {
    case AttributeName::None:            s = "None";                        break;
    case AttributeName::COORDINATES:     s = "COORDINATES";                        break;
    case AttributeName::PHOTOMETRY_MAP:      s = "PHOTOMETRY_MAP";                break;
    case AttributeName::SPECTROSCOPIC_REDSHIFT:  s = "SPECTROSCOPIC_REDSHIFT";              break;
    case AttributeName::AGN_FLAG:        s = "AGN_FLAG";              break;
    case AttributeName::Last:            s = "Last is undefined.";          break;
  };
  return s;
}

//-----------------------------------------------------------------------------

inline AttributeName string2attributeName( const std::string & s )   {
  AttributeName attributeName;
  if     ( "None"         == s )         attributeName = AttributeName::None;
  else if( "COORDINATES"  == s )         attributeName = AttributeName::COORDINATES;
  else if( "PHOTOMETRY_MAP"   == s )         attributeName = AttributeName::PHOTOMETRY_MAP;
  else if( "SPECTROSCOPIC_REDSHIFT" == s )         attributeName = AttributeName::SPECTROSCOPIC_REDSHIFT;
  else if( "AGN_FLAG"     == s )         attributeName = AttributeName::AGN_FLAG;
  else throw ElementsException("DataModel::DataModel : Unknown attribute name : " + s );

  return attributeName;
}

//-----------------------------------------------------------------------------

} /* namespace ChDataModel */
#endif /* ATTRIBUTENAME_H_ */
