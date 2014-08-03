/** 
 * @file PhzDataModel/PhzModel.h
 * @date May 20, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef PHZDATAMODEL_PHZMODEL_H
#define	PHZDATAMODEL_PHZMODEL_H

#include <tuple>
#include <vector>
#include <utility>
#include <istream>
#include "ChMatrix/AxisInfo.h"
#include "ChMatrix/Matrix.h"
#include "ChMatrix/serialize.h"
#include "XYDataset/QualifiedName.h"
#include "PhzDataModel/serialization/QualifiedName.h"

namespace PhzDataModel {

struct ModelParameter {
  enum {
    Z = 0,
    EBV = 1,
    REDDENING_CURVE = 2,
    SED = 3
  };
};

typedef std::tuple<ChMatrix::AxisInfo<double>, ChMatrix::AxisInfo<double>,
    ChMatrix::AxisInfo<XYDataset::QualifiedName>, ChMatrix::AxisInfo<XYDataset::QualifiedName>> ModelAxesTuple;

ModelAxesTuple createAxesTuple(std::vector<double> zs, std::vector<double> ebvs,
                               std::vector<XYDataset::QualifiedName> reddening_curves,
                               std::vector<XYDataset::QualifiedName> seds) {
  ChMatrix::AxisInfo<double> z_axis {"Z", std::move(zs)};
  ChMatrix::AxisInfo<double> ebv_axis {"E(B-V)", std::move(ebvs)};
  ChMatrix::AxisInfo<XYDataset::QualifiedName> reddening_curves_axis {"Reddening Curve", std::move(reddening_curves)};
  ChMatrix::AxisInfo<XYDataset::QualifiedName> sed_axis {"SED", std::move(seds)};
  return ModelAxesTuple{std::move(z_axis), std::move(ebv_axis),
                        std::move(reddening_curves_axis), std::move(sed_axis)};
}

template<typename DataManager>
using PhzMatrix = typename ChMatrix::Matrix<DataManager, double, double, XYDataset::QualifiedName, XYDataset::QualifiedName>;

template<typename DataManager>
PhzMatrix<DataManager> binaryImportPhzMatrix(std::istream& in) {
  return ChMatrix::binaryImport<DataManager, double, double, XYDataset::QualifiedName, XYDataset::QualifiedName>(in);
}

}

#endif	/* PHZDATAMODEL_PHZMODEL_H */

