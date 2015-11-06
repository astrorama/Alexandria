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
 * @brief
 *
 */
class PhotometryCatalogConfig : public Configuration {

public:

  PhotometryCatalogConfig(long manager_id);

  /**
   * @brief Destructor
   */
  virtual ~PhotometryCatalogConfig() = default;

  std::map<std::string, OptionDescriptionList> getProgramOptions() override;

  void initialize(const UserValues& args) override;

  void setBaseDir(const boost::filesystem::path& base_dir);

  const std::vector<std::string>& getPhotometricBands();
  
private:
  
  boost::filesystem::path m_base_dir {};
  std::vector<std::string> m_photometric_bands {};

}; /* End of PhotometryCatalogConfig class */

} /* namespace Configuration */
} /* namespace Euclid */


#endif
