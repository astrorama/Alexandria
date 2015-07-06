/*
 * LuminosityCorrection.cpp
 *
 *  Created on: Jul 6, 2015
 *      Author: fdubath
 */

#include "SourceCatalog/SourceAttributes/LuminosityCorrection.h"



namespace Euclid {
namespace SourceCatalog {
  LuminosityCorrection::LuminosityCorrection(const std::string& reference_filter,
      const std::string& measurement_filter,
      double correction_value):m_reference_filter{reference_filter},
      m_measurement_filter{measurement_filter},
      m_correction_value{correction_value}{}

  void LuminosityCorrection::setReferenceFilter(const std::string& reference_filter){
    m_reference_filter=reference_filter;
  }

  void LuminosityCorrection::setMeasurementFilter(const std::string& measurement_filter){
    m_measurement_filter=measurement_filter;
  }

  void LuminosityCorrection::setCorrection(double correction_value){
    m_correction_value=correction_value;
  }

  std::string LuminosityCorrection::getReferenceFilter() const{
    return m_reference_filter;
  }

  std::string LuminosityCorrection::getMeasurementFilter() const{
    return m_measurement_filter;
  }

  double LuminosityCorrection::getCorrection() const{
    return m_correction_value;
  }

}
}


