/**
 * @file FilterNames.h
 *
 * Created on: May 23, 2013
 *     Author: Pavel Binko
 */

#ifndef FILTERNAMES_H_
#define FILTERNAMES_H_


#include <boost/mpl/for_each.hpp>
#include <boost/mpl/iterator_range.hpp>
#include <boost/mpl/range_c.hpp>

#include <iostream>

#include "ElementsKernel/ElementsException.h"


namespace ChDataModel {

//-----------------------------------------------------------------------------

/**
 * FilterNames gives the name of photometric filters (or bands). The first part of the band gives an indication
 * of the central wave length of the filter. U, B, V mean ultraviolet, blue, visible respectively. This provides
 * however only a rough indication of the filter characteristic and the second part is necessary to identify
 * exactly a filter. For example, V_Subaru refer to the V filter used at the Subaru Japanese telescope in Hawai.
 */
enum class FilterNames {
  None,          // None stands for something like NaN (not a number)
  u_CFHT,        // Valid values
  B_Subaru,
  V_Subaru,
  g_Subaru,
  r_Subaru,
  i_Subaru,
  z_Subaru,
  Ks_KPNO_CTIO,
  i_CFHT,
  u_SDSS,
  g_SDSS,
  r_SDSS,
  i_SDSS,
  z_SDSS,
  F814W_HST,
  NB816_Subaru,
  IA427_Subaru,
  IA464_Subaru,
  IA505_Subaru,
  IA574_Subaru,
  IA709_Subaru,
  IA827_Subaru,
  NB711_Subaru,
  Ks_CFHT,
  J_UKIRT,
  IA484_Subaru,
  IA527_Subaru,
  IA624_Subaru,
  IA679_Subaru,
  IA738_Subaru,
  IA767_Subaru,
  FUV_GALEX,
  NUV_GALEX,
  Zext_ACSf850lp,
  Ynir_WFC3f105w,
  VIS_ACSf814w,
  Rext_ACSf606w,
  Jnir_WFC3f125w,
  Iext_ACSf775w,
  Hnir_WFC3f160w,
  Gext_ACSf435w,
  Last,          // Last actually comes after the last element
  First=u_CFHT   // First points to the first valid element
};


//-----------------------------------------------------------------------------
// The following 4 definitions are needed for the loops, e.g. :
//   - for( const auto& e : FilterNames() )
//   - for( FilterNames e=FilterNames::First; e!=FilterNames::Last; ++e )

inline FilterNames operator++( FilterNames& x ) { return x = (FilterNames)(((int)(x) + 1)); }
//inline FilterNames operator++(FilterNames& x) { return x = (FilterNames)(std::underlying_type<FilterNames>::type(x) + 1); }
inline FilterNames operator*(FilterNames c) {return c;}
inline FilterNames begin(FilterNames /* r */ ) {return FilterNames::First;}
inline FilterNames end(FilterNames /* r */ )   {return FilterNames::Last;}


inline std::ostream& operator << ( std::ostream& stream, const FilterNames & filterName ) {
  switch (filterName) {
    case FilterNames::None:          stream << "None";               break;
    case FilterNames::u_CFHT:        stream << "u_CFHT";             break;
    case FilterNames::B_Subaru:      stream << "B_Subaru";           break;
    case FilterNames::V_Subaru:      stream << "V_Subaru";           break;
    case FilterNames::g_Subaru:      stream << "g_Subaru";           break;
    case FilterNames::r_Subaru:      stream << "r_Subaru";           break;
    case FilterNames::i_Subaru:      stream << "i_Subaru";           break;
    case FilterNames::z_Subaru:      stream << "z_Subaru";           break;
    case FilterNames::Ks_KPNO_CTIO:  stream << "Ks_KPNO_CTIO";       break;
    case FilterNames::i_CFHT:        stream << "i_CFHT";             break;
    case FilterNames::u_SDSS:        stream << "u_SDSS";             break;
    case FilterNames::g_SDSS:        stream << "g_SDSS";             break;
    case FilterNames::r_SDSS:        stream << "r_SDSS";             break;
    case FilterNames::i_SDSS:        stream << "i_SDSS";             break;
    case FilterNames::z_SDSS:        stream << "z_SDSS";             break;
    case FilterNames::F814W_HST:     stream << "F814W_HST";          break;
    case FilterNames::NB816_Subaru:  stream << "NB816_Subaru";       break;
    case FilterNames::IA427_Subaru:  stream << "IA427_Subaru";       break;
    case FilterNames::IA464_Subaru:  stream << "IA464_Subaru";       break;
    case FilterNames::IA505_Subaru:  stream << "IA505_Subaru";       break;
    case FilterNames::IA574_Subaru:  stream << "IA574_Subaru";       break;
    case FilterNames::IA709_Subaru:  stream << "IA709_Subaru";       break;
    case FilterNames::IA827_Subaru:  stream << "IA827_Subaru";       break;
    case FilterNames::NB711_Subaru:  stream << "NB711_Subaru";       break;
    case FilterNames::Ks_CFHT:       stream << "Ks_CFHT";            break;
    case FilterNames::J_UKIRT:       stream << "J_UKIRT";            break;
    case FilterNames::IA484_Subaru:  stream << "IA484_Subaru";       break;
    case FilterNames::IA527_Subaru:  stream << "IA527_Subaru";       break;
    case FilterNames::IA624_Subaru:  stream << "IA624_Subaru";       break;
    case FilterNames::IA679_Subaru:  stream << "IA679_Subaru";       break;
    case FilterNames::IA738_Subaru:  stream << "IA738_Subaru";       break;
    case FilterNames::IA767_Subaru:  stream << "IA767_Subaru";       break;
    case FilterNames::FUV_GALEX:     stream << "FUV_GALEX";          break;
    case FilterNames::NUV_GALEX:     stream << "NUV_GALEX";          break;
    case FilterNames::Zext_ACSf850lp: stream << "Zext_ACSf850lp";    break;
    case FilterNames::Ynir_WFC3f105w: stream << "Ynir_WFC3f105w";    break;
    case FilterNames::VIS_ACSf814w:   stream << "VIS_ACSf814w";      break;
    case FilterNames::Rext_ACSf606w:  stream << "Rext_ACSf606w";     break;
    case FilterNames::Jnir_WFC3f125w: stream << "Jnir_WFC3f125w";    break;
    case FilterNames::Iext_ACSf775w:  stream << "Iext_ACSf775w";     break;
    case FilterNames::Hnir_WFC3f160w: stream << "Hnir_WFC3f160w";    break;
    case FilterNames::Gext_ACSf435w:  stream << "Gext_ACSf435w";     break;
    case FilterNames::Last:          stream << "Last is undefined."; break;
  };
  return stream;
}

inline std::string filterNames2string( const FilterNames & filterName )   {
  std::string s;
  switch (filterName) {
    case FilterNames::None:          s = "None";                     break;
    case FilterNames::u_CFHT:        s = "u_CFHT";                   break;
    case FilterNames::B_Subaru:      s = "B_Subaru";                 break;
    case FilterNames::V_Subaru:      s = "V_Subaru";                 break;
    case FilterNames::g_Subaru:      s = "g_Subaru";                 break;
    case FilterNames::r_Subaru:      s = "r_Subaru";                 break;
    case FilterNames::i_Subaru:      s = "i_Subaru";                 break;
    case FilterNames::z_Subaru:      s = "z_Subaru";                 break;
    case FilterNames::Ks_KPNO_CTIO:  s = "Ks_KPNO_CTIO";             break;
    case FilterNames::i_CFHT:        s = "i_CFHT";                   break;
    case FilterNames::u_SDSS:        s = "u_SDSS";                   break;
    case FilterNames::g_SDSS:        s = "g_SDSS";                   break;
    case FilterNames::r_SDSS:        s = "r_SDSS";                   break;
    case FilterNames::i_SDSS:        s = "i_SDSS";                   break;
    case FilterNames::z_SDSS:        s = "z_SDSS";                   break;
    case FilterNames::F814W_HST:     s = "F814W_HST";                break;
    case FilterNames::NB816_Subaru:  s = "NB816_Subaru";             break;
    case FilterNames::IA427_Subaru:  s = "IA427_Subaru";             break;
    case FilterNames::IA464_Subaru:  s = "IA464_Subaru";             break;
    case FilterNames::IA505_Subaru:  s = "IA505_Subaru";             break;
    case FilterNames::IA574_Subaru:  s = "IA574_Subaru";             break;
    case FilterNames::IA709_Subaru:  s = "IA709_Subaru";             break;
    case FilterNames::IA827_Subaru:  s = "IA827_Subaru";             break;
    case FilterNames::NB711_Subaru:  s = "NB711_Subaru";             break;
    case FilterNames::Ks_CFHT:       s = "Ks_CFHT";                  break;
    case FilterNames::J_UKIRT:       s = "J_UKIRT";                  break;
    case FilterNames::IA484_Subaru:  s = "IA484_Subaru";             break;
    case FilterNames::IA527_Subaru:  s = "IA527_Subaru";             break;
    case FilterNames::IA624_Subaru:  s = "IA624_Subaru";             break;
    case FilterNames::IA679_Subaru:  s = "IA679_Subaru";             break;
    case FilterNames::IA738_Subaru:  s = "IA738_Subaru";             break;
    case FilterNames::IA767_Subaru:  s = "IA767_Subaru";             break;
    case FilterNames::FUV_GALEX:     s = "FUV_GALEX";                break;
    case FilterNames::NUV_GALEX:     s = "NUV_GALEX";                break;
    case FilterNames::Zext_ACSf850lp:s = "Zext_ACSf850lp";    break;
    case FilterNames::Ynir_WFC3f105w:s = "Ynir_WFC3f105w";    break;
    case FilterNames::VIS_ACSf814w:  s = "VIS_ACSf814w";      break;
    case FilterNames::Rext_ACSf606w: s = "Rext_ACSf606w";     break;
    case FilterNames::Jnir_WFC3f125w:s = "Jnir_WFC3f125w";    break;
    case FilterNames::Iext_ACSf775w: s = "Iext_ACSf775w";     break;
    case FilterNames::Hnir_WFC3f160w:s = "Hnir_WFC3f160w";    break;
    case FilterNames::Gext_ACSf435w: s = "Gext_ACSf435w";     break;

    case FilterNames::Last:          s = "Last is undefined.";       break;
  };
  return s;
}

inline FilterNames string2filterNames( const std::string & s )   {
  FilterNames filterName;
  if     ( "None"           == s )   filterName = FilterNames::None;
  else if( "u_CFHT"         == s )   filterName = FilterNames::u_CFHT;
  else if( "B_Subaru"       == s )   filterName = FilterNames::B_Subaru;
  else if( "V_Subaru"       == s )   filterName = FilterNames::V_Subaru;
  else if( "g_Subaru"       == s )   filterName = FilterNames::g_Subaru;
  else if( "r_Subaru"       == s )   filterName = FilterNames::r_Subaru;
  else if( "i_Subaru"       == s )   filterName = FilterNames::i_Subaru;
  else if( "z_Subaru"       == s )   filterName = FilterNames::z_Subaru;
  else if( "Ks_KPNO_CTIO"   == s )   filterName = FilterNames::Ks_KPNO_CTIO;
  else if( "i_CFHT"         == s )   filterName = FilterNames::i_CFHT;
  else if( "u_SDSS"         == s )   filterName = FilterNames::u_SDSS;
  else if( "g_SDSS"         == s )   filterName = FilterNames::g_SDSS;
  else if( "r_SDSS"         == s )   filterName = FilterNames::r_SDSS;
  else if( "i_SDSS"         == s )   filterName = FilterNames::i_SDSS;
  else if( "z_SDSS"         == s )   filterName = FilterNames::z_SDSS;
  else if( "F814W_HST"      == s )   filterName = FilterNames::F814W_HST;
  else if( "NB816_Subaru"   == s )   filterName = FilterNames::NB816_Subaru;
  else if( "IA427_Subaru"   == s )   filterName = FilterNames::IA427_Subaru;
  else if( "IA464_Subaru"   == s )   filterName = FilterNames::IA464_Subaru;
  else if( "IA505_Subaru"   == s )   filterName = FilterNames::IA505_Subaru;
  else if( "IA574_Subaru"   == s )   filterName = FilterNames::IA574_Subaru;
  else if( "IA709_Subaru"   == s )   filterName = FilterNames::IA709_Subaru;
  else if( "IA827_Subaru"   == s )   filterName = FilterNames::IA827_Subaru;
  else if( "NB711_Subaru"   == s )   filterName = FilterNames::NB711_Subaru;
  else if( "Ks_CFHT"        == s )   filterName = FilterNames::Ks_CFHT;
  else if( "J_UKIRT"        == s )   filterName = FilterNames::J_UKIRT;
  else if( "IA484_Subaru"   == s )   filterName = FilterNames::IA484_Subaru;
  else if( "IA527_Subaru"   == s )   filterName = FilterNames::IA527_Subaru;
  else if( "IA624_Subaru"   == s )   filterName = FilterNames::IA624_Subaru;
  else if( "IA679_Subaru"   == s )   filterName = FilterNames::IA679_Subaru;
  else if( "IA738_Subaru"   == s )   filterName = FilterNames::IA738_Subaru;
  else if( "IA767_Subaru"   == s )   filterName = FilterNames::IA767_Subaru;
  else if( "FUV_GALEX"      == s )   filterName = FilterNames::FUV_GALEX;
  else if( "NUV_GALEX"      == s )   filterName = FilterNames::NUV_GALEX;
  else if( "Zext_ACSf850lp" == s )   filterName = FilterNames::Zext_ACSf850lp;
  else if( "Ynir_WFC3f105w" == s )   filterName = FilterNames::Ynir_WFC3f105w;
  else if( "VIS_ACSf814w"   == s )   filterName = FilterNames::VIS_ACSf814w;
  else if( "Rext_ACSf606w"  == s )   filterName = FilterNames::Rext_ACSf606w;
  else if( "Jnir_WFC3f125w" == s )   filterName = FilterNames::Jnir_WFC3f125w;
  else if( "Iext_ACSf775w"  == s )   filterName = FilterNames::Iext_ACSf775w;
  else if( "Hnir_WFC3f160w" == s )   filterName = FilterNames::Hnir_WFC3f160w;
  else if( "Gext_ACSf435w"  == s )   filterName = FilterNames::Gext_ACSf435w;
  else throw ElementsException("DataModel::DataModel : Unknown filter name : " + s );

  return filterName;
}

//-----------------------------------------------------------------------------

} /* namespace ChDataModel */
#endif /* FILTERNAMES_H_ */
