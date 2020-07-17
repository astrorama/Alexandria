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
 *
 * @brief
 * Manages a set of configuration classes
 *
 * @details
 * The ConfigManager is responsible for handling a set of configuration classes.
 * For flexibility (for the case an executable is called from another one), this
 * class is not implemented as a singleton, but a factory method is provided,
 * which returns the manager instances based on an ID.
 *
 * Each manager instance is responsible for managing a set of configurations,
 * which can be registered by using the registerConfiguration() method. When
 * this method is used, all the dependencies of the configuration being registered
 * are also registered automatically.
 *
 * A manager can be under the following states, which describe how it can be used:
 * - Registration phase:
 *    This is the state a ConfigManager instance is in right after creation.
 *    During this phase configuration types can be added by using the
 *    registerConfiguration() method.
 * - Waiting for initialization phase:
 *    A manager goes in this state after a call to the closeRegistration() method.
 *    From this state on, the registerConfiguration() method cannot be used any
 *    more. The closeRegistration() returns a boost options_description which
 *    describes the options for all the managed configurations (it can be called
 *    more than once).
 * - Initialization phase:
 *    The initialization phase starts by calling the initialize() method. This
 *    method gets as arguments the user parameters to initialize the configurations
 *    with. During this phase, the manager performs three actions. First, it
 *    calls the preInitialize() method of all its managed configurations, in
 *    arbitrary order. Second, it calls the initialize() method of the managed
 *    configurations, in such order so all dependencies of a configuration have
 *    already been initialized before its method is called. Finally, it calls
 *    the postInitialize() methods, again in arbitrary order.
 * - Initialized phase:
 *    When all the managed configurations have been initialized (as described
 *    above) the manager enters the initialized state. At this phase, the user
 *    can use the getConfiguration() method for retrieving the information he
 *    needs.
 */
class ConfigManager {

public:

  /// Returns a reference to the ConfigManager with the given ID
  static ConfigManager& getInstance(long id);

  /**
   * @brief Destructor
   */
  virtual ~ConfigManager() = default;

  /**
   * @brief
   * Registers a Configuration to the manager
   *
   * @details
   * After this method is executed all the dependencies of the Configuration will
   * also be registered (recursively). This method can be executed more than one
   * time for the same configuration. Consecutive calls have no extra effect.
   *
   * @tparam T
   *    The type of the Configuration to register
   * @throws Elements::Exception
   *    If the manager is closed for registration
   */
  template <typename T>
  void registerConfiguration();

  /**
   * @brief
   * Registers a dependency between two configurations
   *
   * @details
   * This method can be used to define extra dependencies between configurations
   * than the ones defined by the configurations themselves. Calling this method
   * does not register the related configurations. If any of the related
   * configurations is not registered during the registration phase, the
   * dependency is ignored.
   *
   * The meaning of the template parameters is that the T1 depends on T2.
   *
   * @tparam T1
   *    The dependant Configuration type
   * @tparam T2
   *    The dependency Configuration type
   * @throws Elements::Exception
   *    If the manager is closed for registration
   */
  template <typename T1, typename T2>
  void registerDependency();

  /**
   * @brief
   * Terminates the manager registration phase
   *
   * @details
   * This call will make a test that there are no circular dependencies between
   * the registered configurations. The returned options_description can be
   * used for parsing the user input.
   *
   * @return
   *    The options_description describing the parameters of all the managed
   *    Configurations
   * @throws Elements::Exception
   *    If there are circular dependencies between the configurations
   */
  boost::program_options::options_description closeRegistration();


  /**
   * @brief
   * Initialize the manager
   *
   * @details
   * This method gets as arguments the user parameters to initialize the configurations
   * with. During the initialization phase, the manager performs three actions. First, it
   * calls the preInitialize() method of all its managed configurations, in
   * arbitrary order. Second, it calls the initialize() method of the managed
   * configurations, in such order so all dependencies of a configuration have
   * already been initialized before its method is called. Finally, it calls
   * the postInitialize() methods, again in arbitrary order.
   *
   * When this method returns, all the configurations are in FINAL state and the
   * manager in INITIALIZED state.
   *
   * @param user_values
   *    The user values to initialize the configurations with
   */
  void initialize(const std::map<std::string, boost::program_options::variable_value>& user_values);

  /**
   * @brief
   * Returns a reference to the requested configuration
   *
   * @tparam T
   *    The type of the Configuration
   * @return
   *    A reference to the requested configuration
   * @throws Elements::Exception
   *    If the manager is not initialized
   * @throws Elements::Exception
   *    If the manager does not manage the requested configuration
   */
  template <typename T>
  T& getConfiguration();

private:

  explicit ConfigManager(long id);

  enum class State {
    REGISTRATION, WAITING_INITIALIZATION, INITIALIZED
  };

  long m_id;
  State m_state = State::REGISTRATION;
  std::unique_ptr<std::type_index> m_root_config;
  std::map<std::type_index, std::unique_ptr<Configuration>> m_config_dictionary;
  std::map<std::type_index, std::set<std::type_index>> m_dependency_map;

}; /* End of ConfigManager class */

} /* namespace Configuration */
} /* namespace Euclid */

#include "Configuration/_impl/ConfigManager.icpp"

#endif
