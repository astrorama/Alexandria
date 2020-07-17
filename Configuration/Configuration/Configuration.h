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
 *
 * @brief
 * Superclass of all configuration classes
 *
 * @details
 * For details of how to implement specific configuration implementations see the
 * documentation of the virtual methods.
 */
class Configuration {

public:

  /// Defines the different states the configuration object can be in
  enum class State {
    /// The object has just been constructed
    CONSTRUCTED,
    /// The preInitialize() method has been called and waits for initialization
    PRE_INITIALIZED,
    /// The initialize() method has been called
    INITIALIZED,
    /// The postInitialize() method has been called
    FINAL
  };

  using OptionDescriptionList = std::vector<boost::program_options::option_description>;
  using UserValues = std::map<std::string, boost::program_options::variable_value>;

  /// Constructs a new Configuration instance
  explicit Configuration(long manager_id);

  /**
   * @brief Destructor
   */
  virtual ~Configuration() = default;

  /**
   * @brief
   * Returns the program options defined by a specific configuration
   *
   * @details
   * Configuration implementations should implement this method to return the
   * boost program option descriptions they require. The keys of the map will
   * be used as the group message in the final options grouping, so they can
   * be used for grouping options from different Configuration implementations.
   *
   * The default implementation returns an empty map.
   */
  virtual std::map<std::string, OptionDescriptionList> getProgramOptions();

  /**
   * @brief
   * Method which is called before the initialization phase
   *
   * @details
   * The Configuration implementations can override this method to implement
   * actions which are fast and do not require their dependencies (like textual
   * validation of the inputs). There is no guarantee on the order this method
   * is called between the dependent configurations.
   *
   * @param args
   *    The user parameters
   */
  virtual void preInitialize(const UserValues& args);

  /**
   * @brief
   * Method which is called during the initialization phase
   *
   * @details
   * The Configuration implementations should override this method to implement
   * their logic. When this method is called, all the configurations which are
   * defined as dependencies by using the declareDependency() method are
   * guaranteed to already be initialized.
   *
   * @param args
   *    The user parameters
   */
  virtual void initialize(const UserValues& args);

  /**
   * @brief
   * Method which is called after the initialization phase
   *
   * @brief
   * This method is called after all configurations have been initialized. It
   * can be overridden by Configurations which want to perform an action with
   * the guarantee that all other Configurations are initialized. There is no
   * guarantee on the order this method is called between the dependent
   * configurations.
   *
   * @param args
   *    The user parameters
   */
  virtual void postInitialize(const UserValues& args);

  /// Returns the dependencies of the configuration
  const std::set<std::type_index>& getDependencies();

  /// Returns the current state of the configuration
  State& getCurrentState();

  /// Returns the current state of the configuration
  State getCurrentState() const;

protected:

  /**
   * @brief
   * Declares a Configuration as dependency
   *
   * @brief
   * Configuration implementations can use this method in their constructor to
   * declare their dependencies.
   */
  template <typename T>
  void declareDependency();

  /**
   * @brief
   * Returns a dependency
   *
   * @details
   * Configuration implementations can use this method to get their dependencies
   * during the initialization phase.
   *
   * @return
   *    A reference to the dependency
   */
  template <typename T>
  T& getDependency();

  template <typename T>
  const T& getDependency() const;

private:

  long m_manager_id;
  std::set<std::type_index> m_dependencies;
  State m_state = State::CONSTRUCTED;

}; /* End of Configuration class */

} /* namespace Configuration */
} /* namespace Euclid */

#include "Configuration/_impl/Configuration.icpp"

#endif
