/**
 * @file Table/AsciiWriter.h
 * @date April 16, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef TABLE_ASCIIWRITER_H
#define	TABLE_ASCIIWRITER_H

#include <string>
#include <ostream>

#include "ElementsKernel/Export.h"

#include "Table/Table.h"

namespace Euclid {
namespace Table {

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
   * @throws Elements::Exception
   *    if the comment string is the empty string
   */
  AsciiWriter(std::string comment = "#");

  /// Default destructor
  virtual ~AsciiWriter() = default;

  /**
   * @brief
   * Writes a Table in the given stream
   * @details
   * The file starts with all the given comments, with one comment per line. The
   * comments are followed by one empty line. After that, the first row written
   * is a comment line containing the names of the columns, as described by the
   * ColumnInfo of the table. The next (optional) row is a comment containing
   * the types of the columns. The strings used are:
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
   * An empty line follows these two lines and then one line is written for each
   * Row of the table, which contains the values of the row. The boolean values
   * are represented with "1" (meaning true) and "0" meaning false. The vector
   * values are separated by ",".
   *
   * All the alignment between the columns is done with space characters. The size
   * in characters of each column is calculated as the size of the longest column
   * entry (including type and name) plus one. All the values are right aligned.
   *
   * @param out The stream to output the table
   * @param table The table to output
   * @param comments The comments to add at the beginning of the file
   * @param types A flag to write the types line or not
   */
  void write(std::ostream& out, const Table& table, const std::vector<std::string>& comments={}, bool types=true) const;

private:
  std::string m_comment;

};

}
} // end of namespace Euclid

#endif	/* TABLE_ASCIIWRITER_H */

