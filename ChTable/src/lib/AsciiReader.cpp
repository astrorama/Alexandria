/** 
 * @file AsciiReader.cpp
 * @date April 11, 2014
 * @author Nikolaos Apostolakos
 */

#include <utility>
#include <set>
// The std regex library is not fully implemented in GCC 4.8. The following lines
// make use of the BOOST library and can be modified if GCC 4.9 will be used in
// the future.
// #include <regex>
#include <boost/regex.hpp>
using boost::regex;
using boost::regex_match;
#include <boost/algorithm/string.hpp>
#include "ElementsKernel/ElementsException.h"
#include "ChTable/AsciiReader.h"
#include "AsciiReaderHelper.h"

namespace ChTable {

AsciiReader::AsciiReader(std::vector<std::type_index> column_types,
                         std::vector<std::string> column_names, std::string comment)
                : m_column_types{std::move(column_types)},
                  m_column_names{std::move(column_names)},
                  m_comment{std::move(comment)} {
  if (m_comment.empty()) {
    throw ElementsException() << "Empty string as comment indicator";
  }
  std::set<std::string> set {};
  regex whitespace {".*\\s.*"}; // Checks if input contains any whitespace characters
  for (const auto& name : m_column_names) {
    if (name.empty()) {
      throw ElementsException() << "Empty string column names are not allowed";
    }
    if (regex_match(name, whitespace)) {
      throw ElementsException() << "Column name '" << name << "' contains "
                                << "whitespace characters";
    }
    if (!set.insert(name).second) {  // Check for duplicate names
      throw ElementsException() << "Duplicate column name " << name;
    }
  }
  if (!m_column_names.empty() && !m_column_types.empty()
      && m_column_names.size() != m_column_types.size()) {
    throw ElementsException() << "Different number of column names and types";
  }
}

const Table AsciiReader::read(std::istream& in) const {
  size_t columns_number = countColumns(in, m_comment);
  std::vector<std::string> names {};
  if (m_column_names.empty()) {
    names = autoDetectColumnNames(in, m_comment, columns_number);
  } else if (m_column_names.size() != columns_number) {
      throw ElementsException() << "Columns number in stream (" << columns_number
                                << ") does not match the column names number ("
                                << m_column_names.size() << ")";
  } else {
    names = m_column_names;
  }
  std::vector<std::type_index> types {};
  if (m_column_types.empty()) {
    types = autoDetectColumnTypes(in, m_comment, columns_number);
  } else if (m_column_types.size() != columns_number) {
      throw ElementsException() << "Columns number in stream (" << columns_number
                                << ") does not match the column types number ("
                                << m_column_types.size() << ")";
  } else {
    types = m_column_types;
  }
  auto column_info = createColumnInfo(names, types);
  
  std::vector<Row> row_list;
  regex column_separator {"\\s+"};
  while (in) {
    std::string line;
    getline(in, line);
    size_t comment_pos = line.find(m_comment);
    if (comment_pos != std::string::npos) {
      line = line.substr(0, comment_pos);
    }
    boost::trim(line);
    if (!line.empty()) {
      boost::sregex_token_iterator i (line.begin(), line.end(), column_separator, -1);
      boost::sregex_token_iterator j;
      size_t count {0};
      std::vector<Row::cell_type> values {};
      while (i != j) {
        if (count >= types.size()) {
          throw ElementsException() << "Line with wrong number of cells: " << line;
        }
        values.push_back(convertToCellType(*i, types[count]));
        ++count;
        ++i;
      }
      row_list.push_back(Row{std::move(values), column_info});
    }
  }
  return Table{std::move(row_list)}; 
}

}