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
 * @file src/lib/ConfigManager.cpp
 * @date 11/05/15
 * @author nikoapos
 */

#include "ElementsKernel/Exception.h"
#include "ElementsKernel/Logging.h"
#include "Configuration/Configuration.h"
#include "Configuration/ConfigManager.h"

namespace po = boost::program_options;

namespace Euclid {
namespace Configuration {

static Elements::Logging logger = Elements::Logging::getLogger("ConfigManager");

ConfigManager& ConfigManager::getInstance(long id) {
  static std::map<long, std::unique_ptr<ConfigManager>> manager_map {};
  auto& manager_ptr = manager_map[id];
  if (manager_ptr == nullptr) {
    manager_ptr.reset(new ConfigManager{id});
  }
  return *manager_ptr;
}

ConfigManager::ConfigManager(long id) : m_id{id} {
}

std::vector<std::type_index> hasCircularDependencies(const std::map<std::type_index, std::set<std::type_index>>& dependency_map,
                                                     const std::type_index& root, const std::pair<const std::type_index, std::set<std::type_index>>& config_pair) {
  if (config_pair.second.find(root) != config_pair.second.end()) {
    return {root};
  }
  for (auto& config : config_pair.second) {
    auto found = hasCircularDependencies(dependency_map, root, *dependency_map.find(config));
    if (!found.empty()) {
      std::vector<std::type_index> result {config};
      for (auto& type : found) {
        result.emplace_back(type);
      }
      return result;
    }
  }
  return {};
}

static void cleanupNonRegisteredDependencies(std::map<std::type_index, std::set<std::type_index>>& dep_map,
                                             const std::map<std::type_index, std::unique_ptr<Configuration>>& dict) {
  logger.info() << "Cleaning dependencies of unregistered configurations...";
  std::vector<std::type_index> unregistered_keys {};
  for (auto& pair : dep_map) {
    if (dict.find(pair.first) == dict.end()) {
      unregistered_keys.emplace_back(pair.first);
      continue;
    }
    std::vector<std::type_index> unregistered_values {};
    for (auto& value : pair.second) {
      if (dict.find(value) == dict.end()) {
        unregistered_values.emplace_back(value);
      }
    }
    for (auto& to_remove : unregistered_values) {
      logger.info() << "Removing configuration dependency " << pair.first.name()
                    << " -> " << to_remove.name();
      pair.second.erase(to_remove);
    }
  }
  for (auto& to_remove : unregistered_keys) {
    for (auto& value : dep_map.at(to_remove)) {
      logger.info() << "Removing configuration dependency " << to_remove.name()
                    << " -> " << value.name();
    }
    dep_map.erase(to_remove);
  }
}

po::options_description ConfigManager::closeRegistration() {
  m_state = State::WAITING_INITIALIZATION;
  
  // Populate the dependencies map
  for (auto& pair : m_config_dictionary) {
    m_dependency_map[pair.first].insert(pair.second->getDependencies().begin(),
                                        pair.second->getDependencies().end());
  }
  
  // Cleanup any dependencies related with non register configurations
  cleanupNonRegisteredDependencies(m_dependency_map, m_config_dictionary);
  
  // Check for circular dependencies
  for (auto& pair : m_config_dictionary) {
    auto found = hasCircularDependencies(m_dependency_map, pair.first, *m_dependency_map.find(pair.first));
    if (!found.empty()) {
      logger.error() << "Found circular dependency between configurations:";
      int count = 0;
      logger.error() << "    " << ++count << " : " << pair.first.name();
      for (auto& type : found) {
        logger.error() << "    " << ++count << " : " << type.name();
      }
      throw Elements::Exception() << "Circular dependency between configurations";
    }
  }
  
  std::map<std::string, po::options_description> all_options {};
  for (auto& config : m_config_dictionary) {
    for (auto& pair : config.second->getProgramOptions()) {
      if (all_options.find(pair.first) == all_options.end()) {
        all_options.emplace(pair.first, po::options_description{pair.first});
      }
      auto& group = all_options.at(pair.first);
      for (auto& option : pair.second) {
        group.add(boost::shared_ptr<po::option_description>{new po::option_description{option}});
      }
    }
  }
  
  po::options_description result {};
  for (auto& pair : all_options) {
    result.add(pair.second);
  }
  
  return result;
}

static void recursiveInitialization(const std::map<std::type_index, std::unique_ptr<Configuration>>& dictionary,
                                    const std::map<std::type_index, std::set<std::type_index>>& dependency_map,
                                    const std::map<std::string, po::variable_value>& user_values,
                                    const std::type_index& config) {
  if (dictionary.at(config)->getCurrentState() >= Configuration::State::INITIALIZED) {
    return;
  }
  
  for (auto& dependency : dependency_map.at(config)) {
    recursiveInitialization(dictionary, dependency_map, user_values, dependency);
  }
  
  dictionary.at(config)->initialize(user_values);
  dictionary.at(config)->getCurrentState() = Configuration::State::INITIALIZED;
}

void ConfigManager::initialize(const std::map<std::string, po::variable_value>& user_values) {
  m_state = State::INITIALIZED;
  for (auto& pair : m_config_dictionary) {
    pair.second->preInitialize(user_values);
    pair.second->getCurrentState() = Configuration::State::PRE_INITIALIZED;
  }
  for (auto& pair : m_config_dictionary) {
    recursiveInitialization(m_config_dictionary, m_dependency_map, user_values, pair.first);
  }
  for (auto& pair : m_config_dictionary) {
    pair.second->postInitialize(user_values);
    pair.second->getCurrentState() = Configuration::State::FINAL;
  }
}

} // Configuration namespace
} // Euclid namespace



