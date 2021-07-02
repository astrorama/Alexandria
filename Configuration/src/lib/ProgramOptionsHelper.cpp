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
 * @file src/lib/ProgramOptionsHelper.cpp
 * @date 06/15/16
 * @author nikoapos
 */

#include "Configuration/ProgramOptionsHelper.h"
#include <boost/algorithm/string/predicate.hpp>

namespace Euclid {
namespace Configuration {

std::string ProgramOptionsHelper::wildcard(const std::string& name, const std::string& instance) {
  return name + "-" + instance;
}

std::set<std::string>
ProgramOptionsHelper::findWildcardNames(const std::vector<std::string>& option_name_list,
                                        const std::map<std::string, boost::program_options::variable_value>& options) {
  std::set<std::string> result;
  for (auto& option_name : option_name_list) {
    for (auto& pair : options) {
      if (boost::starts_with(pair.first, option_name)) {
        auto name = pair.first.substr(option_name.size());
        if (!name.empty()) {
          name = name.substr(1);
        }
        result.insert(name);
      }
    }
  }
  return result;
}

}  // namespace Configuration
}  // namespace Euclid
