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
 * @file Table/AsciiWriter.h
 * @date 11/30/16
 * @author nikoapos
 */

#ifndef _TABLE_ASCIIWRITER_H
#define _TABLE_ASCIIWRITER_H

#include "AlexandriaKernel/InstOrRefHolder.h"
#include "Table/TableWriter.h"

namespace Euclid {
namespace Table {

/**
 * @class AsciiWriter
 * @brief
 *
 */
class AsciiWriter : public TableWriter {

public:
  
  template <typename StreamType, typename... Args>
  static AsciiWriter create(Args&&... args);
  
  AsciiWriter(std::ostream& stream);
  
  AsciiWriter(const std::string& filename);
  
  AsciiWriter(AsciiWriter&&) = default;
  AsciiWriter& operator=(AsciiWriter&&) = default;
  
  AsciiWriter(const AsciiWriter&) = delete;
  AsciiWriter& operator=(const AsciiWriter&) = delete;
  
  /**
   * @brief Destructor
   */
  virtual ~AsciiWriter() = default;
  
  AsciiWriter& setCommentIndicator(const std::string& indicator);
  
  AsciiWriter& showColumnInfo(bool show);

  void addComment(const std::string& message) override;
  
protected:
  
  void init(const Table& table) override;
  
  void append(const Table& table) override;

private:

  AsciiWriter(std::unique_ptr<InstOrRefHolder<std::ostream>> stream_holder);
  
  std::unique_ptr<InstOrRefHolder<std::ostream>> m_stream_holder;
  bool m_writing_started = false;
  bool m_initialized = false;
  std::string m_comment = "#";
  bool m_show_column_info = true;
  std::vector<size_t> m_column_lengths;

}; // End of AsciiWriter class

} // namespace Table
} // namespace Euclid

#include "Table/_impl/AsciiWriter.icpp"

#endif
