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
 * @file Table/FitsWriter.h
 * @date 12/01/16
 * @author nikoapos
 */

#ifndef _TABLE_FITSWRITER_H
#define _TABLE_FITSWRITER_H

#include "Table/TableWriter.h"
#include <CCfits/FITS.h>

namespace Euclid {
namespace Table {

/**
 * @class FitsWriter
 *
 * @brief TableWriter implementation for writing tables in FITS format
 *
 * @details
 * This class allows for both creating new FITS tables or extending existing
 * ones, based on the constructor used and the method setHduName(). For more
 * information see the documentation of the constructors and this method.
 *
 * The FITS table HDUs can be both in ASCII and binary format. The conventions
 * are the following:
 *
 *  ASCII format:
 * - bool<br>
 *   I1, where true is represented as 1 and false is represented as 0
 * - int32_t, int64_t<br>
 *   Iw, where w is the length required for the data of the column
 * - float, double<br>
 *   E12 (at the moment the length is is not modifiable)<br>
 * - std::string<br>
 *   Aw, where w is the length required for the data of the column
 *
 * Binary format:
 * - bool : L
 * - int32_t : J
 * - int64_t : K
 * - float : E
 * - double : D
 * - std::string : wA, where w is the length required for the data of the column
 * - vector<int32_t> : wJ, where w is the length of the vector
 * - vector<int64_t> : wK, where w is the length of the vector
 * - vector<float> : wE, where w is the length of the vector
 * - vector<double> : wD, where w is the length of the vector
 *
 * Note that, at the moment, only fixed length vector columns are supported
 * and that there is no support for vector columns for ASCII FITS tables.
 *
 * The TUNITn fits keywords are populated using the unit of the of the
 * ColumnDescriptions of the Table. The descriptions of the columns are
 * set as the values of the (non standard) keywords TDESCn.
 */
class FitsWriter : public TableWriter {

public:
  /// The format of the HDUs a FitsWriter creates
  enum class Format {
    /// FITS ASCII table HDU format
    ASCII,
    /// FITS binary table HDU format
    BINARY
  };

  /**
   * @brief Creates a FitsWriter that writes to a specific file
   *
   * @details
   * If the override_flag is set to true, any pre-existing file will be deleted.
   * If this flag is set to false and there is already an HDU with the name set
   * by the setHduName() method, the table of this HDU will be appended. Otherwise
   * a new table HDU will be added to the file.
   *
   * Note that when this constructor is used the FITS file will be re-opened each
   * time the addData() method is called. This takes away from the user the
   * responsibility of managing the lifetime of the CCfits::FITS objects, but it
   * might cause performance issues (especially with files with hundreds of HDUs).
   * If this is the case, consider to use the other constructor of this class.
   *
   * @param filename
   *    The path of the file to store the FITS table
   * @param override_flag
   *    When true, any existing file will be overridden
   */
  explicit FitsWriter(const std::string& filename, bool override_flag = false);

  /**
   * @brief Creates a FitsWriter that writes to a specific CCfits::FITS object
   *
   * @details
   * If the given obejct already contain an HDU with the name set by the setHduName()
   * method, the table of this HDU will be appended. Otherwisea new table HDU will
   * be added to the CCfits::FITS object.
   *
   * This constructor is not handling the opening/closing of the given file, so
   * is should be used when there are performance issues with the other constructor.
   * As the usage of this constructor delegates the management of the lifetime
   * of the CCfits::FITS object to the user, it is recommended to be used only
   * when performance issues have been identified.
   *
   * @param fits
   *    A pointer to the CCfits::FITS object to write the table
   */
  explicit FitsWriter(std::shared_ptr<CCfits::FITS> fits);

  FitsWriter(FitsWriter&&) = default;
  FitsWriter& operator=(FitsWriter&&) = default;

  FitsWriter(const FitsWriter&) = delete;
  FitsWriter& operator=(const FitsWriter&) = delete;

  /**
   * @brief Destructor
   */
  virtual ~FitsWriter() = default;

  /**
   * @brief Set the FITS table format
   * @details
   * It can be set either to ASCII or binary (default). It returns a reference to
   * the FitsWriter so it can be chained with other calls in the same line.
   * @param format
   *    One of FitsWriter::Format::ASCII, FitsWriter::Format::BINARY
   * @return
   *    A reference to the FitsWriter instance
   * @throws Elements::Exception
   *    if writing of data has already started
   */
  FitsWriter& setFormat(Format format);

  /**
   * @brief Set the HDU name where the table is written
   * @details
   * This method has to be called before any data are written and can be used to
   * change the name of the table HDU. If there is already existing a table HDU
   * with this name, any calls to the addData() method will append data to it.
   * Otherwise a new HDU will be added in the FITS file. The default name is the
   * empty string.
   * @param name
   *    The name of the HDU to write the table in
   * @return
   *    A reference to the FitsWriter instance
   */
  FitsWriter& setHduName(const std::string& name);

  /**
   * @brief Adds a comment to the stream
   * @details
   * This method can only be called before any data have been written. The comments
   * are written to the FITS during the first call of addData(). Note that if an
   * existing HDU is being appended (see setHduName() method) all comments are
   * ignored.
   * @param message
   *    The message to add
   * @throws Elements::Exception
   *    If data have already been written
   */
  void addComment(const std::string& message) override;

protected:
  /// Creates the FITS file if it needs to be created, the table HDU if the
  /// name already exist and writes the comments.
  void init(const Table& table) override;

  /// Writes to the FITS file the contents of the table, following the rules
  /// explained at the class documentation
  void append(const Table& table) override;

private:
  std::string                   m_filename      = "";
  std::shared_ptr<CCfits::FITS> m_fits          = nullptr;
  bool                          m_initialized   = false;
  bool                          m_override_file = true;
  Format                        m_format        = Format::BINARY;
  std::string                   m_hdu_name      = "";
  std::vector<std::string>      m_comments{};
  int                           m_hdu_index    = -1;
  long                          m_current_line = 0;

}; /* End of FitsWriter class */

} /* namespace Table */
} /* namespace Euclid */

#endif
