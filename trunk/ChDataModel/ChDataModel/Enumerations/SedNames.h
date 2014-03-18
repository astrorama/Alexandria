/**
 * @file SedNames.h
 *
 * Created on: May 23, 2013
 *     Author: Pavel Binko
 */

#ifndef SEDNAMES_H_
#define SEDNAMES_H_


#include <boost/mpl/for_each.hpp>
#include <boost/mpl/iterator_range.hpp>
#include <boost/mpl/range_c.hpp>

#include <iostream>

#include "ElementsKernel/ElementsException.h"


namespace ChDataModel {

//-----------------------------------------------------------------------------

/**
 * SedNames gives the name of ...
 */
enum class SedNames {
  None,          // None stands for something like NaN (not a number)
  Ell1_A_0,      // Valid values
  Ell2_A_0,
  Ell3_A_0,
  Ell4_A_0,
  Ell5_A_0,
  Ell6_A_0,
  Ell7_A_0,
  S0_A_0,
  Sa_A_0,
  Sa_A_1,
  Sb_A_0,
  Sb_A_1,
  Sc_A_0,
  Sc_A_1,
  Sc_A_2,
  Sd_A_0,
  Sd_A_1,
  Sd_A_2,
  Sdm_A_0,
  SB0_A_0,
  SB1_A_0,
  SB2_A_0,
  SB3_A_0,
  SB4_A_0,
  SB5_A_0,
  SB6_A_0,
  SB7_A_0,
  SB8_A_0,
  SB9_A_0,
  SB10_A_0,
  SB11_A_0,
  Last,          // Last actually comes after the last element
  First=Ell1_A_0 // First points to the first valid element
};


//-----------------------------------------------------------------------------
// The following 4 definitions are needed for the loops, e.g. :
//   - for( const auto& e : SedNames() )
//   - for( SedNames e=SedNames::First; e!=SedNames::Last; ++e )

inline SedNames operator++( SedNames& x ) { return x = (SedNames)(((int)(x) + 1)); }
//inline SedNames operator++(SedNames& x) { return x = (SedNames)(std::underlying_type<SedNames>::type(x) + 1); }
inline SedNames operator*(SedNames c) {return c;}
inline SedNames begin(SedNames /* r */ ) {return SedNames::First;}
inline SedNames end(SedNames /* r */ )   {return SedNames::Last;}


inline std::ostream& operator << ( std::ostream& stream, const SedNames & sedName ) {
  switch (sedName) {
    case SedNames::None:          stream << "None";               break;
    case SedNames::Ell1_A_0:      stream << "Ell1_A_0";           break;
    case SedNames::Ell2_A_0:      stream << "Ell2_A_0";           break;
    case SedNames::Ell3_A_0:      stream << "Ell3_A_0";           break;
    case SedNames::Ell4_A_0:      stream << "Ell4_A_0";           break;
    case SedNames::Ell5_A_0:      stream << "Ell5_A_0";           break;
    case SedNames::Ell6_A_0:      stream << "Ell6_A_0";           break;
    case SedNames::Ell7_A_0:      stream << "Ell7_A_0";           break;
    case SedNames::S0_A_0:        stream << "S0_A_0";             break;
    case SedNames::Sa_A_0:        stream << "Sa_A_0";             break;
    case SedNames::Sa_A_1:        stream << "Sa_A_1";             break;
    case SedNames::Sb_A_0:        stream << "Sb_A_0";             break;
    case SedNames::Sb_A_1:        stream << "Sb_A_1";             break;
    case SedNames::Sc_A_0:        stream << "Sc_A_0";             break;
    case SedNames::Sc_A_1:        stream << "Sc_A_1";             break;
    case SedNames::Sc_A_2:        stream << "Sc_A_2";             break;
    case SedNames::Sd_A_0:        stream << "Sd_A_0";             break;
    case SedNames::Sd_A_1:        stream << "Sd_A_1";             break;
    case SedNames::Sd_A_2:        stream << "Sd_A_2";             break;
    case SedNames::Sdm_A_0:       stream << "Sdm_A_0";            break;
    case SedNames::SB0_A_0:       stream << "SB0_A_0";            break;
    case SedNames::SB1_A_0:       stream << "SB1_A_0";            break;
    case SedNames::SB2_A_0:       stream << "SB2_A_0";            break;
    case SedNames::SB3_A_0:       stream << "SB3_A_0";            break;
    case SedNames::SB4_A_0:       stream << "SB4_A_0";            break;
    case SedNames::SB5_A_0:       stream << "SB5_A_0";            break;
    case SedNames::SB6_A_0:       stream << "SB6_A_0";            break;
    case SedNames::SB7_A_0:       stream << "SB7_A_0";            break;
    case SedNames::SB8_A_0:       stream << "SB8_A_0";            break;
    case SedNames::SB9_A_0:       stream << "SB9_A_0";            break;
    case SedNames::SB10_A_0:      stream << "SB10_A_0";           break;
    case SedNames::SB11_A_0:      stream << "SB11_A_0";           break;
    case SedNames::Last:          stream << "Last is undefined."; break;
  };
  return stream;
}

inline std::string sedNames2string( const SedNames & sedName )   {
  std::string s;
  switch (sedName) {
    case SedNames::None:          s = "None";                     break;
    case SedNames::Ell1_A_0:      s = "Ell1_A_0";                 break;
    case SedNames::Ell2_A_0:      s = "Ell2_A_0";                 break;
    case SedNames::Ell3_A_0:      s = "Ell3_A_0";                 break;
    case SedNames::Ell4_A_0:      s = "Ell4_A_0";                 break;
    case SedNames::Ell5_A_0:      s = "Ell5_A_0";                 break;
    case SedNames::Ell6_A_0:      s = "Ell6_A_0";                 break;
    case SedNames::Ell7_A_0:      s = "Ell7_A_0";                 break;
    case SedNames::S0_A_0:        s = "S0_A_0";                   break;
    case SedNames::Sa_A_0:        s = "Sa_A_0";                   break;
    case SedNames::Sa_A_1:        s = "Sa_A_1";                   break;
    case SedNames::Sb_A_0:        s = "Sb_A_0";                   break;
    case SedNames::Sb_A_1:        s = "Sb_A_1";                   break;
    case SedNames::Sc_A_0:        s = "Sc_A_0";                   break;
    case SedNames::Sc_A_1:        s = "Sc_A_1";                   break;
    case SedNames::Sc_A_2:        s = "Sc_A_2";                   break;
    case SedNames::Sd_A_0:        s = "Sd_A_0";                   break;
    case SedNames::Sd_A_1:        s = "Sd_A_1";                   break;
    case SedNames::Sd_A_2:        s = "Sd_A_2";                   break;
    case SedNames::Sdm_A_0:       s = "Sdm_A_0";                  break;
    case SedNames::SB0_A_0:       s = "SB0_A_0";                  break;
    case SedNames::SB1_A_0:       s = "SB1_A_0";                  break;
    case SedNames::SB2_A_0:       s = "SB2_A_0";                  break;
    case SedNames::SB3_A_0:       s = "SB3_A_0";                  break;
    case SedNames::SB4_A_0:       s = "SB4_A_0";                  break;
    case SedNames::SB5_A_0:       s = "SB5_A_0";                  break;
    case SedNames::SB6_A_0:       s = "SB6_A_0";                  break;
    case SedNames::SB7_A_0:       s = "SB7_A_0";                  break;
    case SedNames::SB8_A_0:       s = "SB8_A_0";                  break;
    case SedNames::SB9_A_0:       s = "SB9_A_0";                  break;
    case SedNames::SB10_A_0:      s = "SB10_A_0";                 break;
    case SedNames::SB11_A_0:      s = "SB11_A_0";                 break;
    case SedNames::Last:          s = "Last is undefined.";       break;
  };
  return s;
}

inline SedNames string2sedNames( const std::string & s )   {
  SedNames sedName;
  if     ( "None"           == s )   sedName = SedNames::None;
  else if( "Ell1_A_0"       == s )   sedName = SedNames::Ell1_A_0;
  else if( "Ell2_A_0"       == s )   sedName = SedNames::Ell2_A_0;
  else if( "Ell3_A_0"       == s )   sedName = SedNames::Ell3_A_0;
  else if( "Ell4_A_0"       == s )   sedName = SedNames::Ell4_A_0;
  else if( "Ell5_A_0"       == s )   sedName = SedNames::Ell5_A_0;
  else if( "Ell6_A_0"       == s )   sedName = SedNames::Ell6_A_0;
  else if( "Ell7_A_0"       == s )   sedName = SedNames::Ell7_A_0;
  else if( "S0_A_0"         == s )   sedName = SedNames::S0_A_0;
  else if( "Sa_A_0"         == s )   sedName = SedNames::Sa_A_0;
  else if( "Sa_A_1"         == s )   sedName = SedNames::Sa_A_1;
  else if( "Sb_A_0"         == s )   sedName = SedNames::Sb_A_0;
  else if( "Sb_A_1"         == s )   sedName = SedNames::Sb_A_1;
  else if( "Sc_A_0"         == s )   sedName = SedNames::Sc_A_0;
  else if( "Sc_A_1"         == s )   sedName = SedNames::Sc_A_1;
  else if( "Sc_A_2"         == s )   sedName = SedNames::Sc_A_2;
  else if( "Sd_A_0"         == s )   sedName = SedNames::Sd_A_0;
  else if( "Sd_A_1"         == s )   sedName = SedNames::Sd_A_1;
  else if( "Sd_A_2"         == s )   sedName = SedNames::Sd_A_2;
  else if( "Sdm_A_0"        == s )   sedName = SedNames::Sdm_A_0;
  else if( "SB0_A_0"        == s )   sedName = SedNames::SB0_A_0;
  else if( "SB1_A_0"        == s )   sedName = SedNames::SB1_A_0;
  else if( "SB2_A_0"        == s )   sedName = SedNames::SB2_A_0;
  else if( "SB3_A_0"        == s )   sedName = SedNames::SB3_A_0;
  else if( "SB4_A_0"        == s )   sedName = SedNames::SB4_A_0;
  else if( "SB5_A_0"        == s )   sedName = SedNames::SB5_A_0;
  else if( "SB6_A_0"        == s )   sedName = SedNames::SB6_A_0;
  else if( "SB7_A_0"        == s )   sedName = SedNames::SB7_A_0;
  else if( "SB8_A_0"        == s )   sedName = SedNames::SB8_A_0;
  else if( "SB9_A_0"        == s )   sedName = SedNames::SB9_A_0;
  else if( "SB10_A_0"       == s )   sedName = SedNames::SB10_A_0;
  else if( "SB11_A_0"       == s )   sedName = SedNames::SB11_A_0;
  else throw ElementsException("DataModel::DataModel : Unknown sed name : " + s );

  return sedName;
}

//-----------------------------------------------------------------------------

} /* namespace ChDataModel */

#endif /* SEDNAMES_H_ */
