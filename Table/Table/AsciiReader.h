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
 *
 * @brief TableReader implementation for reading ASCII tables from streams
 *
 * @details
 * The format of the ASCII tables this class can read is the following:
 *
 * Comment are supported and by default the comment character is the #. This can
 * be modified using the setCommentIndicator() method.
 *
 * The table can contain in its comments (before the data starts) the
 * descriptions of the columns. This is done by comment lines following the
 * format: "Column: NAME TYPE (UNIT) - DESCRIPTION", where the type, unit and
 * description parts are optional. Note that if the type is missing, the
 * column is read as a string column.
 *
 * The strings which can be used as the column types are:
 *   - bool, boolean : A boolean value as the following (case is ignored):
 *     - true, t, yes, y, 1
 *     - false, f, no, n, 0
 *   - int, int32 : A 32 bit integer
 *   - long, int64 : A 64 bit integer
 *   - float : Single (32 bit) precision floating point
 *   - double : Double (64 bit) precision floating point
 *   - string : String without whitespaces
 *   - [bool], [boolean] : A vector of booleans
 *   - [int], [int32] : A vector of 32 bit integers
 *   - [long], [int64] : A vector of 64 bit integers
 *   - [float] : Vector of single (32 bit) precision floating point
 *   - [double] : Vector of double (64 bit) precision floating point
 *
 * The last non empty comment line (before the data) can repeat the column
 * names and, if the column description comments are missing, is used for
 * detecting the column names. If both the column descriptions and the line
 * with the column names are missing, the columns are named with an increasing
 * counter as "col1", "col2", etc (starting from 1).
 *
 * If the column names comment is present, the column descriptions can be missing
 * and be given in any order.
 *
 * The above automatic detection of the names and types of the columns can be
 * overridden by used defined values, by calling the fixColumnNames() and
 * fixColumnTypes() methods.
 *
 * Note that the vector entries are values separated by "," (no spaces).
 *
 * The stream is red line by line and one row is created for each line which,
 * after comments are removed, does not contain only whitespace characters.
 * The columns are separated by one or more whitespace characters and all rows
 * must have the same number of columns.
 *
 */
class AsciiReader : public TableReader {

public:
  /**
   * @brief Constructs an AsciiReader which contains an object of type StreamType
   *
   * @details
   * This is the most generic construction of AsciiReader, which can be used
   * with any type which inherits from std::istream. It is public to provide
   * full flexibility, but  the other constructors should cover most of the use
   * cases of this class. When this constructor is used, an object of type
   * StreamType is constructed using the given arguments, which will be deleted
   * when the AsciiReader goes out of scope. If you want to not bound the lifetime
   * of the stream with the AsciiReader you should use the AsciiReader(std::istream&)
   * constructor instead.
   *
   * Note that when this method is called, only the StreamType template parameter
   * has to be specified. The argument types will be inferred.
   *
   * @tparam StreamType
   *    The type of the stream to use for reading
   * @tparam Args
   *    The types of arguments to pass to the StreamType constructor
   * @param args
   *    The arguments to use for constructing the StreamType instance
   * @return
   *    The newly constructed AsciiReader
   */
  template <typename StreamType, typename... Args>
  static AsciiReader create(Args&&... args);

  /// Constructs an AsciiReader which reads from the given stream
  explicit AsciiReader(std::istream& stream);

  /// Constructs an AsciiReader which reads from the given file
  explicit AsciiReader(const std::string& filename);

  AsciiReader(AsciiReader&&) = default;
  AsciiReader& operator=(AsciiReader&&) = default;

  AsciiReader(const AsciiReader&) = delete;
  AsciiReader& operator=(const AsciiReader&) = delete;

  /**
   * @brief Destructor
   */
  virtual ~AsciiReader() = default;

  /**
   * @brief Set the comment indicator
   * @details
   * This method can be used to change the comment indicator to something different
   * than the default (#). It returns a reference to the AsciiReader so it can be
   * chained with other calls in the same line.
   * @throws Elements::Exception
   *    If the given indicator is the empty string
   */
  AsciiReader& setCommentIndicator(const std::string& indicator);

  /**
   * @brief Overrides the automatically detected column names
   * @param column_names
   *    The names of the columns or empty for auto-detection
   * @return
   *    A reference to the AsciiReader instance
   * @throws Elements::Exception
   *    if there are duplicate column names
   * @throws Elements::Exception
   *    if any of the given column names is empty or contains whitespace characters
   * @throws Elements::Exception
   *    if automatic column type detection is overridden and the length of the
   *    vectors does not match
   */
  AsciiReader& fixColumnNames(std::vector<std::string> column_names);

  /**
   * @brief Overrides the automatically detected column types
   * @param column_types
   *    The types of the columns or empty for auto-detection
   * @return
   *    A reference to the AsciiReader instance
   * @throws Elements::Exception
   *    if automatic column name detection is overridden and the length of the
   *    vectors does not match
   */
  AsciiReader& fixColumnTypes(std::vector<std::type_index> column_types);

  AsciiReader& fixColumnTypes(std::vector<std::pair<std::type_index, std::size_t>> column_types);

  /**
   * @brief Returns the column information of the table
   * @details
   * For more details of the column info definition in the stream, see the
   * documentation of the class.
   * @return
   *    The description of the table columns
   * @throws Elements::Exception
   *    If automatic column type or name detection is overridden and the stream
   *    contains a different number of columns
   * @throws Elements::Exception
   *    if column name auto-detection is enabled and there are duplicate names
   */
  const ColumnInfo& getInfo() override;

  /**
   * @return Returns the comment associated to the table
   */
  std::string getComment() override;

  /// Implements the TableReader::skip() contract
  void skip(long rows) override;

  /// Implements the TableReader::hasMoreRows() contract
  bool hasMoreRows() override;

  /// Implements the TableReader::rowsLeft() contract
  std::size_t rowsLeft() override;

protected:
  /**
   * @brief Reads the next rows into a Table
   * @details
   * For more info see the TableReader::read() documentation
   * @param rows
   *    The number of rows to read
   * @return
   *    The table containing the row data
   * @throws Elements::Exception
   *    If automatic column type or name detection is overridden and the stream
   *    contains a different number of columns
   * @throws Elements::Exception
   *    if the stream does not contain any more non comment lines
   * @throws Elements::Exception
   *    if any cell cannot be converted to the correct type
   */
  Table readImpl(long rows) override;

private:
  explicit AsciiReader(std::unique_ptr<InstOrRefHolder<std::istream>> stream_holder);

  void readColumnInfo();

  std::unique_ptr<InstOrRefHolder<std::istream>>       m_stream_holder;
  bool                                                 m_reading_started = false;
  std::string                                          m_comment         = "#";
  std::vector<std::pair<std::type_index, std::size_t>> m_column_types{};
  std::vector<std::string>                             m_column_names{};
  std::shared_ptr<ColumnInfo>                          m_column_info;

}; /* End of AsciiReader class */

} /* namespace Table */
} /* namespace Euclid */

#include "_impl/AsciiReader.icpp"

#endif
