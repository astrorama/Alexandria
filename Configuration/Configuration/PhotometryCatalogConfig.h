/*  
 * Copyright (C) 2012-2020 Euclid Science Ground Segment    
 *  
 * This library is free software; you can redistribute it and/or modify it under
 * the terms of the GNU Lesser General Public License as published by the Free 
 * Software Foundation; either version 3.0 of the License, or (at your option)  
 * any later version.  
 *  
 * This library is distributed in the hope that it will be useful, but WITHOUT 
 * ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
 * FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more  
 * details.  
 *  
 * You should have received a copy of the GNU Lesser General Public License 
 * along with this library; if not, write to the Free Software Foundation, Inc.,
 * 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA  
 */  

/**
 * @file Configuration/PhotometryCatalogConfig.h
 * @date 11/06/15
 * @author nikoapos
 */

#ifndef _CONFIGURATION_PHOTOMETRYCATALOGCONFIG_H
#define _CONFIGURATION_PHOTOMETRYCATALOGCONFIG_H

#include <vector>
#include <string>
#include <boost/filesystem.hpp>
#include "Configuration/Configuration.h"

namespace Euclid {
namespace Configuration {

/**
 * @class PhotometryCatalogConfig
 * 
 * @brief
 * Configuration class for enabling photometric catalog input
 */
class PhotometryCatalogConfig : public Configuration {

public:

  /// Constructs a new PhotometryCatalogConfig object
  PhotometryCatalogConfig(long manager_id);

  /// Destructor
  virtual ~PhotometryCatalogConfig() = default;

  /**
   * @brief
   * Returns the program options defined by the PhotometryCatalogConfig
   *
   * @details
   * These options are:
   * - missing-photometry-flag : The flux value to indicate missing photometry data
   * - filter-mapping-file     : The file containing the catalog columns mapping
   * - exclude-filter          : The photometries to ignore
   *
   * All options are in a group called "Input catalog options". They are all
   * optional. The missing-photometr-flag defaults to the value -99 and the
   * filter-mapping-file to the file filter_mapping.txt. If the filter-mapping-file
   * is a relative path, it is relative to the directory set via the setBaseDir()
   * method, during the pre-initialize phase.
   * 
   * @return The map with the option descriptions
   */
  std::map<std::string, OptionDescriptionList> getProgramOptions() override;

  /**
   * @brief
   * Adds the PhotometryAttributeFromRow handler to the CatalogConfig and it
   * initializes the photometric bands list
   * 
   * @param args
   *    The user parameters
   * @throws Elements::Exception
   *    If the filter mapping file does not exist
   * @throws Elements::Exception
   *    If there are syntax errors in the filter mapping file (all non comment
   *    lines must be like "FILTER_NAME FLUX_COLUMN_NAME ERROR_COLUMN_NAME")
   * @throws Elements::Exception
   *    If any filter in the exclude-filter list does not exist in the file
   */
  void initialize(const UserValues& args) override;

  /**
   * @brief
   * Sets the directory used when resolving relative paths
   * 
   * @details
   * This method can be called by other Configuration classes during the pre-
   * initialization phase. By default the current working directory is used.
   * 
   * @param base_dir
   *    The directory to use for resolving relative paths
   * @throws Elements::Exception
   *    If the PhotometryCatalogConfig instance has already been initialized
   */
  void setBaseDir(const boost::filesystem::path& base_dir);

  /**
   * @brief
   * Returns the list of the photometric bands which are included in the catalog
   * 
   * @return
   *    The list of the photometric bands
   * @throws Elements::Exception
   *    If the instance is not yet initialized
   */
  const std::vector<std::string>& getPhotometricBands();
  
private:
  
  boost::filesystem::path m_base_dir {};
  std::vector<std::string> m_photometric_bands {};

}; /* End of PhotometryCatalogConfig class */

} /* namespace Configuration */
} /* namespace Euclid */


#endif
