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
   *                             If not provided the functionality is disabled
   * - enable-upper-limit      : Define if the catalog contains flux upper limit
   *                             (YES/NO by default NO)
   *
   * All options are in a group called "Input catalog options". They are all
   * optional. The missing-photometr-flag defaults to the value -99.
   *
   * @return The map with the option descriptions
   */
  std::map<std::string, OptionDescriptionList> getProgramOptions() override;

  /**
   * @brief
   * Adds the PhotometryAttributeFromRow handler to the CatalogConfig
   *
   * @param args
   *    The user parameters
   */
  void initialize(const UserValues& args) override;

  bool hasMissingPhotometry();

  bool hasUpperLimit();

private:
  bool m_has_missing_photometry {false};
  bool m_has_upper_limit {false};

}; /* End of PhotometryCatalogConfig class */

} /* namespace Configuration */
} /* namespace Euclid */


#endif
