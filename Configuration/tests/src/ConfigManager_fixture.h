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
 * @file ConfigManager_fixture.h
 * @date Nov 9, 2015
 * @author Nikolaos Apostolakos
 */

#ifndef _PHZCONFIGURATION_CONFIGMANAGER_FIXTURE
#define _PHZCONFIGURATION_CONFIGMANAGER_FIXTURE

#include <chrono>
#include "Configuration/ConfigManager.h"
#include "Configuration/Utils.h"


struct ConfigManager_fixture {
  
  long timestamp = Euclid::Configuration::getUniqueManagerId();
  
  Euclid::Configuration::ConfigManager& config_manager = 
                      Euclid::Configuration::ConfigManager::getInstance(timestamp);
 
};

#endif // _PHZCONFIGURATION_CONFIGMANAGER_FIXTURE

