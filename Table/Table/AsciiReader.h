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
 * @file Table/AsciiReader.h
 * @date 12/02/16
 * @author nikoapos
 */

#ifndef _TABLE_ASCIIREADER_H
#define _TABLE_ASCIIREADER_H

#include "AlexandriaKernel/InstOrRefHolder.h"
#include "Table/TableReader.h"

namespace Euclid {
namespace Table {

/**
 * @class AsciiReader
 * @brief
 *
 */
class AsciiReader : public TableReader {

public:
  
  template <typename StreamType, typename... Args>
  static AsciiReader create(Args&&... args);
  
  AsciiReader(std::istream& stream);
  
  AsciiReader(const std::string& filename);
  
  AsciiReader(AsciiReader&&) = default;
  AsciiReader& operator=(AsciiReader&&) = default;
  
  AsciiReader(const AsciiReader&) = delete;
  AsciiReader& operator=(const AsciiReader&) = delete;

  /**
   * @brief Destructor
   */
  virtual ~AsciiReader() = default;
  
  AsciiReader& setCommentIndicator(const std::string& indicator);
  
  AsciiReader& fixColumnNames(std::vector<std::string> column_names);
  
  AsciiReader& fixColumnTypes(std::vector<std::type_index> column_types);

  const ColumnInfo& getInfo() override;

  Table read(long rows=-1) override;
  
  void skip(long rows) override;
  
  bool hasMoreRows() override;

private:

  AsciiReader(std::unique_ptr<InstOrRefHolder<std::istream>> stream_holder);
  
  void readColumnInfo();
  
  std::unique_ptr<InstOrRefHolder<std::istream>> m_stream_holder;
  bool m_reading_started = false;
  std::string m_comment = "#";
  std::vector<std::type_index> m_column_types {};
  std::vector<std::string> m_column_names {};
  std::shared_ptr<ColumnInfo> m_column_info;

}; /* End of AsciiReader class */

} /* namespace Table */
} /* namespace Euclid */

#include "_impl/AsciiReader.icpp"

#endif
