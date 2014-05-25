/**
 * @file PhotometryAttributeHandler.cpp
 *
 * @date Apr 17, 2014
 * @author dubath
 */

#include <typeindex>
#include "ChCatalog/SourceAttributes/PhotometryAttributeFromRow.h"
#include "ElementsKernel/ElementsException.h"

using namespace std;

namespace ChCatalog {

PhotometryAttributeFromRow::PhotometryAttributeFromRow(
    std::shared_ptr<ChTable::ColumnInfo> column_info_ptr,
    const map<string, std::pair<string, string>> filter_name_mapping) {

  unique_ptr<size_t> flux_column_index_ptr;
  unique_ptr<size_t> error_column_index_ptr;

  for (auto filter_name_pair : filter_name_mapping) {
    flux_column_index_ptr = column_info_ptr->find(
        filter_name_pair.second.first);
    error_column_index_ptr = column_info_ptr->find(
        filter_name_pair.second.second);

    if (flux_column_index_ptr == nullptr || type_index(typeid(double)) != column_info_ptr->getType(*(flux_column_index_ptr)) ) {
      throw ElementsException() << "Column info does not have the expected flux column of double type";
    }
    if (error_column_index_ptr == nullptr || type_index(typeid(double)) != column_info_ptr->getType(*(error_column_index_ptr)) ) {
      throw ElementsException() << "Column info does not have the expected flux column of double type";
    }
    m_filter_index_mapping.emplace(filter_name_pair.first,
        make_pair(*(flux_column_index_ptr), *(error_column_index_ptr)));
  }

  // create and filled the shared pointer to the filter name vector
   m_filter_name_vector_ptr = shared_ptr<vector<string>>{new vector<string>{} };
  for(auto a_filter_name_map: filter_name_mapping) {
    m_filter_name_vector_ptr->push_back(a_filter_name_map.first);
  }

}

PhotometryAttributeFromRow::~PhotometryAttributeFromRow() {
  // @todo Auto-generated destructor stub
}

unique_ptr<Attribute> PhotometryAttributeFromRow::createAttribute(
    const ChTable::Row& row) {

  vector<FluxErrorPair> photometry_vector;
  ChTable::Row::cell_type flux_cell;
  ChTable::Row::cell_type error_cell;

  for (auto& filter_index_pair : m_filter_index_mapping) {
    flux_cell = row[filter_index_pair.second.first];
    error_cell = row[filter_index_pair.second.second];
    photometry_vector.push_back(FluxErrorPair {boost::get<double>(flux_cell), boost::get<double>(error_cell) } );
  }

  unique_ptr<Attribute> photometry_ptr { new Photometry{m_filter_name_vector_ptr, photometry_vector } };

  return move(photometry_ptr);
}

} // namespace ChCatalog

