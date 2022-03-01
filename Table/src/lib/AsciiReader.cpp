/*
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
 * @file src/lib/AsciiReader.cpp
 * @date 12/02/16
 * @author nikoapos
 */

#include <boost/algorithm/string.hpp>
#include <fstream>
#include <set>

#if BOOST_VERSION < 107300
#include <boost/io/detail/quoted_manip.hpp>
#else
#include <boost/io/quoted.hpp>
#endif

#include "AlexandriaKernel/RegexHelper.h"
#include "ElementsKernel/Exception.h"
#include "Table/AsciiReader.h"

#include "AsciiReaderHelper.h"
#include "ReaderHelper.h"

namespace Euclid {
namespace Table {

static std::string _peekLine(std::istream& in) {
  std::string line;
  auto        pos = in.tellg();
  getline(in, line);
  in.seekg(pos);
  return line;
}

AsciiReader::AsciiReader(std::istream& stream) : AsciiReader(InstOrRefHolder<std::istream>::create(stream)) {}

AsciiReader::AsciiReader(const std::string& filename) : AsciiReader(create<std::ifstream>(filename)) {}

AsciiReader::AsciiReader(std::unique_ptr<InstOrRefHolder<std::istream>> stream_holder)
    : m_stream_holder(std::move(stream_holder)) {}

AsciiReader& AsciiReader::setCommentIndicator(const std::string& indicator) {
  if (m_reading_started) {
    throw Elements::Exception() << "Changing comment indicator after reading "
                                << "has started is not allowed";
  }
  if (indicator.empty()) {
    throw Elements::Exception() << "Empty string as comment indicator";
  }
  m_comment = indicator;
  return *this;
}

AsciiReader& AsciiReader::fixColumnNames(std::vector<std::string> column_names) {
  if (m_reading_started) {
    throw Elements::Exception() << "Fixing the column names after reading "
                                << "has started is not allowed";
  }

  m_column_names = std::move(column_names);

  std::set<std::string>     set{};
  static const regex::regex vertical_whitespace{".*[\\n\\v\\f\\r].*"};  // Checks if input contains any whitespace
                                                                        // characters
  for (const auto& name : m_column_names) {
    if (name.empty()) {
      throw Elements::Exception() << "Empty string column names are not allowed";
    }
    if (regex_match(name, vertical_whitespace)) {
      throw Elements::Exception() << "Column name '" << name << "' contains "
                                  << "vertical whitespace characters";
    }
    if (!set.insert(name).second) {  // Check for duplicate names
      throw Elements::Exception() << "Duplicate column name " << name;
    }
  }
  if (!m_column_names.empty() && !m_column_types.empty() && m_column_names.size() != m_column_types.size()) {
    throw Elements::Exception() << "Different number of column names and types";
  }

  return *this;
}

AsciiReader& AsciiReader::fixColumnTypes(std::vector<std::type_index> column_types) {
  if (m_reading_started) {
    throw Elements::Exception() << "Fixing the column types after reading "
                                << "has started is not allowed";
  }

  std::transform(column_types.begin(), column_types.end(), std::back_inserter(m_column_types),
                 [](std::type_index type) { return std::make_pair(type, std::size_t(0)); });

  if (!m_column_names.empty() && !m_column_types.empty() && m_column_names.size() != m_column_types.size()) {
    throw Elements::Exception() << "Different number of column names and types";
  }

  return *this;
}

AsciiReader& AsciiReader::fixColumnTypes(std::vector<std::pair<std::type_index, std::size_t>> column_types) {
  if (m_reading_started) {
    throw Elements::Exception() << "Fixing the column types after reading "
                                << "has started is not allowed";
  }

  m_column_types = std::move(column_types);

  if (!m_column_names.empty() && !m_column_types.empty() && m_column_names.size() != m_column_types.size()) {
    throw Elements::Exception() << "Different number of column names and types";
  }

  return *this;
}

void AsciiReader::readColumnInfo() {
  if (m_column_info != nullptr) {
    return;
  }
  m_reading_started = true;

  auto& in = m_stream_holder->ref();

  size_t columns_number = countColumns(in, m_comment);
  if (!m_column_names.empty() && m_column_names.size() != columns_number) {
    throw Elements::Exception() << "Columns number in stream (" << columns_number
                                << ") does not match the column names number (" << m_column_names.size() << ")";
  }
  if (!m_column_types.empty() && m_column_types.size() != columns_number) {
    throw Elements::Exception() << "Columns number in stream (" << columns_number
                                << ") does not match the column types number (" << m_column_types.size() << ")";
  }

  auto auto_names = autoDetectColumnNames(in, m_comment, columns_number);
  auto auto_desc  = autoDetectColumnDescriptions(in, m_comment);

  std::vector<std::string>                             names;
  std::vector<std::pair<std::type_index, std::size_t>> types;
  std::vector<std::string>                             units;
  std::vector<std::string>                             descriptions;
  auto                                                 first_line = firstDataLine(in, m_comment);

  for (size_t i = 0; i < columns_number; ++i) {
    if (m_column_names.empty()) {
      names.emplace_back(auto_names[i]);
    } else {
      names.emplace_back(m_column_names[i]);
    }
    auto info = auto_desc.find(auto_names[i]);
    if (info != auto_desc.end()) {
      if (m_column_types.empty()) {
        types.emplace_back(info->second.type, info->second.size);
      } else {
        types.emplace_back(m_column_types[i]);
      }
      units.emplace_back(info->second.unit);
      descriptions.emplace_back(info->second.description);
    } else {
      if (!m_column_types.empty()) {
        types.emplace_back(m_column_types[i]);
      } else if (i < first_line.size()) {
        types.emplace_back(guessColumnType(first_line[i]));
      } else {
        types.emplace_back(typeid(std::string), 0);
      }
      units.emplace_back("");
      descriptions.emplace_back("");
    }
  }
  m_column_info = createColumnInfo(names, types, units, descriptions);
}

const ColumnInfo& AsciiReader::getInfo() {
  readColumnInfo();
  return *m_column_info;
}

std::string AsciiReader::getComment() {
  std::ostringstream comment;

  m_reading_started = true;
  auto& in          = m_stream_holder->ref();
  while (in && _peekLine(in).compare(0, m_comment.size(), m_comment) == 0) {
    std::string line;
    getline(in, line);
    line = line.substr(m_comment.size());
    boost::trim(line);
    comment << line << '\n';
  }

  auto full_comment = comment.str();
  boost::trim(full_comment);
  return full_comment;
}

Table AsciiReader::readImpl(long rows) {
  readColumnInfo();
  auto& in = m_stream_holder->ref();

  std::vector<Row> row_list;
  while (in && rows != 0) {
    std::string line;
    getline(in, line);
    auto tokens = splitLine(line, m_comment);
    if (tokens.empty()) {
      continue;
    }
    if (tokens.size() != m_column_info->size()) {
      throw Elements::Exception() << "Line with wrong number of cells: " << line;
    }

    std::vector<Row::cell_type> values;
    values.reserve(tokens.size());
    std::size_t index = 0;
    std::transform(tokens.begin(), tokens.end(), std::back_inserter(values), [this, &index](const std::string& token) {
      return convertToCellType(token, m_column_info->getDescription(index++).type);
    });
    row_list.push_back(Row{std::move(values), m_column_info});
  }

  if (row_list.empty()) {
    throw Elements::Exception() << "No more table rows left";
  }
  return Table{std::move(row_list)};
}

void AsciiReader::skip(long rows) {
  readColumnInfo();
  auto& in = m_stream_holder->ref();

  while (in && rows != 0) {
    std::string line;
    getline(in, line);
    size_t comment_pos = line.find(m_comment);
    if (comment_pos != std::string::npos) {
      line = line.substr(0, comment_pos);
    }
    boost::trim(line);
    if (!line.empty()) {
      --rows;
    }
  }
}

bool AsciiReader::hasMoreRows() {
  return hasNextRow(m_stream_holder->ref(), m_comment);
}

std::size_t AsciiReader::rowsLeft() {
  return countRemainingRows(m_stream_holder->ref(), m_comment);
}

}  // namespace Table
}  // namespace Euclid
