/**
 * @file FluxToPdf.h
 * @date Dec 12, 2013
 * @author Pierre Dubath
 */
#ifndef FLUXTOPDF_H_
#define FLUXTOPDF_H_

#include <string>
#include <vector>
#include <tuple>
#include <memory>
#include <cmath>
#include "ChDataModel/Source.h"
#include "ChDataModel/Catalog.h"
#include "ChDataModel/Enumerations/SedNames.h"
#include "ChDataModel/Enumerations/PhotometryTypes.h"
#include "ChDataModel/Enumerations/FilterNames.h"
#include "ProtoZ/matrix/FluxMatrix.h"
#include "ProtoZ/matrix/PdfMatrix.h"
#include "ProtoZ/matrix/AxisInfo.h"
#include "ProtoZ/parameter/PhzParameter.h"
#include "ProtoZ/parameter/FluxModelingParameters.h"
namespace param = ProtoZ::parameter;
#include "ProtoZ/matrix/MatrixFactory.h"
namespace matrix = ProtoZ::matrix;
using namespace ChDataModel;

class FluxToPdf {
public:
  FluxToPdf(std::string& filename);
  FluxToPdf(ProtoZ::matrix::FluxMatrix& flux_matrix);

  virtual ~FluxToPdf();

  std::tuple<SedNames, double, std::string, double, double> getMax(
      ProtoZ::matrix::PdfMatrix& pdf_matrix);

  double getValCalc(PhotometryTypes photometry_type, double f_calc);

  double filterLoop(ChDataModel::Source& source, uint32_t iSed, uint32_t iEbv,
      uint32_t iExtLaw, uint32_t iZ, double* alpha);

  ProtoZ::matrix::PdfMatrix compute(ChDataModel::Source& source);

  /**
   * @brief
   * @details
   * @param
   * @return
   */
  std::vector<ProtoZ::matrix::PdfMatrix> process(Catalog & catalog);

private:

  ProtoZ::matrix::FluxMatrix m_flux_matrix;

  matrix::AxisInfo<dm::SedNames> m_sed_axis;
  matrix::AxisInfo<double> m_ebv_axis;
  matrix::AxisInfo<std::string> m_ext_law_axis;
  matrix::AxisInfo<double> m_z_axis;
  matrix::AxisInfo<dm::FilterNames> m_filter_axis;

};

#endif /* FLUXTOPDF_H_ */
