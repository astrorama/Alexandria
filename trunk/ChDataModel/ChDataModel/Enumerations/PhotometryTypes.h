/**
 * @file PhotometryTypes.h
 *
 * Created on: May 23, 2013
 *     Author: Pavel Binko
 */

#ifndef PHOTOMETRYTYPES_H_
#define PHOTOMETRYTYPES_H_


#include <boost/mpl/for_each.hpp>
#include <boost/mpl/iterator_range.hpp>
#include <boost/mpl/range_c.hpp>

#include <iostream>

#include "ElementsKernel/ElementsException.h"


namespace ChDataModel {

//-----------------------------------------------------------------------------

/**
 *  The type of photometric measurement stored in the Photometry objects
 */
enum class PhotometryTypes {
  None,
  FLUX,
  AB_MAGNITUDE,
  VEGA_MAGNITUDE,
  Last,
  First=FLUX
};


//-----------------------------------------------------------------------------

inline PhotometryTypes operator++( PhotometryTypes& x ) { return x = (PhotometryTypes)(((int)(x) + 1)); }
//inline PhotometryTypes operator++(PhotometryTypes& x) { return x = (PhotometryTypes)(std::underlying_type<PhotometryTypes>::type(x) + 1); }
inline PhotometryTypes operator*(PhotometryTypes c) {return c;}
inline PhotometryTypes begin(PhotometryTypes /* r */) {return PhotometryTypes::First;}
inline PhotometryTypes end(PhotometryTypes /* r */)   {return PhotometryTypes::Last;}

//-----------------------------------------------------------------------------

inline std::ostream& operator << ( std::ostream& stream, const PhotometryTypes & photometryType ) {
  switch (photometryType) {
    case PhotometryTypes::None:            stream << "None";                  break;
    case PhotometryTypes::FLUX:            stream << "FLUX";                  break;
    case PhotometryTypes::AB_MAGNITUDE:    stream << "AB_MAGNITUDE";          break;
    case PhotometryTypes::VEGA_MAGNITUDE:  stream << "VEGA_MAGNITUDE";        break;
    case PhotometryTypes::Last:            stream << "Last is undefined.";    break;
  };
  return stream;
}

//-----------------------------------------------------------------------------

inline std::string photometryTypes2string( const PhotometryTypes & photometryType )   {
  std::string s;
  switch (photometryType) {
    case PhotometryTypes::None:            s = "None";                        break;
    case PhotometryTypes::FLUX:            s = "FLUX";                        break;
    case PhotometryTypes::AB_MAGNITUDE:    s = "AB_MAGNITUDE";                break;
    case PhotometryTypes::VEGA_MAGNITUDE:  s = "VEGA_MAGNITUDE";              break;
    case PhotometryTypes::Last:            s = "Last is undefined.";          break;
  };
  return s;
}

//-----------------------------------------------------------------------------

inline PhotometryTypes string2photometryTypes( const std::string & s )   {
  PhotometryTypes photometryType;
  if     ( "None"           == s )         photometryType = PhotometryTypes::None;
  else if( "FLUX"           == s )         photometryType = PhotometryTypes::FLUX;
  else if( "AB_MAGNITUDE"   == s )         photometryType = PhotometryTypes::AB_MAGNITUDE;
  else if( "VEGA_MAGNITUDE" == s )         photometryType = PhotometryTypes::VEGA_MAGNITUDE;
  else throw ElementsException("DataModel::DataModel : Unknown photometry type : " + s );

  return photometryType;
}

//-----------------------------------------------------------------------------

} /* namespace ChDataModel */
#endif /* PHOTOMETRYTYPES_H_ */
