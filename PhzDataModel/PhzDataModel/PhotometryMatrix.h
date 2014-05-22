/** 
 * @file PhotometryMatrix.h
 * @date May 19, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef PHZDATAMODEL_PHOTOMETRYMATRIX_H
#define	PHZDATAMODEL_PHOTOMETRYMATRIX_H

#include <memory>
#include "ChCatalog/SourceAttributes/Photometry.h"
#include "PhzDataModel/PhzModel.h"
#include "PhzDataModel/serialization/PhotometryVector.h"

namespace PhzDataModel {

typedef std::vector<ChCatalog::Photometry> PhotometryDataHandler;

typedef PhzMatrix<PhotometryDataHandler> PhotometryMatrix;

} // end of namespace PhzDataModel


namespace ChMatrix {

// We define the DataManagerTraits for a vector of Photometries to redefine the
// factory method because the Photometry does not have default constructor.
template<>
class DataManagerTraits<PhzDataModel::PhotometryDataHandler> {
public:
  typedef ChCatalog::Photometry data_type;
  typedef typename PhzDataModel::PhotometryDataHandler::iterator iterator;
  static std::unique_ptr<PhzDataModel::PhotometryDataHandler> factory(size_t size){
    ChCatalog::Photometry default_photometry {std::make_shared<std::vector<std::string>>(), {}};
    return std::unique_ptr<PhzDataModel::PhotometryDataHandler> {
      new PhzDataModel::PhotometryDataHandler(size, default_photometry)
    };
  }
  static size_t size(const PhzDataModel::PhotometryDataHandler& vector) {
    return vector.size();
  }
  static iterator begin(PhzDataModel::PhotometryDataHandler& vector) {
    return vector.begin();
  }
  static iterator end(PhzDataModel::PhotometryDataHandler& vector) {
    return vector.end();
  }
  static const bool enable_boost_serialize = true;
}; // end of DataManagerTraits

} // end of namespace ChMatrix

#endif	/* PHZDATAMODEL_PHOTOMETRYMATRIX_H */

