/** 
 * @file PhotometryVector.h
 * @date May 22, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef PHZDATAMODEL_SERIALIZATION_PHOTOMETRYVECTOR_H
#define	PHZDATAMODEL_SERIALIZATION_PHOTOMETRYVECTOR_H

#include <vector>
#include <memory>
#include <boost/serialization/split_free.hpp>
#include "ElementsKernel/ElementsException.h"
#include "ChCatalog/SourceAttributes/Photometry.h"

namespace boost {
namespace serialization {

template<typename Archive>
void save(Archive& ar, const std::vector<ChCatalog::Photometry>& t, const unsigned int) {
  size_t size = t.size();
  if (size == 0) {
    throw ElementsException() << "Serialization of empty Photometry vectors is not supported";
  }
  ar << size;
  // We store the filter names only once. We require that all photometries have
  // the same filters
  std::vector<std::string> filter_names {};
  for (auto iter=t[0].begin(); iter!=t[0].end(); ++iter) {
    filter_names.push_back(iter.filterName());
  }
  ar << filter_names;
  // We store the flux and error values for each photometry and we check if the
  // filters are matching the common ones
  for (auto& photometry : t) {
    if (photometry.size() != filter_names.size()) {
      throw ElementsException() << "Serialization of vectors of Photometries with "
                                << "different filters is not supported";
    }
    auto filt_iter = filter_names.begin();
    for (auto phot_iter=photometry.begin(); phot_iter!=photometry.end(); ++phot_iter, ++ filt_iter) {
      if (*filt_iter != phot_iter.filterName()) {
        throw ElementsException() << "Serialization of vectors of Photometries with "
                                  << "different filters is not supported";
      }
      ar << (*phot_iter).flux;
      ar << (*phot_iter).error;
    }
  }
}

template<typename Archive>
void load(Archive& ar, std::vector<ChCatalog::Photometry>& t, const unsigned int) {
  size_t size;
  ar >> size;
  std::vector<std::string> filter_names;
  ar >> filter_names;
  auto filter_names_ptr = std::make_shared<std::vector<std::string>>(std::move(filter_names));
  while (size != 0) {
    --size;
    std::vector<ChCatalog::FluxErrorPair> phot_values;
    for (int i=0; i< filter_names_ptr->size(); ++i) {
      double flux;
      double error;
      ar >> flux >> error;
      phot_values.push_back({flux, error});
    }
    t.push_back({filter_names_ptr, std::move(phot_values)});
  }
}

template<typename Archive>
void serialize(Archive& ar, std::vector<ChCatalog::Photometry>& t, const unsigned int version) {
  split_free(ar, t, version);
}

} // end of namespace serialization
} // end of namespace boost

#endif	/* PHZDATAMODEL_SERIALIZATION_PHOTOMETRYVECTOR_H */

