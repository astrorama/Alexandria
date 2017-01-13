/**
 * @file Table/AsciiReader.h
 * @date April 11, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef TABLE_ASCII_READER_H
#define	TABLE_ASCII_READER_H

#include <istream>
#include <vector>
#include <string>
#include <typeindex>

#include "ElementsKernel/Export.h"

#include "Table/Table.h"

namespace Euclid {
namespace Table {

/**
 * @class AsciiReader
 *
 * @brief Tool for reading ASCII tables from streams
 *
 * @details
 * The AsciiReader class is a tool for creating Table objects from input streams. It
 * can be parameterised with the arguments of its constructor (to provide support
 * for more than one format of files) and it provides read() methods for reading
 * the tables.
 */
class ELEMENTS_API AsciiReader {

public:

  /**
   * @brief
   * Constructs a new AsciiReader with the given parameters
   * @details
   * The given file can contain in its comments (before the data starts) the
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
   * with the column names are missing, the columns  are named with an increasing
   * counter as "col1", "col2", etc (starting from 1).
   * 
   * If the column names comment is present, the column descriptions can be missing
   * and be given in any order.
   * 
   * The above automatic detection of the names and types of the columns can be
   * overridden by used defined values, given as constructor parameters (empty
   * vectors enable the automatic detection).
   * 
   * Note that the vector entries are values separated by "," (no spaces).
   * 
   * @param column_types The types of the columns or empty for auto-detection (default)
   * @param column_names The names of the columns or empty for auto-detection (default)
   * @param comment The sequence of characters to mark the beginning of a comment (defaults to "#")
   * @throws Elements::Exception
   *    if the comment string is the empty string
   * @throws Elements::Exception
   *    if there are duplicate column names
   * @throws Elements::Exception
   *    if any of the given column names is empty or contains whitespace characters
   * @throws Elements::Exception
   *    if none of column_types and column_names are set for auto-detection and
   *    they have different size
   */
  AsciiReader(std::vector<std::type_index> column_types = {},
              std::vector<std::string> column_names = {},
              std::string comment = "#");

  /// Default destructor
  virtual ~AsciiReader() = default;

  /**
   * @brief
   * Reads a Table from the given stream
   * @details
   * The stream is red line by line and one row is created for each line which,
   * after comments are removed, does not contain only whitespace characters.
   * The columns are separated by one or more whitespace characters and all rows
   * must have the same number of columns.
   *
   * The names and types of the columns are handled according the configuration
   * given to the AsciiReader constructor (see the constructor for details).
   *
   * The table is populated until the end of the stream is reached.
   *
   * @param in the stream to read the table from
   * @return the table
   * @throws Elements::Exception
   *    if the stream does not contain any non comment lines
   * @throws Elements::Exception
   *    if column names are given to the constructor and the stream contains
   *    data with different number of columns
   * @throws Elements::Exception
   *    if column types are given to the constructor and the stream contains
   *    data with different number of columns
   * @throws Elements::Exception
   *    if the stream contains lines with different number of columns
   * @throws Elements::Exception
   *    if column name auto-detection is enabled and there are duplicate names
   * @throws Elements::Exception
   *    if any cell cannot be converted to the correct type
   */
  const Table read(std::istream& in) const;

private:
  std::vector<std::type_index> m_column_types;
  std::vector<std::string> m_column_names;
  std::string m_comment;

};

}
} // end of namespace Euclid

#endif	/* TABLE_ASCII_READER_H */

