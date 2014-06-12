/** 
 * @file LikelihoodMatrix.h
 * @date June 2, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef PHZDATAMODEL_LIKELIHOODMATRIX_H
#define	PHZDATAMODEL_LIKELIHOODMATRIX_H

#include <vector>
#include "PhzDataModel/PhzModel.h"

namespace PhzDataModel {

typedef std::vector<double> LikelihoodDataHandler;

typedef PhzMatrix<LikelihoodDataHandler> LikelihoodMatrix;

}

#endif	/* PHZDATAMODEL_LIKELIHOODMATRIX_H */

