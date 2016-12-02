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
 * @file src/lib/AsciiWriter.cpp
 * @date 11/30/16
 * @author nikoapos
 */

#include <fstream>
#include <sstream>
#include <boost/lexical_cast.hpp>
#include "ElementsKernel/Exception.h"
#include "Table/AsciiWriter.h"
#include "AsciiWriterHelper.h"

namespace Euclid {
namespace Table {

AsciiWriter::AsciiWriter(std::ostream& stream) : AsciiWriter(InstOrRefHolder<std::ostream>::create(stream)) {
}

AsciiWriter::AsciiWriter(const std::string& filename) : AsciiWriter(create<std::ofstream>(filename)) {
}

AsciiWriter::AsciiWriter(std::unique_ptr<InstOrRefHolder<std::ostream>> stream_holder)
        : m_stream_holder(std::move(stream_holder)) {
}

AsciiWriter& AsciiWriter::setCommentIndicator(const std::string& indicator) {
  if (m_writing_started) {
    throw Elements::Exception() << "Changing comment indicator after writing "
            << "has started is not allowed";
  }
  if (indicator.empty()) {
    throw Elements::Exception() << "Empty string as comment indicator";
  }
  m_comment = indicator;
  return *this;
}

AsciiWriter& AsciiWriter::showColumnInfo(bool show) {
  if (m_writing_started) {
    throw Elements::Exception() << "Changing column info visibility after writing "
            << "has started is not allowed";
  }
  m_show_column_info = show;
  return *this;
}

void AsciiWriter::addComment(const std::string& message) {
  if (m_initialized) {
    throw Elements::Exception() << "Adding comments after writing data in ASCII "
            << "format is not allowed";
  }
  m_writing_started = true;
  
  std::stringstream message_stream {message};
  while (!message_stream.eof()) {
    std::string line;
    std::getline(message_stream, line);
    m_stream_holder->ref() << m_comment << ' ' << line << '\n';
  }
}

void AsciiWriter::init(const Table& table) {
  m_initialized = true;
  // If we have already written anything we leave an empty line
  if (m_writing_started) {
    m_stream_holder->ref() << '\n';
  }
  m_writing_started = true;
  
  auto& out = m_stream_holder->ref();
  
  // Write the column descriptions
  auto& info = *table.getColumnInfo();
  if (m_show_column_info) {
    for (size_t i=0; i<info.size(); ++i) {
      auto& desc = info.getDescription(i);
      out << m_comment << " Column: " << desc.name << ' ' << typeToKeyword(desc.type);
      if (!desc.unit.empty()) {
        out << " (" << desc.unit << ")";
      }
      if (!desc.description.empty()) {
        out << " - " << desc.description;
      }
      out << '\n';
    }
    out << '\n';
  }
  
  // Write the column names
  auto column_lengths = calculateColumnLengths(table);
  out << m_comment.c_str();
  for (size_t i=0; i<info.size(); ++i) {
    out << std::setw(column_lengths[i]) << info.getDescription(i).name;
  }
  out << "\n\n";
}

void AsciiWriter::append(const Table& table) {
  auto& out = m_stream_holder->ref();
  auto column_lengths = calculateColumnLengths(table);
  // The data lines are not prefixed with the comment string, so we need to fix
  // the length of the first column to get the alignment correctly
  column_lengths[0] = column_lengths[0] + m_comment.size();
  for (auto row : table) {
    for (size_t i=0; i<row.size(); ++i) {
      out << std::setw(column_lengths[i]) << boost::lexical_cast<std::string>(row[i]);
    }
    out << "\n";
  }
}


} // Table namespace
} // Euclid namespace



