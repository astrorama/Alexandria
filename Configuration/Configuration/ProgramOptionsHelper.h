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
 * @file Configuration/ProgramOptionsHelper.h
 * @date 06/15/16
 * @author nikoapos
 */

#ifndef _CONFIGURATION_PROGRAMOPTIONSHELPER_H
#define _CONFIGURATION_PROGRAMOPTIONSHELPER_H

#include <boost/program_options.hpp>
#include <map>
#include <set>
#include <string>

namespace Euclid {
namespace Configuration {

/**
 * @class ProgramOptionsHelper
 * @brief Class providing some helper methods for managing boost program options
 */
class ProgramOptionsHelper {

public:
  /**
   * @brief Destructor
   */
  virtual ~ProgramOptionsHelper() = default;

  /**
   * @brief Creates the name to use for a wildcard program option
   *
   * @details
   * This method has two usages. If is is called with only the name parameter,
   * it returns the name of the option as it should be appended to the boost
   * option_description when describing the option. If it is called with an
   * instance name, it returns the name to be used for retrieving the option
   * value from the boost variables_map. The names of the instances can be
   * retrieved by using the findWildcardNames() method.
   *
   * @param name The name of the wildcard option
   * @param instance The name of the instance
   * @return The wildcard option name
   */
  static std::string wildcard(const std::string& name, const std::string& instance = "*");

  /**
   * @brief Returns the instance names of wildcard options
   * @details
   * This method searches for all wildcard options in the option_name_list and
   * it returns the instance names to be used with the wildcard() method for
   * retrieving the option value from a boost variables_map.
   *
   * @param option_name_list The list of the wildcard options to search for
   * @param options The map with the values of the user
   * @return The instance names
   */
  static std::set<std::string>
  findWildcardNames(const std::vector<std::string>&                                      option_name_list,
                    const std::map<std::string, boost::program_options::variable_value>& options);

}; /* End of ProgramOptionsHelper class */

} /* namespace Configuration */
} /* namespace Euclid */

#endif
