/*
 * CosmosAsciiMapping.cpp
 *
 *  Created on: Mar 5, 2013
 *      Author: Pavel Binko
 */

#include "ChDataHandling/CosmosAsciiMapping.h"

using namespace std;
using namespace ChDataModel;


CosmosAsciiMapping::CosmosAsciiMapping() {}
CosmosAsciiMapping::~CosmosAsciiMapping() {}


/*
 * @brief Photometry mapping.
 * @details Map of :
 *          - first  : Filter name.
 *          - second : Pair of column names :
 *                     first  : Value.
 *                     second : Value error.
 *
 * The data description file contains :
 *
 * original_name                                        description    units
 *          char                                               char     char
 *
 *            ID                                   Source ID number   number
 *       ID_2006      Source ID number in Capak et al. 2007 catalog   number
 *          tile                               Number of Image Tile   number
 *            RA                            Right Ascension (J2000)  degrees
 *           DEC                                Declination (J2000)  degrees
 *       pixel_x                 X pixel position within image tile   pixels
 *       pixel_y                 Y pixel position within image tile   pixels
 *        i_fwhm                            FWHM on detection image   pixels
 *         i_max                       Peak flux on detection image      nJy
 *        i_star             Stellarity measured on detection image   number
 *        i_auto                          Total magnitude in I band      mag
 *   auto_offset                                Aperture Correction      mag
 *     auto_flag  Source of aperture correction and total magnitude   number
 *             u                             CFHT u* band magnitude      mag
 *            du                    error on CFHT u* band magnitude      mag
 *             B                           Subaru Bj band magnitude      mag
 *            dB                  error on Subaru Bj band magnitude      mag
 *             V                           Subaru Vj band magnitude      mag
 *            dV                  error on Subaru Vj band magnitude      mag
 *             g                           Subaru g+ band magnitude      mag
 *            dg                  error on Subaru g+ band magnitude      mag
 *             r                           Subaru r+ band magnitude      mag
 *            dr                  error on Subaru r+ band magnitude      mag
 *             i                           Subaru i+ band magnitude      mag
 *            di                  error on Subaru i+ band magnitude      mag
 *             z                           Subaru z+ band magnitude      mag
 *            dz                  error on Subaru z+ band magnitude      mag
 *             K                        KPNO/CTIO Ks band magnitude      mag
 *            dK               error on KPNO/CTIO Ks band magnitude      mag
 *            ic                             CFHT i* band magnitude      mag
 *           dic                    error on CFHT i* band magnitude      mag
 *            us                              SDSS u band magnitude      mag
 *           dus                     error on SDSS u band magnitude      mag
 *            gs                              SDSS g band magnitude      mag
 *           dgs                     error on SDSS g band magnitude      mag
 *            rs                              SDSS r band magnitude      mag
 *           drs                     error on SDSS r band magnitude      mag
 *            is                              SDSS i band magnitude      mag
 *           dis                     error on SDSS i band magnitude      mag
 *            zs                              SDSS z band magnitude      mag
 *           dzs                     error on SDSS z band magnitude      mag
 *         F814W                           HST F814W band magnitude      mag
 *        dF814W                  error on HST F814W band magnitude      mag
 *         NB816                        Subaru NB816 band magnitude      mag
 *        dNB816               error on Subaru NB816 band magnitude      mag
 *         IA427                        Subaru IA427 band magnitude      mag
 *        dIA427               error on Subaru IA427 band magnitude      mag
 *         IA464                        Subaru IA464 band magnitude      mag
 *        dIA464               error on Subaru IA464 band magnitude      mag
 *         IA505                        Subaru IA505 band magnitude      mag
 *        dIA505               error on Subaru IA505 band magnitude      mag
 *         IA574                        Subaru IA574 band magnitude      mag
 *        dIA574               error on Subaru IA574 band magnitude      mag
 *         IA709                        Subaru IA709 band magnitude      mag
 *        dIA709               error on Subaru IA709 band magnitude      mag
 *         IA827                        Subaru IA827 band magnitude      mag
 *        dIA827               error on Subaru IA827 band magnitude      mag
 *         NB711                        Subaru NB711 band magnitude      mag
 *        dNB711               error on Subaru NB711 band magnitude      mag
 *            Kc                             CFHT Ks band magnitude      mag
 *           dKc                    error on CFHT Ks band magnitude      mag
 *             J                             UKIRT J band magnitude      mag
 *            dJ                    error on UKIRT J band magnitude      mag
 *         IA484                        Subaru IA484 band magnitude      mag
 *        dIA484               error on Subaru IA484 band magnitude      mag
 *         IA527                        Subaru IA527 band magnitude      mag
 *        dIA527               error on Subaru IA527 band magnitude      mag
 *         IA624                        Subaru IA624 band magnitude      mag
 *        dIA624               error on Subaru IA624 band magnitude      mag
 *         IA679                        Subaru IA679 band magnitude      mag
 *        dIA679               error on Subaru IA679 band magnitude      mag
 *         IA738                        Subaru IA738 band magnitude      mag
 *        dIA738               error on Subaru IA738 band magnitude      mag
 *         IA767                        Subaru IA767 band magnitude      mag
 *        dIA767               error on Subaru IA767 band magnitude      mag
 *          Eb_v                          Galactic extiction e(B-V)    color
 *               Dust, causing reddening, which is not intrinsic to the mission (not a magnitude)
 *               Measured by the satellite COBE - maps of dust in the Milky Way by D.J. Schlegel 1908
 *           FUV                                GALEX FUV magnitude      mag
 *          dFUV                       error on GALEX FUV magnitude      mag
 *           NUV                                GALEX NUV magnitude      mag
 *          dNUV                       error on GALEX NUV magnitude      mag
 *      mask_FUV                       Bad pixel mask for GALEX FUV   number
 *      mask_NUV                       Bad pixel mask for GALEX NUV   number
 *        B_mask                       Bad pixel mask for Subaru Bj   number
 *        V_mask                       Bad pixel mask for Subaru Vj   number
 *        i_mask                       Bad pixel mask for Subaru i+   number
 *        z_mask                       Bad pixel mask for Subaru z+   number
 *     deep_mask                                 Mask for deep area   number
 */

