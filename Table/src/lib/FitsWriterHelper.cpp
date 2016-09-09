/** 
 * @file src/lib/FitsWriterHelper.cpp
 * @date April 23, 2014
 * @author Nikolaos Apostolakos
 */

#include <algorithm>
#include <sstream>
#include <iomanip>
#include <valarray>
#include <boost/lexical_cast.hpp>
#include <CCfits/CCfits>
#include "FitsWriterHelper.h"
#include "Table/Table.h"
#include "ElementsKernel/Exception.h"

namespace Euclid {
namespace Table {

template<typename T>
std::string scientificFormat(T value) {
  std::ostringstream stream;
  stream << std::scientific << value;
  return stream.str();
}

size_t maxWidth(const Table& table, size_t column_index) {
  size_t width = 0;
  for (const auto& row : table) {
    width = std::max(width, boost::lexical_cast<std::string>(row[column_index]).size());
  }
  return width;
}

size_t maxWidthScientific(const Table& table, size_t column_index) {
  size_t width = 0;
  for (const auto& row : table) {
    width = std::max(width, scientificFormat(row[column_index]).size());
  }
  return width;
}

std::vector<std::string> getAsciiFormatList(const Table& table) {
  auto column_info = table.getColumnInfo();
  std::vector<std::string> format_list {};
  for (size_t column_index=0; column_index<column_info->size(); ++column_index) {
    auto type = column_info->getDescription(column_index).type;
    if (type == typeid(bool)) {
      format_list.push_back("I1");
    } else if (type == typeid(int32_t) || type == typeid(int64_t)) {
      size_t width = maxWidth(table, column_index);
      format_list.push_back("I" + boost::lexical_cast<std::string>(width));
    } else if (type == typeid(float) || type == typeid(double)) {
      size_t width = maxWidthScientific(table, column_index);
      format_list.push_back("E" + boost::lexical_cast<std::string>(width));
    } else if (type == typeid(std::string)) {
      size_t width = maxWidth(table, column_index);
      format_list.push_back("A" + boost::lexical_cast<std::string>(width));
    } else {
      throw Elements::Exception() << "Unsupported column format for FITS ASCII table export: " << type.name();
    }
  }
  return format_list;
}

template <typename T>
size_t vectorSize(const Table& table, size_t column_index) {
  size_t size = boost::get<std::vector<T>>(table[0][column_index]).size();
  for (const auto& row : table) {
    if (boost::get<std::vector<T>>(row[column_index]).size() != size) {
      throw Elements::Exception() << "Bitnary FITS table variable length vector columns are not supported";
    }
  }
  return size;
}

std::vector<std::string> getBinaryFormatList(const Table& table) {
  auto column_info = table.getColumnInfo();
  std::vector<std::string> format_list {};
  for (size_t column_index=0; column_index<column_info->size(); ++column_index) {
    auto type = column_info->getDescription(column_index).type;
    if (type == typeid(bool)) {
      format_list.push_back("L");
    } else if (type == typeid(int32_t)) {
      format_list.push_back("J");
    } else if (type == typeid(int64_t)) {
      format_list.push_back("K");
    } else if (type == typeid(float)) {
      format_list.push_back("E");
    } else if (type == typeid(double)) {
      format_list.push_back("D");
    } else if (type == typeid(std::string)) {
      size_t width = maxWidth(table, column_index);
      format_list.push_back(boost::lexical_cast<std::string>(width) + "A");
    } else if (type == typeid(std::vector<bool>)) {
      size_t size = vectorSize<bool>(table, column_index);
      format_list.push_back(boost::lexical_cast<std::string>(size) + "L");
    } else if (type == typeid(std::vector<int32_t>)) {
      size_t size = vectorSize<int32_t>(table, column_index);
      format_list.push_back(boost::lexical_cast<std::string>(size) + "J");
    } else if (type == typeid(std::vector<int64_t>)) {
      size_t size = vectorSize<int64_t>(table, column_index);
      format_list.push_back(boost::lexical_cast<std::string>(size) + "K");
    } else if (type == typeid(std::vector<float>)) {
      size_t size = vectorSize<float>(table, column_index);
      format_list.push_back(boost::lexical_cast<std::string>(size) + "E");
    } else if (type == typeid(std::vector<double>)) {
      size_t size = vectorSize<double>(table, column_index);
      format_list.push_back(boost::lexical_cast<std::string>(size) + "D");
    } else {
      throw Elements::Exception() << "Unsupported column format for FITS binary table export: " << type.name();
    }
  }
  return format_list;
}

template<typename T>
std::vector<T> createColumnData(const Euclid::Table::Table& table, size_t column_index) {
  std::vector<T> data {};
  for (const auto& row : table) {
    data.push_back(boost::get<T>(row[column_index]));
  }
  return data;
}

template <typename T>
std::vector<std::valarray<T>> createVectorColumnData(const Euclid::Table::Table& table, size_t column_index) {
  std::vector<std::valarray<T>> result {};
  for (auto& row : table) {
    const auto& vec = boost::get<std::vector<T>>(row[column_index]);
    result.emplace_back(vec.data(), vec.size());
  }
  return result;
}

void populateColumn(const Table& table, size_t column_index, CCfits::Table* table_hdu) {
  auto type = table.getColumnInfo()->getDescription(column_index).type;
  // CCfits indices start from 1
  if (type == typeid(bool)) {
    table_hdu->column(column_index+1).write(createColumnData<bool>(table, column_index), 1);
  } else if (type == typeid(int32_t)) {
    table_hdu->column(column_index+1).write(createColumnData<int32_t>(table, column_index), 1);
  } else if (type == typeid(int64_t)) {
    table_hdu->column(column_index+1).write(createColumnData<int64_t>(table, column_index), 1);
  } else if (type == typeid(float)) {
    table_hdu->column(column_index+1).write(createColumnData<float>(table, column_index), 1);
  } else if (type == typeid(double)) {
    table_hdu->column(column_index+1).write(createColumnData<double>(table, column_index), 1);
  } else if (type == typeid(std::string)) {
    table_hdu->column(column_index+1).write(createColumnData<std::string>(table, column_index), 1);
  } else if (type == typeid(std::vector<int32_t>)) {
    table_hdu->column(column_index+1).writeArrays(createVectorColumnData<int32_t>(table, column_index), 1);
  } else if (type == typeid(std::vector<int64_t>)) {
    table_hdu->column(column_index+1).writeArrays(createVectorColumnData<int64_t>(table, column_index), 1);
  } else if (type == typeid(std::vector<float>)) {
    table_hdu->column(column_index+1).writeArrays(createVectorColumnData<float>(table, column_index), 1);
  } else if (type == typeid(std::vector<double>)) {
    table_hdu->column(column_index+1).writeArrays(createVectorColumnData<double>(table, column_index), 1);
  } else {
    throw Elements::Exception() << "Cannot populate FITS column with data of type " << type.name();
  }
}

}
} // end of namespace Euclid