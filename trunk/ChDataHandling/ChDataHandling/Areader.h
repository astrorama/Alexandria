/**
 * Areader.h
 *
 *  Created on: Dec 26, 2013
 *      Author: dubath
 */
#ifndef AREADER_H_
#define AREADER_H_

#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <boost/algorithm/string.hpp>

#include "ChDataModel/Catalog.h"
#include "ChDataModel/Source.h"
#include "ChDataModel/Survey.h"
#include "ChDataModel/Photometry.h"
#include "ChDataModel/Enumerations/FilterNames.h"
#include "ChDataModel/Enumerations/SurveyNames.h"
#include "ChDataModel/Enumerations/PhotometryTypes.h"

using namespace std;

class Areader {
public:
  Areader();
  virtual ~Areader();

  std::vector<vector<string>> readFile(string file_name, size_t start_line,
      size_t line_number);

  void AddSourceToCatalog(ChDataModel::Catalog& catalog,
      vector<string> source_data);

  ChDataModel::Catalog getCatalog(std::string path, size_t line_start,
      size_t line_number);

  void writeAsciiFile(std::vector<string> data, string file_name);


private:

  size_t m_source_id_index = 0;
  ChDataModel::PhotometryTypes m_photometry_types =
      ChDataModel::PhotometryTypes::FLUX;

  map<ChDataModel::FilterNames, size_t> m_filter_map { {
      ChDataModel::FilterNames::Zext_ACSf850lp, 5 }, {
      ChDataModel::FilterNames::Ynir_WFC3f105w, 6 }, {
      ChDataModel::FilterNames::VIS_ACSf814w, 4 }, {
      ChDataModel::FilterNames::Rext_ACSf606w, 2 }, {
      ChDataModel::FilterNames::Jnir_WFC3f125w, 7 }, {
      ChDataModel::FilterNames::Iext_ACSf775w, 3 }, {
      ChDataModel::FilterNames::Hnir_WFC3f160w, 8 }, {
      ChDataModel::FilterNames::Gext_ACSf435w, 1 } };

  size_t m_error_col_offset = 8;

  size_t m_spectro_z_index = 17;

  size_t m_agn_index = 18;

};

#endif /* AREADER_H_ */
