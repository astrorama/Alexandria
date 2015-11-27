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
 * @file Configuration/Configuration.h
 * @date 11/05/15
 * @author nikoapos
 */

#ifndef _CONFIGURATION_CONFIGURATION_H
#define _CONFIGURATION_CONFIGURATION_H

#include <vector>
#include <set>
#include <map>
#include <string>
#include <typeindex>
#include <boost/program_options.hpp>

namespace Euclid {
namespace Configuration {

/**
 * @class Configuration
 * @brief
 *
 */
class Configuration {

public:
  
  enum class State {
    CONSTRUCTED,
    PRE_INITIALIZED,
    INITIALIZED,
    FINAL
  };

  using OptionDescriptionList = std::vector<boost::program_options::option_description>;
  using UserValues = std::map<std::string, boost::program_options::variable_value>;
  
  Configuration(long manager_id);

  /**
   * @brief Destructor
   */
  virtual ~Configuration() = default;
  
  virtual std::map<std::string, OptionDescriptionList> getProgramOptions();
  
  virtual void preInitialize(const UserValues& args);
  
  virtual void initialize(const UserValues& args);
  
  virtual void postInitialize(const UserValues& args);

  const std::set<std::type_index>& getDependencies();
  
  State& getCurrentState();
  
  State getCurrentState() const;
  
protected:
  
  template <typename T>
  void declareDependency();
  
  template <typename T>
  T& getDependency();

private:
  
  long m_manager_id;
  std::set<std::type_index> m_dependencies {};
  State m_state {State::CONSTRUCTED};

}; /* End of Configuration class */

} /* namespace Configuration */
} /* namespace Euclid */

#include "Configuration/_impl/Configuration.icpp"

#endif
