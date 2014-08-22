/** 
 * @file src/lib/FitsReader.cpp
 * @date April 17, 2014
 * @author Nikolaos Apostolakos
 */

#include <set>
#include <boost/regex.hpp>
#include <CCfits/CCfits>
using boost::regex;
using boost::regex_match;
#include "ElementsKernel/ElementsException.h"
#include "ChTable/Row.h"
#include "ChTable/FitsReader.h"
#include "ReaderHelper.h"
#include "FitsReaderHelper.h"

namespace Euclid {
namespace ChTable {

FitsReader::FitsReader(std::vector<std::string> column_names)
                : m_column_names{std::move(column_names)} {
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
}

const Euclid::ChTable::Table FitsReader::read(const CCfits::HDU& hdu) {
  // First we check that we have a table HDU
  try {
    dynamic_cast<const CCfits::Table&>(hdu);
  } catch (std::bad_cast&) {
    throw ElementsException() << "Given HDU is not a table";
  }
  const CCfits::Table& table_hdu = dynamic_cast<const CCfits::Table&>(hdu);
  
  std::vector<std::string> names {};
  if (m_column_names.empty()) {
    names = autoDetectColumnNames(table_hdu);
  } else if (m_column_names.size() != static_cast<size_t>(table_hdu.numCols())) {
    throw ElementsException() << "Columns number in HDU (" << table_hdu.numCols()
                              << ") does not match the column names number ("
                              << m_column_names.size() << ")";
  } else {
    names = m_column_names;
  }
  auto column_info = createColumnInfo(names, autoDetectColumnTypes(table_hdu));
  
  // CCfits reads per column, so we first read all the columns and then we
  // create all the rows
  std::vector<std::vector<Row::cell_type>> data;
  for (int i=1; i<=table_hdu.numCols(); ++i) {
    // The i-1 is because CCfits starts from 1 and ColumnInfo from 0
    data.push_back(translateColumn(table_hdu.column(i), column_info->getType(i-1)));
  }
  
  std::vector<Row> row_list;
  for (int i=0; i<table_hdu.rows(); ++i) {
    std::vector<Row::cell_type> cells {};
    for (const auto& column_data : data) {
      cells.push_back(column_data[i]);
    }
    row_list.push_back(Row{cells,column_info});
  }
  
  return Euclid::ChTable::Table{row_list};
}

}
} // end of namespace Euclid