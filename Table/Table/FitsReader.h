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
 * @file Table/FitsReader.h
 * @date 12/05/16
 * @author nikoapos
 */

#ifndef _TABLE_FITSREADER_H
#define _TABLE_FITSREADER_H

#include <functional>
#include <CCfits/CCfits>
#include "Table/TableReader.h"

namespace Euclid {
namespace Table {

/**
 * @class FitsReader
 * @brief
 *
 */
class FitsReader : public TableReader {

public:
  
  FitsReader(const CCfits::HDU& hdu);
  
  FitsReader(const std::string& filename, int hdu_index=1);
  
  FitsReader(const std::string& filename, const std::string& hduName);
  
  FitsReader(FitsReader&&) = default;
  FitsReader& operator=(FitsReader&&) = default;
  
  FitsReader(const FitsReader&) = delete;
  FitsReader& operator=(const FitsReader&) = delete;

  /**
   * @brief Destructor
   */
  virtual ~FitsReader() = default;
  
  FitsReader& fixColumnNames(std::vector<std::string> column_names);

  const ColumnInfo& getInfo() override;
  
  void skip(long rows) override;
  
  bool hasMoreRows() override;
  
protected:

  Table readImpl(long rows) override;

private:
  
  void readColumnInfo();
  
  std::unique_ptr<CCfits::FITS> m_fits {nullptr};
  std::reference_wrapper<const CCfits::HDU> m_hdu; 
  bool m_reading_started = false;
  long m_total_rows = -1;
  long m_current_row = 1;
  std::vector<std::string> m_column_names {};
  std::shared_ptr<ColumnInfo> m_column_info;

}; /* End of FitsReader class */

} /* namespace Table */
} /* namespace Euclid */


#endif
