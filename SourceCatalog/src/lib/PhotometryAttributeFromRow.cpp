/**
 * @file src/lib/PhotometryAttributeFromRow.cpp
 *
 * @date Apr 17, 2014
 * @author dubath
 */

#include <typeindex>
#include <cmath>
#include "ElementsKernel/Real.h"
#include "SourceCatalog/SourceAttributes/PhotometryAttributeFromRow.h"
#include "ElementsKernel/Exception.h"
#include "ElementsKernel/Real.h"
#include "Table/CastVisitor.h"
#include "SourceCatalog/LuminosityParsingException.h"


using namespace std;

namespace Euclid {
namespace SourceCatalog {

PhotometryAttributeFromRow::PhotometryAttributeFromRow(
    std::shared_ptr<Euclid::Table::ColumnInfo> column_info_ptr,
    const vector<pair<string, std::pair<string, string>>>& filter_name_mapping,
    const bool has_missing_photometry,
    const double missing_photometry_flag,
    const bool has_upper_limit) :
    m_has_missing_photometry(has_missing_photometry),
    m_missing_photometry_flag(missing_photometry_flag),
    m_has_upper_limit(has_upper_limit){

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

    bool missing_data = false;
    bool upper_limit = false;
    if (std::isinf(flux)){
            throw SourceCatalog::LuminosityParsingException(
                               "Infinite  flux encountered when parsing the luminosity",
                               flux,
                               error);
    }
    if (m_has_missing_photometry) {
      /** Missing photometry enabled **/
      missing_data = Elements::isEqual(flux, m_missing_photometry_flag) || std::isnan(flux);
      if (missing_data){
        error=0;
      } else {
        if (m_has_upper_limit) {
          /** Upper limit enabled **/
          if (Elements::isEqual(error,0.)){
                     throw SourceCatalog::LuminosityParsingException(
                               "Zero error encountered when parsing the luminosity with 'missing data' and 'upper limit' enabled",
                               flux,
                               error);
                         }
                 if (error<0){
                   /** Actual upper limit **/
                   upper_limit=true;
                   if (flux<=0){
                             throw SourceCatalog::LuminosityParsingException(
                                 "Negative or Zero flux encountered when parsing the luminosity in the context of an 'upper limit'",
                                 flux,
                                 error);
                           }
                   error=std::abs(error);
                   }

        } else {
          /** Upper limit disabled **/
          if (error<=0){
            throw SourceCatalog::LuminosityParsingException(
                                  "Negative or Zero error encountered when parsing the luminosity with 'missing data' enabled and 'upper limit' disabled",
                                  flux,
                                  error);
                            }
          }

        }
    } else {

      /** Missing photometry disabled **/
      if (std::isnan(flux)){
                throw SourceCatalog::LuminosityParsingException(
                    "NAN flux encountered when parsing the luminosity with 'missing data' disabled",
                    flux,
                    error);
      }

      if (m_has_upper_limit) {
        /** Upper limit enabled **/
        if (Elements::isEqual(error,0.)){
            throw SourceCatalog::LuminosityParsingException(
                      "Zero error encountered when parsing the luminosity with 'missing data' disabled and 'upper limit' enabled",
                      flux,
                      error);
                }
        if (error<0){
          /** Actual upper limit **/
          upper_limit=true;
          if (flux<=0){
                    throw SourceCatalog::LuminosityParsingException(
                        "Negative or Zero flux encountered when parsing the luminosity in the context of an 'upper limit'",
                        flux,
                        error);
                  }
          error=std::abs(error);

        }

      } else {
        /** Upper limit disabled **/
        if (error<=0){
          throw SourceCatalog::LuminosityParsingException(
              "Negative or Zero error encountered when parsing the luminosity with 'missing data' and 'upper limit' disabled",
              flux,
              error);
        }
      }
    }




    photometry_vector.push_back(FluxErrorPair{flux, error, missing_data, upper_limit});
  }//Eof for

  unique_ptr<Attribute> photometry_ptr { new Photometry{m_filter_name_vector_ptr, photometry_vector } };

  return move(photometry_ptr);
}

} // namespace SourceCatalog
} // end of namespace Euclid

