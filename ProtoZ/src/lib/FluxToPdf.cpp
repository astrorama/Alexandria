/**
 * @file FluxToPdf.cpp
 * @date Dec 12, 2013
 * @author dubath
 */
#include "ProtoZ/FluxToPdf.h"
#include "ProtoZ/FluxModeling.h"
#include <algorithm>

FluxToPdf::FluxToPdf(std::string& filename) :
      m_flux_matrix(filename) {

    m_sed_axis = m_flux_matrix.getSedAxis();
    m_ebv_axis = m_flux_matrix.getEbvAxis();
    m_ext_law_axis = m_flux_matrix.getExtLawAxis();
    m_z_axis = m_flux_matrix.getZAxis();
    m_filter_axis = m_flux_matrix.getFilterAxis();

  }

FluxToPdf::FluxToPdf(ProtoZ::matrix::FluxMatrix& flux_matrix) :
     m_flux_matrix(std::move(flux_matrix)) {

   m_sed_axis = m_flux_matrix.getSedAxis();
   m_ebv_axis = m_flux_matrix.getEbvAxis();
   m_ext_law_axis = m_flux_matrix.getExtLawAxis();
   m_z_axis = m_flux_matrix.getZAxis();
   m_filter_axis = m_flux_matrix.getFilterAxis();

 }


FluxToPdf::~FluxToPdf() {
  // TODO Auto-generated destructor stub
}

std::vector<double> FluxToPdf::marginalizePdf(ProtoZ::matrix::PdfMatrix& pdf_matrix) {
  std::vector<double> resultVector {};

  //ToDo add the Probabilty vectors
  double P_EBMV, P_EXT_LAW, P_SED; // Prior probalities
  P_EBMV = P_EXT_LAW = P_SED = 1.;

  for (uint32_t zIndex = 0; zIndex < m_z_axis.size(); zIndex++) {
    double pdf_z{};
    for (uint32_t sedIndex = 0; sedIndex < m_sed_axis.size(); sedIndex++) {
      double pdf_z_sed{};
      for (uint32_t extLawIndex = 0; extLawIndex < m_ext_law_axis.size(); extLawIndex++) {
        double pdf_z_sed_extlaw{};
        for (uint32_t ebvIndex = 0; ebvIndex < m_ebv_axis.size(); ebvIndex++) {
          pdf_z_sed_extlaw += (P_EBMV * pdf_matrix.getValue(sedIndex, ebvIndex, extLawIndex, zIndex));
        } // Eof ebvIndex
        pdf_z_sed += (P_EXT_LAW * pdf_z_sed_extlaw);
      } // Eof extLawIndex
      pdf_z += (P_SED * pdf_z_sed);
    } //Eof sedIndex
    resultVector.push_back(pdf_z);
  } // Eof zIndex

  return resultVector;
}

// Derive the most likely Z value from the PDF
double FluxToPdf::analyzePdf(ProtoZ::matrix::PdfMatrix& pdf_matrix)
{
  auto resultVector = marginalizePdf(pdf_matrix);

  double z_at_max = m_z_axis.indexToValue(std::distance(resultVector.begin(), max_element(resultVector.begin(), resultVector.end())));

  return (z_at_max);
}

std::tuple<SedNames, double, std::string, double, double> FluxToPdf::getMax(
    ProtoZ::matrix::PdfMatrix& pdf_matrix) {

  SedNames sedName { };
  double ebv { };
  std::string extLaw { };
  double redshift { };
  double max = 0.0;

  for (uint32_t iSed = 0; iSed < m_sed_axis.size(); ++iSed) {
    for (uint32_t iEbv = 0; iEbv < m_ebv_axis.size(); ++iEbv) {
      for (uint32_t iExtLaw = 0; iExtLaw < m_ext_law_axis.size(); ++iExtLaw) {
        for (uint32_t iZ = 0; iZ < m_z_axis.size(); ++iZ) {

          if (max < pdf_matrix.getValue(iSed, iEbv, iExtLaw, iZ)) {
            max = pdf_matrix.getValue(iSed, iEbv, iExtLaw, iZ);
            sedName = m_sed_axis.indexToValue(iSed);
            ebv = m_ebv_axis.indexToValue(iEbv);
            extLaw = m_ext_law_axis.indexToValue(iExtLaw);
            redshift = m_z_axis.indexToValue(iZ);
          }

        }
      }
    }
  }
  return std::make_tuple(sedName, ebv, extLaw, redshift, max);
}

double FluxToPdf::getValCalc(PhotometryTypes photometry_type, double f_calc) {
  double val_calc { };
  if (photometry_type == PhotometryTypes::AB_MAGNITUDE) {
    val_calc = -2.5 * std::log10(f_calc) - 48.6;
  } else if (photometry_type == PhotometryTypes::FLUX) {
    val_calc = pow(10.0, 13.0) * f_calc;
  }
  return val_calc;
}

double FluxToPdf::filterLoop(ChDataModel::Source& source, uint32_t iSed,
    uint32_t iEbv, uint32_t iExtLaw, uint32_t iZ, double* alpha) {

  double alpha_up { };
  double alpha_down { };
  double chi2 { };

  for (uint32_t iFilter = 0; iFilter < m_filter_axis.size(); ++iFilter) {
    FilterNames filterNames = m_filter_axis.indexToValue(iFilter);
    Photometry photometry = source.getPhotometry(filterNames);
    double val_obs = photometry.getValue();
    double e_obs = photometry.getValueError();

    double f_calc = m_flux_matrix.getValue(iSed, iEbv, iExtLaw, iZ, iFilter);
    double val_calc = getValCalc(
        photometry.getPhotometryType(), f_calc);

    if (alpha == nullptr) {
      alpha_up += (val_calc * val_obs) / std::pow(e_obs, 2);
      alpha_down += std::pow(val_calc, 2) / std::pow(e_obs, 2);
    } else {
      chi2 += std::pow(*alpha * val_calc - val_obs, 2) / std::pow(e_obs, 2);
    }
  }
  if (alpha == nullptr) {
    return alpha_up / alpha_down;
  } else {
    return chi2;
  }
}

ProtoZ::matrix::PdfMatrix FluxToPdf::compute(ChDataModel::Source& source) {

  ProtoZ::matrix::PdfMatrix pdf_matrix { m_flux_matrix };

  for (uint32_t iSed = 0; iSed < m_sed_axis.size(); ++iSed) {
    for (uint32_t iEbv = 0; iEbv < m_ebv_axis.size(); ++iEbv) {
      for (uint32_t iExtLaw = 0; iExtLaw < m_ext_law_axis.size(); ++iExtLaw) {
        for (uint32_t iZ = 0; iZ < m_z_axis.size(); ++iZ) {

          double alpha = filterLoop(source, iSed, iEbv, iExtLaw, iZ, nullptr);

          double chi2 = filterLoop(source, iSed, iEbv, iExtLaw, iZ, &alpha);

          pdf_matrix.setValue(iSed, iEbv, iExtLaw, iZ, exp(-1 * chi2 / 2));
        }
      }
    }
  }
  return pdf_matrix;
}

/**
 * @brief
 * @details
 * @param
 * @return
 */
std::vector<ProtoZ::matrix::PdfMatrix> FluxToPdf::process(Catalog & catalog) {

  std::vector<ProtoZ::matrix::PdfMatrix> pdf_vector { };

  std::map<int64_t, Source> source_map = catalog.getSourceMap();

  for (auto source : source_map) {
    pdf_vector.push_back(this->compute(source.second));
  }
  return pdf_vector;
}
