/*
 * LuminosityCorrection.h
 *
 *  Created on: Jul 6, 2015
 *      Author: fdubath
 */

#ifndef SOURCECATALOG_SOURCECATALOG_SOURCEATTRIBUTES_LUMINOSITYCORRECTION_H_
#define SOURCECATALOG_SOURCECATALOG_SOURCEATTRIBUTES_LUMINOSITYCORRECTION_H_
#include <string>
#include "SourceCatalog/Attribute.h"

namespace Euclid {
namespace SourceCatalog {

/**
 * The LuminosityCorrection is designed to store the information required to
 * compute the absolute luminosity from a source assuming the model.
 */
class LuminosityCorrection: public Attribute {
public:
  virtual ~LuminosityCorrection(){}

  LuminosityCorrection(const std::string& reference_filter,
      double correction_value);

  void setReferenceFilter(const std::string& reference_filter);

  void setCorrection(double correction_value);

  std::string getReferenceFilter() const;

  double getCorrection() const;

private:
  std::string m_reference_filter;
  double m_correction_value;

};


}
}


#endif /* SOURCECATALOG_SOURCECATALOG_SOURCEATTRIBUTES_LUMINOSITYCORRECTION_H_ */
