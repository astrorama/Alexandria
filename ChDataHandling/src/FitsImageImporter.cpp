/**
 * @file FitsImageImporter.cpp
 *
 * Created on: Sep 16, 2013
 *     Author: Pavel Binko
 */

#include "ChDataHandling/FitsImageImporter.h"
#include "ChDataModel/Fits/Image.h"

#include <iostream>

#include <boost/algorithm/string.hpp>

#include <CCfits/CCfits>
#include "CCfits/FitsError.h"
#include "CCfits/FITS.h"

#include "ChDataModel/Fits/Header.h"
#include "ChDataModel/Fits/Keyword.h"

using namespace std;
using namespace ChDataModel;
using namespace Fits;


//------------------------------------------------------------------------------

FitsImageImporter::FitsImageImporter(const std::string & fitsFileName) {
  // Open the FITS file for reading
  m_fileHandle = new CCfits::FITS(fitsFileName, CCfits::RWmode::Read);
}

//------------------------------------------------------------------------------

FitsImageImporter::~FitsImageImporter() {
  // Destroy the FITS object in memory and close the FITS file on disk
  m_fileHandle->destroy();
}

//------------------------------------------------------------------------------

ChDataModel::Fits::Image * FitsImageImporter::importImage(
    const std::string & hduName) {

  Image * image = new Image();

  // Check on the primary HDU or consecutive extension
  std::string lower_hduName = hduName;
  boost::algorithm::to_lower(lower_hduName);

  if (lower_hduName == FitsImageImporter::primaryHDUName) {

    // Primary HDU

    // Read the FITS file header from the primary HDU
    //   and place it directly into the image object
    this->readFitsHeader_primaryHDU(image);

    // Read the image contents from the primary HDU
    //   and place it directly into the image object
    this->readFitsImage_primaryHDU(image);

  }
  else {

    // Consecutive extension (identified by its name)

    // Read the FITS file header from an extension HDU
    //   and place it directly into the image object
    this->readFitsHeader_extHDU(hduName, image);

    // Read the image contents from an extension HDU
    //   and place it directly into the image object
    this->readFitsImage_extHDU(hduName, image);

  }

  return image;

}

//------------------------------------------------------------------------------

void FitsImageImporter::readFitsHeader_primaryHDU(
    ChDataModel::Fits::Image * image) {

  // Reading the keywords will happen from the primary HDU
  CCfits::HDU & ccfits_image = m_fileHandle->pHDU();
  this->readFitsHeader_internal(ccfits_image, image);

}

//------------------------------------------------------------------------------

void FitsImageImporter::readFitsHeader_extHDU(const std::string & hduName,
    ChDataModel::Fits::Image * image) {

  // Reading the keywords will happen from an extension HDU
  CCfits::HDU & ccfits_image = m_fileHandle->extension(hduName);
  this->readFitsHeader_internal(ccfits_image, image);

}

//------------------------------------------------------------------------------

