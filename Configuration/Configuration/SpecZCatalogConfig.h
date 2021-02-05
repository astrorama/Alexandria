/*
 * Copyright (C) 2012-2021 Euclid Science Ground Segment
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
 * @file Configuration/SpecZCatalogConfig.h
 * @date 11/06/15
 * @author nikoapos
 */

#ifndef _CONFIGURATION_SPECZCATALOGCONFIG_H
#define _CONFIGURATION_SPECZCATALOGCONFIG_H

#include "Configuration/Configuration.h"

namespace Euclid {
namespace Configuration {

/**
 * @class SpecZCatalogConfig
 *
 * @brief
 * Configuration class for enabling SpecZ catalog input
 */
class SpecZCatalogConfig : public Configuration {

public:
  /// Constructs a new SpecZCatalogConfig object
  explicit SpecZCatalogConfig(long manager_id);

  /// Destructor
  virtual ~SpecZCatalogConfig() = default;

  /**
   * @brief
   * Returns the program options defined by the SpecZCatalogConfig
   *
   * @details
   * These options are:
   *  - spec-z-column-name      : The name of the column containing the SpecZ
   *  - spec-z-column-index     : The index (1-based) of the column containing the SpecZ
   *  - spec-z-err-column-name  : The name of the column containing the SpecZ error
   *  - spec-z-err-column-index : The index (1-based) of the column containing the SpecZ error
   *
   * Either the name or the column index can be provided but not both. The SpecZ
   * column information is mandatory while the error is optional (the error is
   * set to 0 if not provided)
   *
   * All options are in a group called "Input catalog options".
   *
   * @return The map with the option descriptions
   */
  std::map<std::string, OptionDescriptionList> getProgramOptions() override;

  /**
   * @brief
   * Checks that all the options are valid. See the exceptions thrown for a
   * detailed list of the checks.
   *
   * @param args
   *    The user parameters
   * @throws Elements::Exception
   *    If both the spec-z-column-name and spec-z-column-index are given
   * @throws Elements::Exception
   *    If none of the spec-z-column-name and spec-z-column-index are given
   * @throws Elements::Exception
   *    If the spec-z-column-index is an invalid one-based index (less than 1)
   * @throws Elements::Exception
   *    If both the spec-z-err-column-name and spec-z-err-column-index are given
   * @throws Elements::Exception
   *    If the spec-z-err-column-index is an invalid one-based index (less than 1)
   */
  void preInitialize(const UserValues& args) override;

  /**
   * @brief
   * Adds the SpectroscopicRedshiftAttributeFromRow handler to the CatalogCnofig
   *
   * @param args
   *    The user parameters
   * @throws Elements::Exception
   *    If the defined SpecZ column does not exist
   * @throws Elements::Exception
   *    If the defined SpecZ error column does not exist
   */
  void initialize(const UserValues& args) override;

private:
}; /* End of SpecZCatalogConfig class */

} /* namespace Configuration */
} /* namespace Euclid */

#endif
