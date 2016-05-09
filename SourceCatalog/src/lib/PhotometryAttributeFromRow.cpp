/**
 * @file src/lib/PhotometryAttributeFromRow.cpp
 *
 * @date Apr 17, 2014
 * @author dubath
 */

#include <typeindex>
#include "ElementsKernel/Real.h"
#include "SourceCatalog/SourceAttributes/PhotometryAttributeFromRow.h"
#include "ElementsKernel/Exception.h"
#include "ElementsKernel/Real.h"
#include "Table/CastVisitor.h"

using namespace std;

namespace Euclid {
namespace SourceCatalog {

PhotometryAttributeFromRow::PhotometryAttributeFromRow(
    std::shared_ptr<Euclid::Table::ColumnInfo> column_info_ptr,
    const vector<pair<string, std::pair<string, string>>>& filter_name_mapping,
    const double missing_photometry_flag) :
    m_missing_photometry_flag(missing_photometry_flag) {

  unique_ptr<size_t> flux_column_index_ptr;
  unique_ptr<size_t> error_column_index_ptr;

  for (auto filter_name_pair : filter_name_mapping) {
    flux_column_index_ptr = column_info_ptr->find(filter_name_pair.second.first);
    error_column_index_ptr = column_info_ptr->find(filter_name_pair.second.second);

    if (flux_column_index_ptr == nullptr) {
      throw Elements::Exception() << "Column info does not have the flux column "
                                  << filter_name_pair.second.first;
    }
    if (error_column_index_ptr == nullptr) {
      throw Elements::Exception() << "Column info does not have the flux error column "
                                  << filter_name_pair.second.second;
    }
    m_table_index_vector.push_back(make_pair(*(flux_column_index_ptr), *(error_column_index_ptr)));
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
    const Euclid::Table::Row& row) {

  vector<FluxErrorPair> photometry_vector {};

  for (auto& filter_index_pair : m_table_index_vector) {
    Euclid::Table::Row::cell_type flux_cell = row[filter_index_pair.first];
    Euclid::Table::Row::cell_type error_cell = row[filter_index_pair.second];

    double flux = boost::apply_visitor(Table::CastVisitor<double>{}, flux_cell);
    double error = boost::apply_visitor(Table::CastVisitor<double>{}, error_cell);
    bool missing_data = Elements::isEqual(flux, m_missing_photometry_flag);
    bool upper_limit = error < 0;
    error = std::abs(error);
    
    photometry_vector.push_back(FluxErrorPair{flux, error, missing_data, upper_limit});
  }//Eof for

  unique_ptr<Attribute> photometry_ptr { new Photometry{m_filter_name_vector_ptr, photometry_vector } };

  return move(photometry_ptr);
}

} // namespace SourceCatalog
} // end of namespace Euclid

