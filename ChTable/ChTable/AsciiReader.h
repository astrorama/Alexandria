/**
 * @file ChTable/AsciiReader.h
 * @date April 11, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef CHTABLE_ASCII_READER_H
#define	CHTABLE_ASCII_READER_H

#include <istream>
#include <vector>
#include <string>
#include <typeindex>

#include "ElementsKernel/Export.h"

#include "ChTable/Table.h"

namespace Euclid {
namespace ChTable {

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
   * The reader will use the column types and names given as parameters and will
   * ignore any configuration in the stream. To enable auto-detection of column
   * names or types based on the comments of the stream, an empty vector should be
   * passed as an argument (which is the default behavior).
   *
   * If auto-detection of column names is enabled, the names of the columns are
   * extracted from the first non empty comment
   * line, which contains the same number of whitespace separated words as the
   * columns of the table. If there is no such comment line, the columns are
   * named with an increasing counter as "col1", "col2", etc (starting from 1).
   * Note that any comment characters are stripped out of the beginning and ending
   * of the names.
   *
   * If auto-detection of column types is enabled, the types are extracted from
   * the first comment line right after the column names comment, which has that
   * many keywords as the number of columns. The available types are:
   *   - bool, boolean : A boolean value as the following (case is ignored):
   *     - true, t, yes, y, 1
   *     - false, f, no, n, 0
   *   - int, int32 : A 32 bit integer
   *   - long, int64 : A 64 bit integer
   *   - float : Single (32 bit) precision floating point
   *   - double : Double (64 bit) precision floating point
   *   - string : String without whitespaces
   *
   * If there is no such line all columns are treated as strings.
   *
   * @param column_types The types of the columns or empty for auto-detection (default)
   * @param column_names The names of the columns or empty for auto-detection (default)
   * @param comment The sequence of characters to mark the beginning of a comment (defaults to "#")
   * @throws ElementsException
   *    if the comment string is the empty string
   * @throws ElementsException
   *    if there are duplicate column names
   * @throws ElementsException
   *    if any of the given column names is empty or contains whitespace characters
   * @throws ElementsException
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
   * @throws ElementsException
   *    if the stream does not contain any non comment lines
   * @throws ElementsException
   *    if column names are given to the constructor and the stream contains
   *    data with different number of columns
   * @throws ElementsException
   *    if column types are given to the constructor and the stream contains
   *    data with different number of columns
   * @throws ElementsException
   *    if the stream contains lines with different number of columns
   * @throws ElementsException
   *    if column name auto-detection is enabled and there are duplicate names
   * @throws ElementsException
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

#endif	/* CHTABLE_ASCII_READER_H */

