/**
 * @file PhotometryAttributeHandler.cpp
 *
 * @date Apr 17, 2014
 * @author dubath
 */

#include <typeindex>
#include "ChCatalog/SourceAttributes/PhotometryAttributeHandler.h"
#include "ElementsKernel/ElementsException.h"

using namespace std;

namespace ChCatalog {

PhotometryAttributeHandler::PhotometryAttributeHandler(
    const ChTable::ColumnInfo column_info,
    const map<FilterName, std::pair<string, string>> filter_name_mapping) {
  // @todo Auto-generated constructor stub

  unique_ptr<size_t> flux_column_index_ptr;
  unique_ptr<size_t> error_column_index_ptr;

  for (auto filter_name_pair : filter_name_mapping) {
    flux_column_index_ptr = column_info.find(
        filter_name_pair.second.first);
    error_column_index_ptr = column_info.find(
        filter_name_pair.second.second);

    if (flux_column_index_ptr == nullptr || type_index(typeid(double)) != column_info.getType(*(flux_column_index_ptr)) ) {
      throw ElementsException() << "Column info does not have the expected flux column of double type";
    }
    if (error_column_index_ptr == nullptr || type_index(typeid(double)) != column_info.getType(*(error_column_index_ptr)) ) {
      throw ElementsException() << "Column info does not have the expected flux column of double type";
    }
    m_filter_index_mapping.emplace(filter_name_pair.first,
        make_pair(*(flux_column_index_ptr), *(error_column_index_ptr)));
  }
}

PhotometryAttributeHandler::~PhotometryAttributeHandler() {
  // @todo Auto-generated destructor stub
}

unique_ptr<Attribute> PhotometryAttributeHandler::createAttribute(
    const ChTable::Row& row) {

  map<FilterName, pair<double, double>> photometry_map;
  ChTable::Row::cell_type flux_cell;
  ChTable::Row::cell_type error_cell;

  for (auto filter_index_pair : m_filter_index_mapping) {
    flux_cell = row[filter_index_pair.second.first];
    error_cell = row[filter_index_pair.second.second];
    photometry_map[filter_index_pair.first] = make_pair(
        boost::get<double>(flux_cell), boost::get<double>(error_cell));
  }
  unique_ptr<Attribute> photometry_ptr(new Photometry(photometry_map));
  return photometry_ptr;
}

} // namespace ChCatalog

