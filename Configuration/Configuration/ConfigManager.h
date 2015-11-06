/*  
 * Copyright (C) 2012-2020 Euclid Science Ground Segment    
 *  
 * This library is free software; you can redistribute it and/or modify it under the terms of the GNU Lesser General  
 * Public License as published by the Free Software Foundation; either version 3.0 of the License, or (at your option)  
 * any later version.  
 *  
 * This library is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied  
 * warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more  
 * details.  
 *  
 * You should have received a copy of the GNU Lesser General Public License along with this library; if not, write to  
 * the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA  
 */  

/**
 * @file Configuration/ConfigManager.h
 * @date 11/05/15
 * @author nikoapos
 */

#ifndef _CONFIGURATION_CONFIGMANAGER_H
#define _CONFIGURATION_CONFIGMANAGER_H

#include <map>
#include <string>
#include <memory>
#include <typeindex>
#include <boost/program_options.hpp>

namespace Euclid {
namespace Configuration {

// Forward definition of the Configuration class. It is included in the .icpp
// file. This is done to break the include circle.
class Configuration;

/**
 * @class ConfigManager
 * @brief
 *
 */
class ConfigManager {

public:

  static ConfigManager& getInstance(long id);

  /**
   * @brief Destructor
   */
  virtual ~ConfigManager() = default;

  template <typename T>
  void registerConfiguration();
  
  boost::program_options::options_description closeRegistration();
  
  void initialize(const std::map<std::string, boost::program_options::variable_value>& user_values);
  
  template <typename T>
  T& getConfiguration();

private:
  
  ConfigManager(long id);
  
  enum class State {
    REGISTRATION, WAITING_INITIALIZATION, INITIALIZED
  };

  long m_id;
  State m_state = State::REGISTRATION;
  std::unique_ptr<std::type_index> m_root_config {nullptr};
  std::map<std::type_index, std::unique_ptr<Configuration>> m_config_dictionary {};

}; /* End of ConfigManager class */

} /* namespace Configuration */
} /* namespace Euclid */

#include "Configuration/_impl/ConfigManager.icpp"

#endif
