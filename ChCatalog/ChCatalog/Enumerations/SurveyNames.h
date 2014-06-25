/**
 * @file ChCatalog/Enumerations/SurveyNames.h
 *
 * Created on: May 23, 2013
 *     Author: Pavel Binko
 */

#ifndef SURVEYNAMES_H_
#define SURVEYNAMES_H_


#include <boost/mpl/for_each.hpp>
#include <boost/mpl/iterator_range.hpp>
#include <boost/mpl/range_c.hpp>

#include <iostream>

#include "ElementsKernel/ElementsException.h"


namespace ChDataModel {

//-----------------------------------------------------------------------------

/**
 *
 */
enum class SurveyNames {
  None,
  EUCLID,
  COSMOS,
  VVDS,
  Last,
  First=COSMOS
};

//-----------------------------------------------------------------------------

inline SurveyNames operator++( SurveyNames& x ) { return x = (SurveyNames)(((int)(x) + 1)); }
//inline SurveyNames operator++(SurveyNames& x) { return x = (SurveyNames)(std::underlying_type<SurveyNames>::type(x) + 1); }
inline SurveyNames operator*(SurveyNames c) {return c;}
inline SurveyNames begin(SurveyNames /* r */) {return SurveyNames::First;}
inline SurveyNames end(SurveyNames /* r */)   {return SurveyNames::Last;}


inline std::ostream& operator << ( std::ostream& stream, const SurveyNames & surveyName ) {
  switch (surveyName) {
    case SurveyNames::None:      stream << "None";               break;
    case SurveyNames::EUCLID:    stream << "EUCLID";             break;
    case SurveyNames::COSMOS:    stream << "COSMOS";             break;
    case SurveyNames::VVDS:      stream << "VVDS";               break;
    case SurveyNames::Last:      stream << "Last is undefined."; break;
  };
  return stream;
}

inline std::string surveyNames2string( const SurveyNames & surveyName )   {
  std::string s;
  switch (surveyName) {
    case SurveyNames::None:      s = "None";                     break;
    case SurveyNames::EUCLID:    s = "EUCLID";                   break;
    case SurveyNames::COSMOS:    s = "COSMOS";                   break;
    case SurveyNames::VVDS:      s = "VVDS";                     break;
    case SurveyNames::Last:      s = "Last is undefined.";       break;
  };
  return s;
}

inline SurveyNames string2surveyNames( const std::string & s )   {
  SurveyNames surveyName;
  if     ( "None"   == s )       surveyName = SurveyNames::None;
  else if( "EUCLID" == s )       surveyName = SurveyNames::EUCLID;
  else if( "COSMOS" == s )       surveyName = SurveyNames::COSMOS;
  else if( "VVDS"   == s )       surveyName = SurveyNames::VVDS;
  else throw ElementsException("DataModel::DataModel : Unknown survey name : " + s);

  return surveyName;
}

//-----------------------------------------------------------------------------

} /* namespace ChDataModel */
#endif /* SURVEYNAMES_H_ */
