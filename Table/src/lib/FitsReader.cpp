/**
 * Copyright (C) 2012-2022 Euclid Science Ground Segment
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
 * @file src/lib/FitsReader.cpp
 * @date 12/05/16
 * @author nikoapos
 */

#include <set>

#include "AlexandriaKernel/memory_tools.h"
#include "ElementsKernel/Exception.h"
#include "ElementsKernel/Unused.h"
#include "Table/FitsReader.h"

#include "AlexandriaKernel/RegexHelper.h"
#include "FitsReaderHelper.h"
#include "ReaderHelper.h"

namespace Euclid {
namespace Table {

static CCfits::HDU& _readKeys(CCfits::HDU& hdu) {
  hdu.readAllKeys();
  return hdu;
}

FitsReader::FitsReader(const CCfits::HDU& hdu) : m_hdu(hdu) {}

FitsReader::FitsReader(const std::string& filename, int hduIndex)
    : m_fits(Euclid::make_unique<CCfits::FITS>(filename)), m_hdu(_readKeys(m_fits->extension(hduIndex))) {}

FitsReader::FitsReader(const std::string& filename, const std::string& hduName)
    : m_fits(Euclid::make_unique<CCfits::FITS>(filename)), m_hdu(_readKeys(m_fits->extension(hduName))) {}

FitsReader& FitsReader::fixColumnNames(std::vector<std::string> column_names) {
  if (m_reading_started) {
    throw Elements::Exception() << "Fixing the column names after reading "
                                << "has started is not allowed";
  }

  m_column_names = std::move(column_names);

  std::set<std::string> set{};
  regex::regex          whitespace{".*\\s.*"};  // Checks if input contains any whitespace characters
  for (const auto& name : m_column_names) {
    if (name.empty()) {
      throw Elements::Exception() << "Empty string column names are not allowed";
    }
    if (regex_match(name, whitespace)) {
      throw Elements::Exception() << "Column name '" << name << "' contains "
                                  << "whitespace characters";
    }
    if (!set.insert(name).second) {  // Check for duplicate names
      throw Elements::Exception() << "Duplicate column name " << name;
    }
  }

  return *this;
}

void FitsReader::readColumnInfo() {
  if (m_column_info != nullptr) {
    return;
  }
  m_reading_started = true;

  try {
    ELEMENTS_UNUSED auto& temp = dynamic_cast<const CCfits::Table&>(m_hdu.get());
  } catch (std::bad_cast&) {
    throw Elements::Exception() << "Given HDU is not a table";
  }
  const CCfits::Table& table_hdu = dynamic_cast<const CCfits::Table&>(m_hdu.get());

  m_total_rows = table_hdu.rows();

  std::vector<std::string> names{};
  if (m_column_names.empty()) {
    names = autoDetectColumnNames(table_hdu);
  } else if (m_column_names.size() != static_cast<size_t>(table_hdu.numCols())) {
    throw Elements::Exception() << "Columns number in HDU (" << table_hdu.numCols()
                                << ") does not match the column names number (" << m_column_names.size() << ")";
  } else {
    names = m_column_names;
  }
  m_column_info = createColumnInfo(names, autoDetectColumnTypes(table_hdu), autoDetectColumnUnits(table_hdu),
                                   autoDetectColumnDescriptions(table_hdu));
}

const ColumnInfo& FitsReader::getInfo() {
  readColumnInfo();
  return *m_column_info;
}

std::string FitsReader::getComment() {
  const CCfits::Table& table_hdu = dynamic_cast<const CCfits::Table&>(m_hdu.get());
  return table_hdu.comment();
}

Table FitsReader::readImpl(long rows) {
  readColumnInfo();

  // Compute how many rows we are going to read
  if (m_current_row > m_total_rows) {
    return Table(m_column_info);
  }
  if (rows == -1) {
    rows = m_total_rows - m_current_row + 1;
  }
  rows = std::min(rows, m_total_rows - m_current_row + 1);

  const CCfits::Table& table_hdu = dynamic_cast<const CCfits::Table&>(m_hdu.get());

  // CCfits reads per column, so we first read all the columns and then we
  // create all the rows
  std::vector<std::vector<Row::cell_type>> data;
  data.reserve(table_hdu.numCols());
  for (int i = 1; i <= table_hdu.numCols(); ++i) {
    // The i-1 is because CCfits starts from 1 and ColumnInfo from 0
    // We use a clone of the column because CCfits will cache in memory the read data, so multiple calls
    // to readImpl will steadily increase the memory consumption, which will only be released when
    // the FitsReader is destroyed (~FitsReader() => ~Table() => ~Column())
    // For scalars this is not a big deal, but when the column has an array (i.e. a bunch of PDZs), the
    // pile up can be significant after a while.
    std::unique_ptr<CCfits::Column> column(table_hdu.column(i).clone());
    data.emplace_back(
        translateColumn(*column, m_column_info->getDescription(i - 1).type, m_current_row, m_current_row + rows - 1));
  }

  m_current_row += rows;

  std::vector<Row> row_list;
  row_list.reserve(rows);
  for (int i = 0; i < rows; ++i) {
    std::vector<Row::cell_type> cells;
    cells.reserve(data.size());
    for (auto& column_data : data) {
      cells.emplace_back(std::move(column_data[i]));
    }
    row_list.emplace_back(cells, m_column_info);
  }

  return Table(std::move(row_list));
}

void FitsReader::skip(long rows) {
  readColumnInfo();
  m_current_row += rows;
}

bool FitsReader::hasMoreRows() {
  readColumnInfo();
  return m_current_row <= m_total_rows;
}

std::size_t FitsReader::rowsLeft() {
  readColumnInfo();
  return m_total_rows - m_current_row + 1;
}

}  // namespace Table
}  // namespace Euclid
