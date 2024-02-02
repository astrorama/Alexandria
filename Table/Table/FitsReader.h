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

/**
 * @file Table/FitsReader.h
 * @date 12/05/16
 * @author nikoapos
 */

#ifndef _TABLE_FITSREADER_H
#define _TABLE_FITSREADER_H

#include "Table/TableReader.h"
#include <CCfits/CCfits>
#include <functional>

namespace Euclid {
namespace Table {

/**
 * @class FitsReader
 *
 * @brief TableReader implementation for reading FITS tables
 *
 * @details
 * This class can read both binary and ASCII table HDUs. In the case
 * of ASCII table, the format mapping is the following:
 * - Aw (Character) : std::string
 * - Iw (Decimal integer) : int64_t
 * - Fw.d (Floating-point, fixed decimal notation) : double
 * - Ew.d (Floating-point, fixed exponential notation) : double
 * - Dw.d (Floating-point, fixed exponential notation) : double
 *
 * In the case of binary table, the format mapping is the following (note that
 * a subset of formats is only supported):
 * - L (Logical) : bool
 * - X (Bit) : NOT SUPPORTED
 * - B (Unsigned byte) : int32_t
 * - I (16-bit integer) : int32_t
 * - J (32-bit integer) : int32_t
 * - K (64-bit integer) : int64_t
 * - A (Character) : std::string
 * - E (Single precision floating point) : float
 * - D (Double precision floating point) : double
 * - C (Single precision complex) : NOT SUPPORTED
 * - M (Double precision complex) : NOT SUPPORTED
 * - P (Array Descriptor 32-bit) : NOT SUPPORTED
 * - Q (Array Descriptor 64-bit) : NOT SUPPORTED
 *
 * Note that repeat counts (which create arrays) in the binary table formats
 * are translated to vectors, with exception the "A" format, which is translated to
 * a string.
 *
 * The (non standard) keywords TDESCn are considered to contain the text
 * description of the column. The unit is retrieved by using the standard
 * TUNITn keyword. The names of the columns can be overridden by using the
 * method  fixColumnNames().
 *
 */
class FitsReader : public TableReader {

public:
  /**
   * @brief Creates a FitsReader that reads from the given HDU
   *
   * @details
   * This constructor delegates the lifetime management of the CCfits::HDU object
   * to the user. The given reference must be valid for all the lifetime of the
   * FitsReader object. This constructor is meant to be used for more advanced
   * use cases (like optimization). If you just want to read a table from a file
   * you should first consider the other constructors.
   *
   * @param hdu
   *    A reference to the CCfits::HDU to read the table from
   */
  explicit FitsReader(const CCfits::HDU& hdu);

  /// Creates a FitsReader that reads a table from a FITS file, based on the
  /// HDU index
  explicit FitsReader(const std::string& filename, int hdu_index = 1);

  /// Creates a FitsReader that reads a table from a FITS file, based on the
  /// HDU name
  FitsReader(const std::string& filename, const std::string& hduName);

  FitsReader(FitsReader&&)            = default;
  FitsReader& operator=(FitsReader&&) = default;

  FitsReader(const FitsReader&)            = delete;
  FitsReader& operator=(const FitsReader&) = delete;

  /**
   * @brief Destructor
   */
  virtual ~FitsReader() = default;

  /**
   * @brief Overrides the column names of the table
   * @param column_names
   *    The names of the columns or empty for auto-detection
   * @return
   *    A reference to the FitsReader instance
   * @throws Elements::Exception
   *    if there are duplicate column names
   * @throws Elements::Exception
   *    if any of the given column names is empty or contains whitespace characters
   * @throws Elements::Exception
   *    if the FitsReader instance has already been used for reading
   */
  FitsReader& fixColumnNames(std::vector<std::string> column_names);

  /**
   * @brief Returns the column information of the table
   * @details
   * For more details of the column info definition in the FITS file, see the
   * documentation of the class.
   * @return
   *    The description of the table columns
   * @throws Elements::Exception
   *    If automatic column type or name detection is overridden and the HDU
   *    contains a different number of columns
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
  /// Implements the TableReader::readImpl() contract
  Table readImpl(long rows) override;

private:
  void readColumnInfo();

  std::unique_ptr<CCfits::FITS>             m_fits{nullptr};
  std::reference_wrapper<const CCfits::HDU> m_hdu;
  bool                                      m_reading_started = false;
  long                                      m_total_rows      = -1;
  long                                      m_current_row     = 1;
  std::vector<std::string>                  m_column_names{};
  std::shared_ptr<ColumnInfo>               m_column_info;

}; /* End of FitsReader class */

} /* namespace Table */
} /* namespace Euclid */

#endif
