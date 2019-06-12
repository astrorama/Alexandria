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

/* 
 * @file PdfCatalogConfig.h
 * @author nikoapos
 */

#ifndef CONFIGURATION_PDFCATALOGCONFIG_H
#define CONFIGURATION_PDFCATALOGCONFIG_H

#include "ElementsKernel/Exception.h"
#include "SourceCatalog/SourceAttributes/PdfFromRow.h"
#include "Configuration/Configuration.h"
#include "Configuration/CatalogConfig.h"

namespace Euclid {
namespace Configuration {

template <typename T>
class PdfCatalogConfig : public Configuration {
  
public:
  
  PdfCatalogConfig(long manager_id) : Configuration(manager_id) {
    declareDependency<CatalogConfig>();
  }
  
  virtual ~PdfCatalogConfig() = default;
  
  void addPdfColumn(const std::string& pdf_name, const std::string& col_name,
                    std::vector<T> keys) {
    if (getCurrentState() >= State::INITIALIZED) {
      throw Elements::Exception() << "addPdfColumn() call to initialized PdfCatalogConfig";
    }
    m_keys.emplace(pdf_name, std::move(keys));
    m_column_names.emplace(pdf_name, col_name);
  }
  
  void initialize(const UserValues&) override {
    getDependency<CatalogConfig>().addAttributeHandler(std::make_shared<SourceCatalog::PdfFromRow<T>>(m_keys, m_column_names));
  }

  
private:
  
  std::map<std::string, std::vector<T>> m_keys;
  std::map<std::string, std::string> m_column_names;
  
};

}
}

#endif /* CONFIGURATION_PDFCATALOGCONFIG_H */

