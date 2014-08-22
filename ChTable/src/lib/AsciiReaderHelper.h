/**
 * @file src/lib/AsciiReaderHelper.h
 * @date April 15, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef CHTABLE_ASCIIREADERHELPER_H
#define	CHTABLE_ASCIIREADERHELPER_H

#include <istream>
#include <string>
#include <typeindex>


#include "ElementsKernel/Export.h"
#include "ChTable/Row.h"

namespace Euclid {
namespace ChTable {

/**
 * @class StreamRewinder
 *
 * @brief
 * This class gets a stream as argument during construction and when it is deleted
 * it sets the position of the stream back to where it was during the constructor
 * call.
 */
class StreamRewinder {
public:
  StreamRewinder(std::istream& stream) : m_stream(stream), m_position(stream.tellg()) { }
  ~StreamRewinder() {
    m_stream.seekg(m_position);
  }
private:
  std::istream& m_stream;
  int m_position;
};

/**
 * @brief
 * Returns the number of whitespace separated tokens of the first non commented
 * line
 * @details
 * When the method returns the given stream is positioned at the same position
 * like before the method was called.
 *
 * @param in The string to read from
 * @param comment The comment pattern
 * @return The number of columns
 * @throws ElementsException
 *    if there is no uncommented, non-empty line
 */
ELEMENTS_API size_t countColumns(std::istream& in, const std::string& comment);

/**
 * @brief
 * Reads the column names of the given stream
 * @details
 * For more information about the auto-detection rules see the constructor of
 * AsciiReader. When the method returns, the given stream is positioned at the
 * same position like before the method was called.
 *
 * @param in The stream to read the column names from
 * @param comment The comment pattern
 * @param columns_number The number of columns
 * @return The auto-detected names of the columns
 * @throws ElementsException
 *    if there are duplicate column names
 */
ELEMENTS_API std::vector<std::string> autoDetectColumnNames(std::istream& in,
                                               const std::string& comment,
                                               size_t columns_number);

/**
 * @brief
 * Reads the column types of the given stream
 * @details
 * For more information about the auto-detection rules see the constructor of
 * AsciiReader. When the method returns, the given stream is positioned at the
 * same position like before the method was called.
 *
 * @param in The stream to read the column types from
 * @param comment The comment pattern
 * @param columns_number The number of columns
 * @return The auto-detected types of the columns
 * @throws ElementsException
 *    if any of the types is not one of the valid keywords
 */
ELEMENTS_API std::vector<std::type_index> autoDetectColumnTypes(std::istream& in,
                                                   const std::string& comment,
                                                   size_t columns_number);

/**
 * @brief
 * Converts the given value to a Row::cell_type of the given type
 * @details
 * For more information of the supported types see the documentation of the
 * Euclid::ChTable::AsciiReader constructor.
 *
 * @param value The value to convert
 * @param type The type of the cell
 * @return The Row::cell_type representing the value
 * @throws ElementsException
 *    if the conversion fails
 */
ELEMENTS_API Row::cell_type convertToCellType(const std::string& value, std::type_index type);

}
} // end of namespace Euclid

#endif	/* CHTABLE_ASCIIREADERHELPER_H */

