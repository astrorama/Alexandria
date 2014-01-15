/**
 * @file FitsImageImporter.h
 *
 * Created on: Sep 16, 2013
 *     Author: Pavel Binko
 */

#ifndef FITSIMAGEIMPORTER_H_
#define FITSIMAGEIMPORTER_H_

#include <map>
#include <string>

#include <CCfits/CCfits>

#include <ChDataModel/Fits/Image.h>

//------------------------------------------------------------------------------

/**
 * @class FitsImageImporter
 * @brief
 *   Imports image in the FITS format
 */
class FitsImageImporter {

public:

  /**
   * @brief Constructor
   * @details
   *   It opens the FITS file.
   * @param fitsFileName
   *   The FITS file name
   */
  FitsImageImporter(const std::string & fitsFileName);

  /**
   * @brief Destructor
   * @details
   *   It destroys the CCfits::FITS object and closes the disk file.
   */
  virtual ~FitsImageImporter();

  /**
   * @brief importImage
   *   Imports FITS image
   * @details
   *   It is FITS data specific, it uses CCfits library
   * @return
   *   FITS image
   */
  ChDataModel::Fits::Image * importImage(const std::string & hduName);

  /**
   * @brief readFitsHeader_primaryHDU
   *   Reads the header from the primary HDU of the given FITS file.
   * @param hduName
   *   The name of the HDU.
   * @param image
   *   Pointer to the image object.
   * @throws
   *   ElementsException, if the FITS header is not OK.
   */
  void readFitsHeader_primaryHDU(ChDataModel::Fits::Image * image);

  /**
   * @brief readFitsHeader_extHDU
   *   Reads the header from an extension HDU of the given FITS file.
   * @param hduName
   *   The name of the HDU.
   * @param image
   *   Pointer to the image object.
   * @throws
   *   ElementsException, if the FITS header is not OK.
   */
  void readFitsHeader_extHDU(const std::string & hduName,
      ChDataModel::Fits::Image * image);

  /**
   * @brief readFitsImage_primaryHDU
   *   Reads the image from the primary HDU of the given FITS file.
  * @param hduName
   *   The name of the HDU.
   * @param image
   *   Pointer to the image object.
   * @throws
   *   ElementsException, if the FITS image is not OK.
   */
  void readFitsImage_primaryHDU(ChDataModel::Fits::Image * image);

  /**
   * @brief readFitsImage_extHDU
   *   Reads the image from an extension HDU of the given FITS file.
   * @param hduName
   *   The name of the HDU.
   * @param image
   *   Pointer to the image object.
   * @throws
   *   ElementsException, if the FITS image is not OK.
   */
  void readFitsImage_extHDU(const std::string & hduName,
      ChDataModel::Fits::Image * image);

private:

  /**
   * @brief readFitsHeader_internal
   *   Reads the header from an HDU (primary or extension).
   * @param ccfits_image
   *   Reference to the CCfits image object.
   * @param image
   *   Pointer to the image object.
   * @throws
   *   ElementsException, if the FITS image is not OK.
   */
  void readFitsHeader_internal(CCfits::HDU & ccfits_image,
      ChDataModel::Fits::Image * image);

  /**
   * @brief addSpecialKeywords
   *   Fills the header with the special keywords : NAXIS, NAXIS*, COMMENT, HISTORY.
   * @param hduName
   *   The CCfits HDU.
   * @param image
   *   Pointer to the image object.
   */
  void addSpecialKeywords(CCfits::HDU & hdu, ChDataModel::Fits::Image * image);

private:

  /**
   * FITS file handle
   */
  CCfits::FITS * m_fileHandle { };

  /**
   * Const string (all lower case) to compare with the argument hduName
   */
  std::string const primaryHDUName = "primaryhdu";

};

#endif /* FITSIMAGEIMPORTER_H_ */
