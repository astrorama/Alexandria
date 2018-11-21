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
 * @file src/lib/FitsWriter.cpp
 * @date 12/01/16
 * @author nikoapos
 */

#include <CCfits/CCfits>
#include "ElementsKernel/Exception.h"
#include "Table/FitsWriter.h"
#include "FitsWriterHelper.h"

namespace Euclid {
namespace Table {

FitsWriter::FitsWriter(const std::string& filename, bool override_flag)
        : m_filename(filename), m_override_file(override_flag) {
}

FitsWriter::FitsWriter(std::shared_ptr<CCfits::FITS> fits) : m_fits(fits) {
}

FitsWriter& FitsWriter::setFormat(Format format) {
  if (m_initialized) {
    throw Elements::Exception() << "Changing the format after writing "
            << "has started is not allowed";
  }
  m_format = format;
  return *this;
}

FitsWriter& FitsWriter::setHduName(const std::string& name) {
  if (m_initialized) {
    throw Elements::Exception() << "Changing the HDU name after writing "
            << "has started is not allowed";
  }
  m_hdu_name = name;
  return *this;
}

void FitsWriter::addComment(const std::string& message) {
  if (m_initialized) {
    throw Elements::Exception() << "Adding comments after writing "
            << "has started is not allowed";
  }
  m_comments.push_back(message);
}

void FitsWriter::init(const Table& table) {

  std::shared_ptr<CCfits::FITS> fits;
  if (m_fits != nullptr) {
    fits = m_fits;
  } else {
    // CCfits overrides the file if the name starts with !, otherwise it opens it
    std::string filename = (m_override_file ? "!" : "") + m_filename;
    fits = std::make_shared<CCfits::FITS>(filename, CCfits::RWmode::Write);
  }
  
  // Create the column info arrays to feed the CCfits based on the ColumnInfo object
  auto& info = *table.getColumnInfo();
  std::vector<std::string> column_name_list {};
  std::vector<std::string> column_unit_list {};
  for (size_t column_index=0; column_index<info.size(); ++column_index) {
    column_name_list.push_back(info.getDescription(column_index).name);
    column_unit_list.push_back(info.getDescription(column_index).unit);
  }
  std::vector<std::string> column_format_list = (m_format == Format::BINARY)
                                              ? getBinaryFormatList(table)
                                              : getAsciiFormatList(table);
  
  CCfits::HduType hdu_type = (m_format == Format::BINARY)
                           ? CCfits::HduType::BinaryTbl 
                           : CCfits::HduType::AsciiTbl;
  
  auto number_of_hdus_before = fits->extension().size();
  CCfits::Table* table_hdu = fits->addTable(m_hdu_name, 0, column_name_list,
                                           column_format_list, column_unit_list, hdu_type);
  bool new_hdu = number_of_hdus_before != fits->extension().size();
  m_hdu_index = table_hdu->index();
  m_current_line = table_hdu->rows() + 1;
  
  if (new_hdu) {
    // Write the customized description header keywords, and also dimensions for multidimensional arrays
    for (size_t column_index=0; column_index<info.size(); ++column_index) {
      auto& type = info.getDescription(column_index).type;
      auto& desc = info.getDescription(column_index).description;
      table_hdu->addKey("TDESC" + std::to_string(column_index+1), desc, "");

      if (type == typeid(NdArray::NdArray<double>)) {
        auto a = boost::get<NdArray::NdArray<double>>(table[0][column_index]);
        std::stringstream str;
        str << '(';

        auto shape = a.shape();
        int j;
        for (j = shape.size() - 1; j > 0; --j) {
          str << shape[j] << ",";
        }

        str << shape[j] << ')';
        table_hdu->addKey(CCfits::Column::TDIM() + std::to_string(column_index+1), str.str(), "");
      }
    }
    
    for (auto& c : m_comments) {
      table_hdu->writeComment(c);
    }
  }
  
  m_initialized = true;
}

void FitsWriter::append(const Table& table) {
  std::shared_ptr<CCfits::FITS> fits;
  if (m_fits != nullptr) {
    fits = m_fits;
  } else {
    fits = std::make_shared<CCfits::FITS>(m_filename, CCfits::RWmode::Write);
  }
  auto& table_hdu = fits->extension(m_hdu_index);
  
  auto& info = *table.getColumnInfo();
  for (size_t column_index=0; column_index<info.size(); ++column_index) {
    populateColumn(table, column_index, table_hdu, m_current_line);
  }
  m_current_line += table.size();
}

} // Table namespace
} // Euclid namespace



