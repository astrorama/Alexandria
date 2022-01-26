/*
 * Copyright (C) 2012-2022 Euclid Science Ground Segment
 *
 * This library is free software; you can redistribute it and/or modify it under
 * the terms of the GNU Lesser General Public License as published by the Free
 * Software Foundation; either version 3.0 of the License, or (at your option)
 * any later version.
 *
 * This library is distributed in the hope that it will be useful, but WITHOUT
 * ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
 * FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more
 * details.
 *
 * You should have received a copy of the GNU Lesser General Public License
 * along with this library; if not, write to the Free Software Foundation, Inc.,
 * 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
 */

/*
 * @file SOMTrainer.h
 * @author nikoapos
 */

#ifndef SOM_SOMTRAINER_H
#define SOM_SOMTRAINER_H

#include "SOM/LearningRestraintFunc.h"
#include "SOM/NeighborhoodFunc.h"
#include "SOM/SOM.h"
#include "SOM/SamplingPolicy.h"

namespace Euclid {
namespace SOM {

class SOMTrainer {

public:
  SOMTrainer(NeighborhoodFunc::Signature neighborhood_func, LearningRestraintFunc::Signature learning_restraint_func)
      : m_neighborhood_func(neighborhood_func), m_learning_restraint_func(learning_restraint_func) {}

  template <typename DistFunc, typename InputIter, typename InputToWeightFunc>
  void train(SOM<DistFunc>& som, std::size_t iter_no, InputIter begin, InputIter end, InputToWeightFunc weight_func,
             const SamplingPolicy::Interface<InputIter>& sampling_policy = SamplingPolicy::FullSet<InputIter>{}) {

    // We repeat the training for iter_no iterations
    for (std::size_t i = 0; i < iter_no; ++i) {

      // Compute the factor of the current iteration
      auto learn_factor = m_learning_restraint_func(i, iter_no);
      if (learn_factor == 0) {
        continue;
      }

      // Go through the training sample of the iteration
      for (auto it = sampling_policy.start(begin, end); it != end; it = sampling_policy.next(it)) {

        // Get the weights of the input object
        auto input_weights = weight_func(*it);

        // Find the coordinates of the BMU for the input
        std::size_t bmu_x, bmu_y;
        double      nd_distance;
        std::tie(bmu_x, bmu_y, nd_distance) = som.findBMU(*it, weight_func);

        // Now go through all the cells and update their values according their coordinates
        std::size_t size_x, size_y;
        std::tie(size_x, size_y) = som.getSize();

        for (std::size_t cell_y = 0; cell_y < size_y; ++cell_y) {
          for (std::size_t cell_x = 0; cell_x < size_x; ++cell_x) {
            auto& cell = som(cell_x, cell_y);

            // Compute the factor based on the distance of the BMU and the cell
            auto neighborhood_factor = m_neighborhood_func({bmu_x, bmu_y}, {cell_x, cell_y}, i, iter_no);

            // Get the weights of the cell and update them
            if (neighborhood_factor != 0) {
              for (std::size_t wi = 0; wi < som.getDimensions(); ++wi) {
                cell[wi] = cell[wi] + neighborhood_factor * learn_factor * (input_weights[wi] - cell[wi]);
              }
            }
          }
        }
      }
    }
  }

private:
  NeighborhoodFunc::Signature      m_neighborhood_func;
  LearningRestraintFunc::Signature m_learning_restraint_func;
};

}  // namespace SOM
}  // namespace Euclid

#endif /* SOM_SOMTRAINER_H */
