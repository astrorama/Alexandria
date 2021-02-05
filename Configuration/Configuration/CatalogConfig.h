/*
 * Copyright (C) 2012-2021 Euclid Science Ground Segment
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

#include "Configuration/Configuration.h"
#include "SourceCatalog/AttributeFromRow.h"
#include "SourceCatalog/Catalog.h"
#include "Table/Table.h"
#include "Table/TableReader.h"
#include <boost/filesystem.hpp>
#include <functional>
#include <memory>
#include <vector>

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
 * of type Table::Table (using the method readAsTable() ) or of type
 * SourceCatalog::Catalog (using the method readAsCatalog() ). For performing partial
 * reading of the catalog the methods getTableReader() and getTableToCatalogConverter()
 * can be used instead.
 *
 * Any other configurations (like catalog specific configurations) can use the
 * getColumnInfo() method to retrieve the table column information, after the
 * CatalogConfig has been initialized.
 *
 * Because this is a generic class, it has no knowledge of the specific catalog
 * attributes. By default it does not use any attribute handlers and it only
 * parses the ID of the catalog entries. The more specific catalog configurations
 * (for example coordinates catalog), should declare the CatalogConfig
 * as a dependency and they should add an attribute handler during the initialize
 * phase. The more specific catalog configuration classes
 * can use the getColumnInfo() method to get the catalog columns information (if
 * needed).
 *
 */
class CatalogConfig : public Configuration {

public:
  /// A function that converts objects of type Table::Table to objects of type
  /// SourceCatalog::Catalog
  using TableToCatalogConverter = std::function<SourceCatalog::Catalog(const Table::Table&)>;

  /// Constructs a new CatalogConfig object
  explicit CatalogConfig(long manager_id);

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
   * @param args
   *    The user parameters
   * @throws Elements::Exception
   *    If there is any I/O error with reading the input-catalog-file
   * @throws Elements::Exception
   *    If the file has wrong format type
   * @throws Elements::Exception
   *    If the given file has no ID column, as described by the source-id-column-name
   *    and source-id-column-index parameters
   * @throws Elements::Exception
   *    If there is any I/O error with reading the input-catalog-file
   */
  void initialize(const UserValues& args) override;

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
   * @return
   *    A TableReader object that can be used to read the configured catalog
   */
  std::unique_ptr<Table::TableReader> getTableReader() const;

  /**
   * @return
   *    Column information about the catalog
   */
  std::shared_ptr<Table::ColumnInfo> getColumnInfo() const;

  /**
   * @return
   *    The name of the column that stores the object ID
   */
  std::string getIdColumn() const;

  /**
   * @return
   *    A callable that converts the table to a SourceCatalog
   */
  TableToCatalogConverter getTableToCatalogConverter() const;

  /**
   * @brief
   * Returns the catalog as a Table::Table object
   *
   * @details
   * This method can be called to read and retrieve the catalog as a Table::Table
   * object. When this method is called the information from the attribute
   * handlers is ignored and each row contains all the columns from the file.
   * Note that this method is going to read the full catalog each time it is called.
   *
   * @return
   *    The catalog as a Table::Table
   * @throws Elements::Exception
   *    If the instance is not yet final
   * @throws Elements::Exception
   *    If there is any I/O error with reading the input-catalog-file
   * @throws Elements::Exception
   *    If the file has wrong format type
   * @throws Elements::Exception
   *    If any of the registered attribute handlers fails
   */
  Table::Table readAsTable() const;

  /**
   * @brief
   * Returns the Catalog object
   *
   * @details
   * This method can be called to read and retrieve the catalog as a Catalog
   * object. It is a convenience method alternative from using the getTableReader()
   * and getTableToCatalogConverter() methods Note that this method is going to
   * read the full catalog each time it is called.
   *
   * @return
   *    The source catalog
   * @throws Elements::Exception
   *    If the instance is not yet final
   * @throws Elements::Exception
   *    If there is any I/O error with reading the input-catalog-file
   * @throws Elements::Exception
   *    If the file has wrong format type
   * @throws Elements::Exception
   *    If any of the registered attribute handlers fails
   */
  SourceCatalog::Catalog readAsCatalog() const;

  /**
   * @brief
   * Returns the filename of the input catalog
   *
   * @details
   * This method can be called only on instances of CatalogConfig which are
   * finalized.
   *
   * @return
   *    The filename of the input catalog
   * @throws Elements::Exception
   *    If the instance is not yet final
   */
  const boost::filesystem::path& getFilename() const;

private:
  boost::filesystem::path                                       m_base_dir;
  boost::filesystem::path                                       m_filename;
  bool                                                          m_fits_format = true;
  std::string                                                   m_id_column_name;
  std::vector<std::shared_ptr<SourceCatalog::AttributeFromRow>> m_attribute_handlers;
  std::shared_ptr<Table::ColumnInfo>                            m_column_info;

}; /* End of CatalogConfig class */

} /* namespace Configuration */
} /* namespace Euclid */

#endif
