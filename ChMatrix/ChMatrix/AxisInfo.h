/** 
 * @file AxisInfo.h
 * @date May 12, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef CHMATRIX_AXISINFO_H
#define	CHMATRIX_AXISINFO_H

#include <string>
#include <vector>

namespace ChMatrix {

template<typename T>
class AxisInfo {

public:
  
  typedef typename std::vector<T>::const_iterator const_iterator;
  
  AxisInfo(std::string name, std::vector<T> values);
  
  virtual ~AxisInfo() = default;
  
  size_t size() const;
  
  const std::string& name() const;
  
  const T& operator[](size_t index) const;
  
  const_iterator begin() const;
  
  const_iterator end() const;

private:
  
  std::string m_name;
  std::vector<T> m_values;
  
};

} // end of namespace ChMatrix

#include "ChMatrix/_impl/AxisInfo.icpp"

#endif	/* CHMATRIX_AXISINFO_H */

