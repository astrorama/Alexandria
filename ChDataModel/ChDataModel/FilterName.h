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

  FilterName(const std::string& group, const std::string& name);

  virtual ~FilterName() = default;

  const std::string& group() const;

  const std::string& name() const;

  const std::string& qualifiedName() const;
  
  size_t hash() const;
  
  bool operator<(const FilterName& other) const;
  
  bool operator==(const FilterName& other) const;

private:

  const std::string m_group;
  const std::string m_name;
  mutable std::string m_qual_name {};
  mutable size_t m_hash {0};

}; // class FilterName

} // namespace ChDataModel 

namespace std {

template <>
struct hash<ChDataModel::FilterName>;

} // namespace std

#endif // FILTERNAME_H_ 
