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
 * 
 * @brief
 * Configuration class for enabling catalog input
 * 
 * @details
 * The CatalogConfiguration class provides the basis for reading input catalogs.
 * It provides all the functionality for reading an input catalog as an object
 * of type Table::Table and for converting it to an object of type
 * SourceCatalog::Catalog.
 *
 * Because this is a generic class, it has no knowledge of the specific catalog
 * attributes. By default it does not use any attribute handlers and it only
 * parses the ID of the catalog entries. The more specific catalog configurations
 * (for example coordinates catalog), should declare the CatalogConfig
 * as a dependency and they should add an attribute handler during the initialize
 * phase. The CatalogConfig class reads the catalog from the file as a Table::Table
 * during the initialize phase, so the more specific catalog configuration classes
 * can use the getAsTable() method to get the catalog columns information (if
 * needed).
 * 
 * Note that the SourceCatalog::Catalog object is initialized during the
 * post-initialize phase, so all the catalog specific configurations have already
 * register their handlers.
 */
class CatalogConfig : public Configuration {

public:

  /// Constructs a new CatalogConfig object
  CatalogConfig(long manager_id);

  /// Destructor
  virtual ~CatalogConfig() = default;

  /**
   * @brief
   * Returns the program options defined by the CatalogConfig
   *
   * @details
   * These options are:
   * - input-catalog-file     : The file containing the input catalog
   * - input-catalog-format   : The format of the input catalog (one of AUTO, FITS or ASCII)
   * - source-id-column-name  : The name of the column representing the source ID
   * - source-id-column-index : The index (1-based) of the column representing the source ID
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
   *    If both the source-id-column-name and source-id-column-index are given
   * @throws Elements::Exception
   *    If the source-id-column-index is an invalid one-based index (less than 1)
   * @throws Elements::Exception
   *    If the input-catalog-format is not one of AUTO, FITS or ASCII
   */
  void preInitialize(const UserValues& args) override;
  
  /**
   * @brief
   * Initializes the CatalogConfig instance
   * 
   * @details
   * During the initialization the file defined by the input-catalog-file option
   * is parsed into a Table::Table object.
   * 
   * @param args
   *    The user parameters
   * @throws Elements::Exception
   *    If there is any I/O error with reading the input-catalog-file
   * @throws Elements::Exception
   *    If the file has wrong format type
   */
  void initialize(const UserValues& args) override;

  /**
   * @brief
   * Post-initializes the CatalogConfig instance
   * 
   * @details
   * During the post-initialization, the already parsed Table::Table object is
   * converted to a SourceCatalog::Catalog object, using the attribute handlers
   * set by the addAttributeHandler() method.
   * 
   * @param args
   *    The user parameters
   * @throws Elements::Exception
   *    If the given file has no ID column, as described by the source-id-column-name
   *    and source-id-column-index parameters
   * @throws Elements::Exception
   *    If any of the registered attribute handlers fails
   */
  void postInitialize(const UserValues& args) override;

  /**
   * @brief
   * Sets the directory used when resolving relative paths
   * 
   * @details
   * This method can be called by other Configuration classes during the pre-
   * initialization phase. By default the current working directory is used.
   * 
   * @param base_dir
   *    The directory to use for resolving relative paths
   * @throws Elements::Exception
   *    If the CatalogConfig instance has already been initialized
   */
  void setBaseDir(const boost::filesystem::path& base_dir);
  
  /**
   * @brief
   * Adds an attribute handler which will be used for adding attributes at the
   * catalog objects
   * 
   * @details
   * This method can be called by other configuration classes before the post-
   * initialization phase, to add extra attributes to the catalog.
   * 
   * @param handler
   *    The AttributeHandler to add
   * @throws Elements::Exception
   *    If the CatalogConfig instance has already been finalized
   */
  void addAttributeHandler(std::shared_ptr<SourceCatalog::AttributeFromRow> handler);

  /**
   * @brief
   * Returns the catalog as a Table::Table object
   * 
   * @details
   * This method can be called after the CatalogConfig has been initialized, and
   * it can be used by other configurations which need the catalog column info.
   * 
   * @return 
   *    The catalog as a Table::Table
   * @throws Elements::Exception
   *    If the instance is not yet initialized
   */
  const Table::Table& getAsTable() const;
  
  /**
   * @brief
   * Returns the Catalog object
   * 
   * @details
   * This method can be called only on instances of CatalogConfig which are
   * finalized.
   * 
   * @return
   *    The source catalog
   * @throws Elements::Exception
   *    If the instance is not yet final
   */
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
