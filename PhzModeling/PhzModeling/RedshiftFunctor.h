/**
 * @file PhzModeling/RedshiftFunctor.h
 * @date Sep 15, 2014
 * @author Florian Dubath
 */

#ifndef PHZMODELING_REDSHIFTFUNCTOR_H
#define	PHZMODELING_REDSHIFTFUNCTOR_H


#include "XYDataset/XYDataset.h"

namespace Euclid {
namespace PhzModeling {

class RedshiftFunctor {

public:
	RedshiftFunctor() = default;

	RedshiftFunctor(RedshiftFunctor&&) = default;

	RedshiftFunctor& operator=(RedshiftFunctor&&) = default;

	virtual ~RedshiftFunctor() = default;

	Euclid::XYDataset::XYDataset operator()(const Euclid::XYDataset::XYDataset& sed, double z) const {
	    std::vector<std::pair<double, double>> redshifted_values {};
	    for (auto& sed_pair : sed) {
	    	redshifted_values.push_back(std::make_pair(sed_pair.first*(1+z),sed_pair.second/((1+z)*(1+z))));
	    }
	    return  Euclid::XYDataset::XYDataset {std::move(redshifted_values)};
	  }
};

} // end of namespace PhzModeling
} // end of namespace Euclid

#endif	/* PHZMODELING_REDSHIFTFUNCTOR_H */
