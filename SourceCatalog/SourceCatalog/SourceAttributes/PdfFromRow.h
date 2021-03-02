/*
 * Copyright (C) 2012-2021 Euclid Science Ground Segment
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
 * Copyright (C) 2012-2021 Euclid Science Ground Segment
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
 * @file PdfFromRow.h
 * @author nikoapos
 */

#ifndef SOURCECATALOG_PDFFROMROW_H
#define SOURCECATALOG_PDFFROMROW_H

#include "AlexandriaKernel/memory_tools.h"
#include "ElementsKernel/Exception.h"
#include "SourceCatalog/AttributeFromRow.h"
#include "SourceCatalog/SourceAttributes/Pdf.h"
#include "Table/CastVisitor.h"
#include <map>
#include <string>
#include <vector>

namespace Euclid {
namespace SourceCatalog {

template <typename T>
class PdfFromRow : public AttributeFromRow {

public:
  PdfFromRow(std::map<std::string, std::vector<T>> keys, std::map<std::string, std::string> column_names)
      : m_keys(std::move(keys)), m_column_names(std::move(column_names)) {}

  virtual ~PdfFromRow() = default;

  std::unique_ptr<Attribute> createAttribute(const Euclid::Table::Row& row) override {
    std::map<std::string, typename Pdf<T>::PdfType> pdf_map{};

    for (auto& pair : m_keys) {
      // Use the key values to create the axis of the PDF
      GridContainer::GridAxis<T> axis{pair.first, pair.second};
      // Create a PDF with zero values
      typename Pdf<T>::PdfType pdf{axis};

      // Get the PDF data from the row
      auto& col_name = m_column_names.at(pair.first);
      auto  data     = boost::apply_visitor(Table::CastVisitor<std::vector<double>>{}, row[col_name]);
      if (data.size() != pdf.size()) {
        throw Elements::Exception() << "Incompatible PDF size";
      }

      // Copy the data in the PDF
      std::copy(data.begin(), data.end(), pdf.begin());

      // Put the PDF in the map
      pdf_map.emplace(pair.first, std::move(pdf));
    }

    return make_unique<Pdf<T>>(std::move(pdf_map));
  }

private:
  std::map<std::string, std::vector<T>> m_keys;
  std::map<std::string, std::string>    m_column_names;
};

}  // namespace SourceCatalog
}  // namespace Euclid

#endif /* SOURCECATALOG_PDFFROMROW_H */
