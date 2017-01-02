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
 * 
 * @brief TableWriter implementation for writing ASCII tables to streams
 * 
 * @details
 * The format of the ASCII tables produced is the following:
 * 
 * The table starts with all the given comments, with one comment per line. The
 * comments are followed by one empty line. Comments can be added by using the
 * addComment() method. The comment indicator is by default the # character and
 * it can be modified by using the setCommentIndicator() method.
 * 
 * The next rows are comment lines describing the columns of the table. They
 * follow the format: "Column: NAME TYPE (UNIT) - DESCRIPTION", where the unit
 * and description parts are presented only when they are not empty. The strings
 * used as the column types are:
 *   - bool for boolean
 *   - int for 32 bit integer
 *   - long for 64 bit integer
 *   - float for 32 bit floating point
 *   - double for 64 bit floating point
 *   - string for string
 *   - [bool] for boolean vector
 *   - [int] for 32 bit integer vector
 *   - [long] for 64 bit integer vector
 *   - [float] for 32 bit floating point vector
 *   - [double] for 64 bit floating point vector
 * 
 * The column descriptions are following the same order as the columns of the
 * table and are followed by one empty line. These descriptions can be disabled
 * by using the showColumnInfo() method.
 * 
 * After that, the first row written is a comment line containing the names of
 * the columns, followed by one empty line. Then one line is written for each
 * Row of the table, which contains the values of the row. The boolean values
 * are represented with "1" (meaning true) and "0" meaning false. The vector
 * values are separated by ",".
 *
 * All the alignment between the columns is done with space characters. The size
 * in characters of each column is calculated as the size of the longest column
 * entry (including type and name) plus one. If a subsequent call of addData()
 * would result to longer columns, this is applied from that moment on. All the
 * values are right aligned.
 *
 */
class AsciiWriter : public TableWriter {

public:
  
  /**
   * @brief Constructs an AsciiWriter which contains an object of type StreamType
   * 
   * @details
   * This is the most generic construction of AsciiWriter, which can be used
   * with any type which inherits from std::istream. It is public to provide
   * full flexibility, but  the other constructors should cover most of the use
   * cases of this class. When this constructor is used, an object of type
   * StreamType is constructed using the given arguments, which will be deleted
   * when the AsciiWriter goes out of scope. If you want to not bound the lifetime
   * of the stream with the AsciiWriter you should use the AsciiWriter(std::ostream&)
   * constructor instead.
   * 
   * Note that when this method is called, only the StreamType template parameter
   * has to be specified. The argument types will be inferred.
   * 
   * @tparam StreamType
   *    The type of the stream to use for writing
   * @tparam Args
   *    The types of arguments to pass to the StreamType constructor
   * @param args
   *    The arguments to use for constructing the StreamType instance
   * @return 
   *    The newly constructed AsciiWriter
   */
  template <typename StreamType, typename... Args>
  static AsciiWriter create(Args&&... args);
  
  /// Constructs an AsciiWriter which writes to the given stream
  AsciiWriter(std::ostream& stream);
  
  /// Constructs an AsciiWriter which writes to the given file (overrides if
  /// it already exists)
  AsciiWriter(const std::string& filename);
  
  AsciiWriter(AsciiWriter&&) = default;
  AsciiWriter& operator=(AsciiWriter&&) = default;
  
  AsciiWriter(const AsciiWriter&) = delete;
  AsciiWriter& operator=(const AsciiWriter&) = delete;
  
  /**
   * @brief Destructor
   */
  virtual ~AsciiWriter() = default;
  
  /**
   * @brief Set the comment indicator
   * @details
   * This method can be used to change the comment indicator to something different
   * than the default (#). It returns a reference to the AsciiWriter so it can be
   * chained with other calls in the same line.
   * @return 
   *    A reference to the AsciiWriter instance
   * @throws Elements::Exception
   *    If the given indicator is the empty string
   * @throws Elements::Exception
   *    if writing of data has already started
   */
  AsciiWriter& setCommentIndicator(const std::string& indicator);
  
  /**
   * @brief Sets if the column information will be written to the stream
   * @param show
   *    True to write the information, false to skip it
   * @return 
   *    A reference to the AsciiWriter instance
   * @throws Elements::Exception
   *    if writing of data has already started
   */
  AsciiWriter& showColumnInfo(bool show);

  /**
   * @brief Adds a comment to the stream
   * @details
   * This method can only be called before any data have been written. It directly
   * adds a comment to the stream, following the rules explained at the documentation
   * of the class.
   * @param message
   *    The message to add
   * @throws Elements::Exception
   *    If data have already been written
   */
  void addComment(const std::string& message) override;
  
protected:
  
  /// Writes to the stream the column info, following the rules explained at the
  /// class documentation
  void init(const Table& table) override;
  
  /// Writes to the stream the contents of the table, following the rules
  /// explained at the class documentation
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
