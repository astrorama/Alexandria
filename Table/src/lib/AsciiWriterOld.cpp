/** 
 * @file src/lib/AsciiWriter.cpp
 * @date April 16, 2014
 * @author Nikolaos Apostolakos
 */

#include <utility>
#include <iomanip>
#include <boost/lexical_cast.hpp>
#include "ElementsKernel/Exception.h"
#include "Table/AsciiWriterOld.h"
#include "AsciiWriterHelper.h"

namespace Euclid {
namespace Table {

AsciiWriterOld::AsciiWriterOld(std::string comment) : m_comment{std::move(comment)} {
  if (m_comment.empty()) {
    throw Elements::Exception() << "Empty string as comment indicator";
  }
}

void AsciiWriterOld::write(std::ostream& out, const Table& table,
        const std::vector<std::string>& comments, bool show_column_info) const {
  
  // Write the comments
  if (!comments.empty()) {
    for (auto& c : comments) {
      out << m_comment << ' ' << c << '\n';
    }
    out << '\n';
  }
  
  // Write the column descriptions
  auto column_info = table.getColumnInfo();
  if (show_column_info) {
    for (size_t i=0; i<column_info->size(); ++i) {
      auto& info = column_info->getDescription(i);
      out << m_comment << " Column: " << info.name << ' ' << typeToKeyword(info.type);
      if (!info.unit.empty()) {
        out << " (" << info.unit << ")";
      }
      if (!info.description.empty()) {
        out << " - " << info.description;
      }
      out << '\n';
    }
    out << '\n';
  }
  
  
  auto column_lengths = calculateColumnLengths(table);
  // Write the column names
  out << m_comment.c_str();
  for (size_t i=0; i<column_info->size(); ++i) {
    out << std::setw(column_lengths[i]) << column_info->getDescription(i).name;
  }
  out << "\n\n";

  // Write the data
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