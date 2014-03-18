/**
 * @file KeywordTypes.h
 *
 * Created on: Oct 14, 2013
 *     Author: Pavel Binko
 */

#ifndef KEYWORDTYPES_H_
#define KEYWORDTYPES_H_


//#include <boost/mpl/for_each.hpp>
//#include <boost/mpl/iterator_range.hpp>
//#include <boost/mpl/range_c.hpp>

#include <iostream>

#include "ElementsKernel/ElementsException.h"


namespace ChDataModel {
namespace Fits {

//-----------------------------------------------------------------------------

/**
 * Keyword types, used in the FITS keywords
 */
enum class KeywordTypes {
  None,
  Bool,
  Double,
  Long,
  String,
  Last,
  First=Bool
};

//-----------------------------------------------------------------------------

inline KeywordTypes operator++( KeywordTypes& x ) { return x = (KeywordTypes)(((int)(x) + 1)); }
//inline KeywordTypes operator++(KeywordTypes& x) { return x = (KeywordTypes)(std::underlying_type<KeywordTypes>::type(x) + 1); }
inline KeywordTypes operator*(KeywordTypes c) {return c;}
inline KeywordTypes begin(KeywordTypes /* r */) {return KeywordTypes::First;}
inline KeywordTypes end(KeywordTypes /* r */)   {return KeywordTypes::Last;}


inline std::ostream& operator << ( std::ostream& stream, const KeywordTypes & keywordType ) {
  switch (keywordType) {
    case KeywordTypes::None:      stream << "None";               break;
    case KeywordTypes::Bool:      stream << "Bool";               break;
    case KeywordTypes::Double:    stream << "Double";             break;
    case KeywordTypes::Long:      stream << "Long";               break;
    case KeywordTypes::String:    stream << "String";             break;
    case KeywordTypes::Last:      stream << "Last is undefined."; break;
  };
  return stream;
}

inline std::string keywordTypes2string( const KeywordTypes & keywordType )   {
  std::string s;
  switch (keywordType) {
    case KeywordTypes::None:      s = "None";                     break;
    case KeywordTypes::Bool:      s = "Bool";                     break;
    case KeywordTypes::Double:    s = "Double";                   break;
    case KeywordTypes::Long:      s = "Long";                     break;
    case KeywordTypes::String:    s = "String";                   break;
    case KeywordTypes::Last:      s = "Last is undefined.";       break;
  };
  return s;
}

inline KeywordTypes string2keywordTypes( const std::string & s )   {
  KeywordTypes keywordType;
  if     ( "None"   == s )        keywordType = KeywordTypes::None;
  else if( "Bool"   == s )        keywordType = KeywordTypes::Bool;
  else if( "Double" == s )        keywordType = KeywordTypes::Double;
  else if( "Long"   == s )        keywordType = KeywordTypes::Long;
  else if( "String" == s )        keywordType = KeywordTypes::String;
  else throw ElementsException("DataModel::Fits::KeywordTypes : Unknown keyword type : " + s);

  return keywordType;
}

//-----------------------------------------------------------------------------

} /* namespace Fits */
} /* namespace ChDataModel */

#endif /* KEYWORDTYPES_H_ */
