/** 
 * @file src/lib/AsciiWriter.cpp
 * @date April 16, 2014
 * @author Nikolaos Apostolakos
 */

#include <utility>
#include <iomanip>
#include <boost/lexical_cast.hpp>
#include "ElementsKernel/Exception.h"
#include "Table/AsciiWriter.h"
#include "AsciiWriterHelper.h"

namespace Euclid {
namespace Table {

AsciiWriter::AsciiWriter(std::string comment) : m_comment{std::move(comment)} {
  if (m_comment.empty()) {
    throw Elements::Exception() << "Empty string as comment indicator";
  }
}

void AsciiWriter::write(std::ostream& out, const Table& table, bool types) const {
  auto column_lengths = calculateColumnLengths(table);
  auto column_info = table.getColumnInfo();
  // Write the column names
  out << m_comment.c_str();
  for (size_t i=0; i<column_info->size(); ++i) {
    out << std::setw(column_lengths[i]) << column_info->getName(i);
  }
  out << "\n";
  // Write the column types
  if (types) {
    out << m_comment.c_str();
    for (size_t i=0; i<column_info->size(); ++i) {
      out << std::setw(column_lengths[i]) << typeToKeyword(column_info->getType(i));
    }
    out << "\n";
  }
  out << "\n";
  // The data lines are not prefixed with the comment string, so we need to fix
  // the length of the first column to get the alignment correctly
  column_lengths[0] = column_lengths[0] + m_comment.size();
  for (auto row : table) {
    for (size_t i=0; i<row.size(); ++i) {
      out << std::setw(column_lengths[i]) << boost::lexical_cast<std::string>(row[i]);
    }
    out << "\n";
  }
}

}
} // end of namespace Euclid