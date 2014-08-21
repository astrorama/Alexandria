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

namespace PhzDataModel {

typedef std::vector<ChCatalog::Photometry> PhotometryCellManager;

typedef PhzGrid<PhotometryCellManager> PhotometryGrid;

} // end of namespace PhzDataModel


namespace Grid {

// We define the GridCellManagerTraits for a vector of Photometries to redefine the
// factory method because the Photometry does not have default constructor.
template<>
struct GridCellManagerTraits<PhzDataModel::PhotometryCellManager> {
  typedef ChCatalog::Photometry data_type;
  typedef typename PhzDataModel::PhotometryCellManager::iterator iterator;
  static std::unique_ptr<PhzDataModel::PhotometryCellManager> factory(size_t size){
    ChCatalog::Photometry default_photometry {std::make_shared<std::vector<std::string>>(), {}};
    return std::unique_ptr<PhzDataModel::PhotometryCellManager> {
      new PhzDataModel::PhotometryCellManager(size, default_photometry)
    };
  }
  static size_t size(const PhzDataModel::PhotometryCellManager& vector) {
    return vector.size();
  }
  static iterator begin(PhzDataModel::PhotometryCellManager& vector) {
    return vector.begin();
  }
  static iterator end(PhzDataModel::PhotometryCellManager& vector) {
    return vector.end();
  }
  static const bool enable_boost_serialize = true;
}; // end of GridCellManagerTraits

} // end of namespace Grid

// Here we include the serialization of the photometry grid. This is done here
// to avoid having the default grid serialization applied to the PhotometryGrid
// (which would happen if the user would forget to include this file)
#include "PhzDataModel/serialization/PhotometryGrid.h"

#endif	/* PHZDATAMODEL_PHOTOMETRYGRID_H */