map<FilterNames, pair<string, string>> CosmosAsciiMapping::photometryMapping {
  { FilterNames::u_CFHT, { "u", "du" } },                 // u_cfht.res
  { FilterNames::B_Subaru, { "B", "dB" } },               // B_subaru.res
  { FilterNames::V_Subaru, { "V", "dV" } },               // V_subaru.res
  { FilterNames::g_Subaru, { "g", "dg" } },               // g_subaru.res
  { FilterNames::r_Subaru, { "r", "dr" } },               // r_subaru.res
  { FilterNames::i_Subaru, { "i", "di" } },               // i_subaru.res
  { FilterNames::z_Subaru, { "z_mag", "dz" } },           // z_subaru.res
  { FilterNames::Ks_KPNO_CTIO, { "K", "dK" } },           // flamingos_Ks.res
  { FilterNames::i_CFHT, { "ic", "dic" } },               // i_cfht.res
  { FilterNames::u_SDSS, { "us", "dus" } },               // u_SDSS.res
  { FilterNames::g_SDSS, { "gs", "dgs" } },               // g_SDSS.res
  { FilterNames::r_SDSS, { "rs", "drs" } },               // r_SDSS.res
  { FilterNames::i_SDSS, { "is", "dis" } },               // i_SDSS.res
  { FilterNames::z_SDSS, { "zs", "dzs" } },               // z_SDSS.res
  { FilterNames::F814W_HST, { "F814W", "dF814W" } },      // f814.pb
  { FilterNames::NB816_Subaru, { "NB816", "dNB816" } },   // NB816.pb
  { FilterNames::IA427_Subaru, { "IA427", "dIA427" } },   // IA427.res
  { FilterNames::IA464_Subaru, { "IA464", "dIA464" } },   // IA464.res
  { FilterNames::IA505_Subaru, { "IA505", "dIA505" } },   // IA505.res
  { FilterNames::IA574_Subaru, { "IA574", "dIA574" } },   // IA574.res
  { FilterNames::IA709_Subaru, { "IA709", "dIA709" } },   // IA709.res
  { FilterNames::IA827_Subaru, { "IA827", "dIA827" } },   // IA827.res
  { FilterNames::NB711_Subaru, { "NB711", "dNB711" } },   // NB711.pb
  { FilterNames::Ks_CFHT, { "Kc", "dKc" } },              // wircam_Ks.res - inconsistency between Ks and Kc
  { FilterNames::J_UKIRT, { "J", "dJ" } },                // J_wfcam.res
  { FilterNames::IA484_Subaru, { "IA484", "dIA484" } },   // IA484.res
  { FilterNames::IA527_Subaru, { "IA527", "dIA527" } },   // IA527.res
  { FilterNames::IA624_Subaru, { "IA624", "dIA624" } },   // IA624.res
  { FilterNames::IA679_Subaru, { "IA679", "dIA679" } },   // IA679.res
  { FilterNames::IA738_Subaru, { "IA738", "dIA738" } },   // IA738.res
  { FilterNames::IA767_Subaru, { "IA767", "dIA767" } },   // IA767.res
  { FilterNames::FUV_GALEX, { "FUV", "dFUV" } },          // galex1500.res
  { FilterNames::NUV_GALEX, { "NUV", "dNUV" } },          // galex2500.res
};

// For testing - reduced list of filters
//map<FilterNames, pair<string, string>> CosmosAsciiMapping::photometryMapping {
//  { FilterNames::u_CFHT,    { "u", "du" } },
//  { FilterNames::B_Subaru,  { "B", "dB" } },
//  { FilterNames::V_Subaru,  { "V", "dV" } },
//  { FilterNames::g_Subaru,  { "g", "dg" } },
//};


/*
 * @brief Source mapping.
 * @details Map of :
 *          - first  : Name of the variable in the class Source.
 *          - second : Column name.
 */
map<string, string> CosmosAsciiMapping::sourceMapping {
    { "sourceID",       "ID"},
    { "ra",             "ra"},
    { "dec",            "dec"}
};
