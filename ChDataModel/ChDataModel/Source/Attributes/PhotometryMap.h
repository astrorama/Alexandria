/**
 * @file PhotometryMap.h
 *
 * @date Jan 16, 2014
 * @author dubath
 */

#ifndef PHOTOMETRYMAP_H_
#define PHOTOMETRYMAP_H_

#include<string>
#include<map>

namespace ChDataModel {

class PhotometryMap : public Attribute {
public:
  PhotometryMap(std::map<std::string, Photometry> m_photometry_map) {}
  virtual ~PhotometryMap() {}

  const std::map<std::string, Photometry>& getPhotometryMap() const {
    return m_photometry_map;
  }

private:
  const std::map<std::string, Photometry> m_photometry_map {};

};

} // namespace ChDataModel 

#endif // PHOTOMETRYMAP_H_ 
