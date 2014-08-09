/** 
 * @file PhzDataModel/PhotometryGrid.h
 * @date May 19, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef PHZDATAMODEL_PHOTOMETRYGRID_H
#define	PHZDATAMODEL_PHOTOMETRYGRID_H

#include <memory>
#include "ChCatalog/SourceAttributes/Photometry.h"
#include "PhzDataModel/PhzModel.h"
#include "PhzDataModel/serialization/PhotometryVector.h"

namespace PhzDataModel {

typedef std::vector<ChCatalog::Photometry> PhotometryGridManager;

typedef PhzGrid<PhotometryGridManager> PhotometryGrid;

} // end of namespace PhzDataModel


namespace Grid {

// We define the GridCellManagerTraits for a vector of Photometries to redefine the
// factory method because the Photometry does not have default constructor.
template<>
struct GridCellManagerTraits<PhzDataModel::PhotometryGridManager> {
  typedef ChCatalog::Photometry data_type;
  typedef typename PhzDataModel::PhotometryGridManager::iterator iterator;
  static std::unique_ptr<PhzDataModel::PhotometryGridManager> factory(size_t size){
    ChCatalog::Photometry default_photometry {std::make_shared<std::vector<std::string>>(), {}};
    return std::unique_ptr<PhzDataModel::PhotometryGridManager> {
      new PhzDataModel::PhotometryGridManager(size, default_photometry)
    };
  }
  static size_t size(const PhzDataModel::PhotometryGridManager& vector) {
    return vector.size();
  }
  static iterator begin(PhzDataModel::PhotometryGridManager& vector) {
    return vector.begin();
  }
  static iterator end(PhzDataModel::PhotometryGridManager& vector) {
    return vector.end();
  }
  static const bool enable_boost_serialize = true;
}; // end of GridCellManagerTraits

} // end of namespace Grid

#endif	/* PHZDATAMODEL_PHOTOMETRYGRID_H */

