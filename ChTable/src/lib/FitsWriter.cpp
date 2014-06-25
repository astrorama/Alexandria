/** 
 * @file src/lib/FitsWriter.cpp
 * @date April 23, 2014
 * @author Nikolaos Apostolakos
 */

#include "FitsWriterHelper.h"
#include "ChTable/FitsWriter.h"
#include "ElementsKernel/ElementsException.h"

namespace ChTable {

FitsWriter::FitsWriter(Format format) : m_format{format} { }

void FitsWriter::write(CCfits::FITS& fits, const std::string& hdu_name, const Table& table) const {
  auto column_info = table.getColumnInfo();
  std::vector<std::string> column_name_list {};
  std::vector<std::string> column_unit_list {};
  for (size_t column_index=0; column_index<column_info->size(); ++column_index) {
    column_name_list.push_back(column_info->getName(column_index));
    column_unit_list.push_back("");
  }
  std::vector<std::string> column_format_list = (m_format == Format::BINARY)
                                              ? getBinaryFormatList(table)
                                              : getAsciiFormatList(table);
  CCfits::HduType hdu_type = (m_format == Format::BINARY)
                           ? CCfits::HduType::BinaryTbl 
                           : CCfits::HduType::AsciiTbl;
  CCfits::Table* table_hdu = fits.addTable(hdu_name, table.size(), column_name_list,
                                           column_format_list, column_unit_list, hdu_type);
  for (size_t column_index=0; column_index<column_info->size(); ++column_index) {
    populateColumn(table, column_index, table_hdu);
  }
}

}