/** 
 * @file FitsWriter.h
 * @date April 23, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef CHTABLE_FITSWRITER_H
#define	CHTABLE_FITSWRITER_H

#include <CCfits/CCfits>
#include <string>
#include "ChTable/Table.h"

namespace ChTable {

/**
 * @class FitsWriter
 * 
 * @brief Tool for writing tables in FITS format
 * 
 * @details
 * The FitsWriter class is a tool for writing Table objects in FITS format. It
 * can be parameterized with the arguments of its constructor and it provides
 * write() methods for writing the tables.
 */
class FitsWriter {
  
public:
  
  /// The format of the HDUs a FitsWriter creates
  enum class Format {
    /// FITS ASCII table HDU format
    ASCII,
    /// FITS binary table HDU format
    BINARY
  };
  
  /**
   * @brief
   * Constructs a new FitsWriter
   * 
   * @param format The output HDU format
   */
  FitsWriter(Format format = Format::BINARY);
  
  /**
   * @brief
   * Adds a table HDU to a FITS object
   * @details
   * The format of the columns of the table depends on the format the FitsWriter
   * is initialized for. The conversions are the following:
   * 
   * ASCII format:
   * - bool<br>
   *   I1, where true is represented as 1 and false is represented as 0
   * - int32_t, int64_t<br>
   *   Iw, where w is the length required for the data of the column
   * - float, double<br>
   *   Ew.d, where w and d are the lengths required for the data of the column
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
   * 
   * @param fits The FITS object to add the table HDU
   * @param hdu_name The name of the HDU
   * @param table The table to output
   */
  void write(CCfits::FITS& fits, const std::string& hdu_name, const Table& table) const;
  
private:
  Format m_format;
  
};

}

#endif	/* CHTABLE_FITSWRITER_H */

