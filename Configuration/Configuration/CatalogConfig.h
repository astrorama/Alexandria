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
 * @file Configuration/CatalogConfig.h
 * @date 11/05/15
 * @author nikoapos
 */

#ifndef _CONFIGURATION_CATALOGCONFIG_H
#define _CONFIGURATION_CATALOGCONFIG_H

#include <memory>
#include <vector>
#include <boost/filesystem.hpp>
#include "Table/Table.h"
#include "SourceCatalog/Catalog.h"
#include "SourceCatalog/AttributeFromRow.h"
#include "Configuration/Configuration.h"

namespace Euclid {
namespace Configuration {

/**
 * @class CatalogConfig
 * @brief
 *
 */
class CatalogConfig : public Configuration {

public:

  CatalogConfig(long manager_id);

  /**
   * @brief Destructor
   */
  virtual ~CatalogConfig() = default;

  std::map<std::string, OptionDescriptionList> getProgramOptions() override;
  
  void preInitialize(const UserValues& args) override;
  
  void initialize(const UserValues& args) override;

  void postInitialize(const UserValues& args) override;

  void setBaseDir(const boost::filesystem::path& base_dir);
  
  void addAttributeHandler(std::shared_ptr<SourceCatalog::AttributeFromRow> handler);

  const Table::Table& getAsTable() const;
  
  const SourceCatalog::Catalog& getCatalog() const;

private:

  boost::filesystem::path m_base_dir {};
  std::unique_ptr<Table::Table> m_table_ptr {};
  std::vector<std::shared_ptr<SourceCatalog::AttributeFromRow>> m_attribute_handlers {};
  std::unique_ptr<SourceCatalog::Catalog> m_catalog_ptr {};
  
}; /* End of CatalogConfig class */

} /* namespace Configuration */
} /* namespace Euclid */

#endif
