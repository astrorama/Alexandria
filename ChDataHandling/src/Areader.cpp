/**
 * Areader.cpp
 *
 *  Created on: Dec 26, 2013
 *      Author: dubath
 */
#include "ChDataHandling/Areader.h"

Areader::Areader() {
  // TODO Auto-generated constructor stub

}

Areader::~Areader() {
  // TODO Auto-generated destructor stub
}

std::vector<vector<string>> Areader::readFile(string file_name, size_t start_line,
    size_t line_number) {

  size_t line_index {};
  std::string line {};
  vector<string> line_fields {};
  std::vector<vector<string>> file_fields {};

  ifstream myfile {};
  myfile.open(file_name);
  if (myfile.is_open()) {
    while (line_index < start_line) {
      getline(myfile, line);
      ++line_index;
    }
    while (!myfile.eof() && line_number > 0) {
      getline(myfile, line);
      boost::split(line_fields, line, boost::is_any_of(", "));
      file_fields.push_back(line_fields);
      --line_number;
    }
    myfile.close();
  } else {
    stringstream errorBuffer;
       errorBuffer << "Areader: The file " << file_name
           << " cannot be opened" << endl;
       throw ElementsException(errorBuffer.str());
  }
  return file_fields;
}

void Areader::AddSourceToCatalog(ChDataModel::Catalog& catalog, vector<string> source_data) {

  int64_t source_id {std::stoi(source_data.at(m_source_id_index))};
  ChDataModel::Source source {source_id, 0.0, 0.0};

  for( auto ii=m_filter_map.begin(); ii!=m_filter_map.end(); ++ii)
  {
    ChDataModel::Photometry photometry {&source, (*ii).first, m_photometry_types,
      std::stod(source_data.at( (*ii).second ) ),
      std::stod(source_data.at( (*ii).second + m_error_col_offset) ) };
    source.addPhotometry(photometry);
  }
  source.setSpecZ(std::stod(source_data.at(m_spectro_z_index)));
  source.setAgnFlag(std::stod(source_data.at(m_spectro_z_index)));
  catalog.addSource(source);
}

ChDataModel::Catalog Areader::getCatalog(std::string path, size_t line_start, size_t line_number) {

  std::vector<vector<string>> file_fields = this->readFile(path, line_start, line_number);

    ChDataModel::Survey survey {ChDataModel::SurveyNames::EUCLID};
    ChDataModel::Catalog catalog = survey.createCatalog();

    for (vector<string> line : file_fields) {
      this->AddSourceToCatalog(catalog, line);
    }
  return catalog;
}

void Areader::writeAsciiFile(std::vector<string> data, string file_name) {

   ofstream myfile (file_name);
   if (myfile.is_open()) {
     for(string line : data) {

       myfile << line << "\n";
     }
     myfile.close();
   } else {
   stringstream errorBuffer;
      errorBuffer << "Areader: The file " << file_name
          << " cannot be opened for writting" << endl;
      throw ElementsException(errorBuffer.str());
   }
 }

