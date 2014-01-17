/**
 * @file FilterName.h
 *
 * @date Jan 16, 2014
 * @author dubath
 */

#ifndef FILTERNAME_H_
#define FILTERNAME_H_

#include <string>

namespace ChDataModel {

class FilterName {
public:
  FilterName(std::string filter_name) : m_filter_name(filter_name) {}
  virtual ~FilterName();

  const std::string& get() const {
    return m_filter_name;
  }

private:

  const std::string m_filter_name;

};

} // namespace ChDataModel 

#endif // FILTERNAME_H_ 
