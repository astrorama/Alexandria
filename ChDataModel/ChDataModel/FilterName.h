/**
 * @file FilterName.h
 *
 * @date Jan 16, 2014
 * @author dubath
 */

#ifndef FILTERNAME_H_
#define FILTERNAME_H_

#include <string>
#include <functional>

namespace ChDataModel {

class FilterName {

public:

  FilterName(const std::string& group, const std::string& name);
  
  FilterName(const FilterName&) = default;
  
  FilterName& operator=(const FilterName&) = default;
  
  FilterName(FilterName&&) = default;
  
  FilterName& operator=(FilterName&&) = default;

  virtual ~FilterName() = default;

  const std::string& group() const;

  const std::string& name() const;

  const std::string& qualifiedName() const;
  
  size_t hash() const;
  
  bool operator<(const FilterName& other) const;
  
  bool operator==(const FilterName& other) const;

private:

  std::string m_group;
  std::string m_name;
  mutable std::string m_qual_name {};
  mutable size_t m_hash {0};

}; // class FilterName

} // namespace ChDataModel 

namespace std {

template <>
struct hash<ChDataModel::FilterName> {
  size_t operator()(const ChDataModel::FilterName& filterName) const {
    return filterName.hash();
  }
};

} // namespace std

#endif // FILTERNAME_H_ 
