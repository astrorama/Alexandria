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
 * @file Table/FitsWriter.h
 * @date 12/01/16
 * @author nikoapos
 */

#ifndef _TABLE_FITSWRITER_H
#define _TABLE_FITSWRITER_H

#include "Table/TableWriter.h"

namespace Euclid {
namespace Table {

/**
 * @class FitsWriter
 * @brief
 *
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
  
  FitsWriter(const std::string& filename);
  
  FitsWriter(std::shared_ptr<CCfits::FITS> fits);
  
  FitsWriter(FitsWriter&&) = default;
  FitsWriter& operator=(FitsWriter&&) = default;
  
  FitsWriter(const FitsWriter&) = delete;
  FitsWriter& operator=(const FitsWriter&) = delete;

  /**
   * @brief Destructor
   */
  virtual ~FitsWriter() = default;

  FitsWriter& overrideFile(bool override);
  
  FitsWriter& setFormat(Format format);
  
  FitsWriter& setHduName(const std::string& name);

  void addComment(const std::string& message) override;
  
protected:
  
  void init(const Table& table) override;
  
  void append(const Table& table) override;

private:
  
  std::string m_filename = "";
  std::shared_ptr<CCfits::FITS> m_fits = nullptr;
  bool m_initialized = false;
  bool m_override_file = true;
  Format m_format = Format::BINARY;
  std::string m_hdu_name = "";
  std::vector<std::string> m_comments {};
  int m_hdu_index = -1;
  long m_current_line = 0;

}; /* End of FitsWriter class */

} /* namespace Table */
} /* namespace Euclid */


#endif
