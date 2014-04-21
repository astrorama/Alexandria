/** 
 * @file FitsReader.h
 * @date April 17, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef CHTABLE_FITSREADER_H
#define	CHTABLE_FITSREADER_H

#include <CCfits/CCfits>
#include "ChTable/Table.h"

namespace ChTable {

/**
 * @class FitsReader
 * 
 * @brief Tool for reading tables from FITS HDUs
 * 
 * @details
 * The FitsReader class is a tool for creating Table objects from FITS HDUs. It
 * can be parameterized with the arguments of its constructor and it provides
 * read() methods for reading the tables.
 */
class FitsReader {
  
public:
  
  /**
   * @brief
   * Constructs a new FitsReader with the given parameters
   * @details
   * The reader will use the given column names as the names used for the Table
   * instances it constructs. To enable auto-detection of column names from the
   * HDU header keywords, an empty vector should be passed. In this case the
   * TTYPEn keywords will be used. Any column without the TTYPEn keyword will be
   * given a name as "col1", "col2, etc (starting from 1).
   * 
   * @param column_names The names of the columns or empty for auto-detection (default)
   * @throws ElementsException
   *    if there are duplicate column names
   * @throws ElementsException
   *    if any of the given column names is empty or contains whitespace characters
   */
  FitsReader(std::vector<std::string> column_names = {});
  
  /**
   * @brief
   * Reads a Table from the given FITS HDU
   * @details
   * Note that this method can read both binary and ASCII table HDUs. In the case
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
   * are not supported, with exception the "A" format, which is translated to
   * a string.
   * 
   * @param hdu The HDU containing the table
   * @return the table
   * @throws ElementsException
   *    if the given HDU is not a binary or ASCII table HDU
   * @throws ElementsException
   *    if column names are given to the constructor and the HDU  contains data
   *    with different number of columns
   * @throws ElementsException
   *    if any column has a format that is not supported
   */
  const ChTable::Table read(const CCfits::HDU& hdu);
  
private:
  std::vector<std::string> m_column_names;
  
};

}

#endif	/* CHTABLE_FITSREADER_H */