void FitsImageImporter::readFitsHeader_internal(CCfits::HDU & ccfits_image,
    ChDataModel::Fits::Image * image) {

  // Read all the keywords, excluding those associated with columns
  ccfits_image.readAllKeys();

  // Key types in CCfits (key types starting with "V" have negative sign)
  //
  // Tbit = TBIT              -> long
  // Tbyte = TBYTE            -> long
  // Tlogical = TLOGICAL      -> bool
  // Tstring = TSTRING        -> string
  // Tushort = TUSHORT        -> long
  // Tshort = TSHORT          -> long
  // Tuint = TUINT            -> long
  // Tint = TINT              -> long
  // Tulong = TULONG          -> long
  // Tlong = TLONG            -> long
  // Tlonglong = TLONGLONG    -> long
  // Tfloat = TFLOAT          -> double
  // Tdouble = TDOUBLE        -> double
  // Tcomplex = TCOMPLEX      - not resolved
  // Tdblcomplex=TDBLCOMPLEX  - not resolved

  // Create the image header
  image->setHeader(new Header);

  // Access the map with all keywords
  std::map<std::string, CCfits::Keyword*> ccfits_map = ccfits_image.keyWord();
  for (auto & it : ccfits_map) {

    // Name
    string name = it.first;

    // Comment
    string comment = it.second->comment();

    // Value
    CCfits::ValueType keytype = it.second->keytype();

    switch (keytype) {
      case CCfits::ValueType::Tlogical :
      case CCfits::ValueType::VTlogical : {                        // Bool
        bool bool_value = it.second->value(bool_value);
        image->getHeader()->addKeyword(name, bool_value, comment);
        break;
      }

      case CCfits::ValueType::Tbit :
      case CCfits::ValueType::VTbit :
      case CCfits::ValueType::Tbyte :
      case CCfits::ValueType::VTbyte :
      case CCfits::ValueType::Tushort :
      case CCfits::ValueType::VTushort :
      case CCfits::ValueType::Tshort :
      case CCfits::ValueType::VTshort :
      case CCfits::ValueType::Tuint :
      case CCfits::ValueType::VTuint :
      case CCfits::ValueType::Tint :
      case CCfits::ValueType::VTint :
      case CCfits::ValueType::Tulong :
      case CCfits::ValueType::VTulong :
      case CCfits::ValueType::Tlong :
      case CCfits::ValueType::VTlong :
      case CCfits::ValueType::Tlonglong :
      case CCfits::ValueType::VTlonglong : {                       // Long
        long long_value = it.second->value(long_value);
        image->getHeader()->addKeyword(name, long_value, comment);
        break;
      }

      case CCfits::ValueType::Tfloat :
      case CCfits::ValueType::VTfloat :
      case CCfits::ValueType::Tdouble :
      case CCfits::ValueType::VTdouble : {                         // Double
        double double_value = it.second->value(double_value);
        image->getHeader()->addKeyword(name, double_value, comment);
        break;
      }

      case CCfits::ValueType::Tstring : {                          // String
        // The string declaration of the type string must be on a separate line
        string string_value;
        string_value = it.second->value(string_value);
        image->getHeader()->addKeyword(name, string_value, comment);
        break;
      }

      case CCfits::ValueType::Tcomplex :
      case CCfits::ValueType::Tdblcomplex : {                      // Complex
        stringstream errorBuffer;
        errorBuffer
            << "ChDataHandling::FitsImageImporter::readFitsHeader : The type "
            << keytype << " of the keyword " << name
            << " is currently not supported." << endl;
        throw ElementsException(errorBuffer.str());
        break;
      }

      default : {                                                  // The rest
        stringstream errorBuffer;
        errorBuffer
            << "ChDataHandling::FitsImageImporter::readFitsHeader : The keyword "
            << name << " has an unknown type " << keytype << "." << endl;
        throw ElementsException(errorBuffer.str());
      }

    } // Eof switch (keytype)

  } // Eof for (auto & it : ccfits_map)

  // Add special keywords into the image header
  this->addSpecialKeywords(ccfits_image, image);

} // Eof FitsImageImporter::readFitsHeader

//------------------------------------------------------------------------------

void FitsImageImporter::readFitsImage_primaryHDU(
    ChDataModel::Fits::Image * image) {

  // Reading the image will happen from the primary HDU
  CCfits::PHDU & ccfits_image = m_fileHandle->pHDU();

  std::valarray<double> imageContents = { };

  // Read the image contents
  ccfits_image.read(imageContents);

  // Copy the image contents into the image object
  image->setData(imageContents);
}

//------------------------------------------------------------------------------

void FitsImageImporter::readFitsImage_extHDU(const std::string & hduName,
    ChDataModel::Fits::Image * image) {

  // Reading the image will happen from an extension HDU
  CCfits::ExtHDU & ccfits_image = m_fileHandle->extension(hduName);

  std::valarray<double> imageContents = { };

  // Read the image contents
  ccfits_image.read(imageContents);

  // Copy the image contents into the image object
  image->setData(imageContents);

} // Eof FitsImageImporter::readFitsImage

//------------------------------------------------------------------------------

void FitsImageImporter::addSpecialKeywords(CCfits::HDU & hdu,
    ChDataModel::Fits::Image * image) {

  // Create the image header if not existing
  if (image->getHeader() == nullptr) {
    stringstream errorBuffer;
    errorBuffer
        << "ChDataHandling::FitsImageImporter::addSpecialKeywords : "
        << "The Header object must exist before adding special keywords."
        << endl;
    throw ElementsException(errorBuffer.str());
  }

  // Add special keywords into the map

  // NAXIS
  long nofAxes = hdu.axes();
  image->getHeader()->addKeyword("NAXIS", nofAxes, "Number of axes");

  // All keywords NAXIS*
  for(int i = 0; i < nofAxes; i++) {
    stringstream keywordName, commentText;
    keywordName << "NAXIS" << i+1;
    commentText << "Length of data axis " << i+1;
    image->getHeader()->addKeyword(keywordName.str(), hdu.axis(i), commentText.str());
  }

  // COMMENT
  image->getHeader()->addKeyword("COMMENT", hdu.getComments(), "");

  // HISTORY
  image->getHeader()->addKeyword("HISTORY", hdu.getHistory(), "");

} // Eof FitsImageImporter::addSpecialKeywords

//------------------------------------------------------------------------------
