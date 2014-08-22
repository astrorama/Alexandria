/**
 * @file ChTable/AsciiWriter.h
 * @date April 16, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef CHTABLE_ASCIIWRITER_H
#define	CHTABLE_ASCIIWRITER_H

#include <string>
#include <ostream>

#include "ElementsKernel/Export.h"

#include "ChTable/Table.h"

namespace Euclid {
namespace ChTable {

/**
 * @class AsciiWriter
 *
 * @brief Tool for writing ASCII tables to streams
 *
 * @details
 * The AsciiWriter class is a tool for writing ASCII representations of Table
 * objects in output streams. It can be parameterised with the arguments of its
 * constructors and it provides write() methods for writing the tables.
 */
class ELEMENTS_API AsciiWriter {

public:

  /**
   * @brief
   * Constructs a new AsciiWriter
   *
   * @param comment The pattern to use for comment lines
   * @throws ElementsException
   *    if the comment string is the empty string
   */
  AsciiWriter(std::string comment = "#");

  /// Default destructor
  virtual ~AsciiWriter() = default;

  /**
   * @brief
   * Writes a Table in the given stream
   * @details
   * The first row written in the file is a comment line containing the names of
   * the columns, as described by the ColumnInfo of the table. The second row is
   * a comment containing the types of the columns. The strings used are:
   *   - bool for boolean
   *   - int for 32 bit integer
   *   - long for 64 bit integer
   *   - float for 32 bit floating point
   *   - double for 64 bit floating point
   *   - string for string
   *
   * An empty line follows these two lines and then one line is written for each
   * Row of the table, which contains the values of the row. The boolean values
   * are represented with "1" (meaning true) and "0" meaning false.
   *
   * All the alignment between the columns is done with space characters. The size
   * in characters of each column is calculated as the size of the longest column
   * entry (including type and name) plus one. All the values are right aligned.
   *
   * @param out The stream to output the table
   * @param table The table to output
   */
  void write(std::ostream& out, const Table& table) const;

private:
  std::string m_comment;

};

}
} // end of namespace Euclid

#endif	/* CHTABLE_ASCIIWRITER_H */

