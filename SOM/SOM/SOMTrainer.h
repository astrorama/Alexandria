/*
 * Copyright (C) 2012-2020 Euclid Science Ground Segment    
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

#include "SOM/SOM.h"
#include "SOM/NeighborhoodFunc.h"
#include "SOM/LearningRestraintFunc.h"

#include <iostream>

namespace Euclid {
namespace SOM {

class SOMTrainer {
  
public:
  
  SOMTrainer(NeighborhoodFunc::Signature neighborhood_func,
             LearningRestraintFunc::Signature learning_restraint_func=LearningRestraintFunc::linear())
          : m_neighborhood_func(neighborhood_func), 
            m_learning_restraint_func(learning_restraint_func) {
  }

  template <std::size_t ND, typename DistFunc, typename InputIter, typename InputToWeightFunc>
  void train(SOM<ND, DistFunc>& som, std::size_t iter_no, InputIter begin, InputIter end, InputToWeightFunc weight_func) {
    
    // We repeat the training for iter_no iterations
    for (std::size_t i = 0; i < iter_no; ++ i) {
     
      // Go through the training sample of the iteration
      for (auto it = begin; it != end; ++it) {
        
        // Get the weights of the input object
        auto input_weights = weight_func(*it);
        
        // Find the coordinates of the BMU for the input
        std::size_t bmu_x;
        std::size_t bmu_y;
        double nd_distance;
        std::tie(bmu_x, bmu_y, nd_distance) = som.findBMU(*it, weight_func);

        // Now go through all the cells and update their values according their coordinates
        for (auto cell_it = som.begin(); cell_it != som.end(); ++ cell_it) {
          
          // Compute the factor based on the distance of the BMU and the cell
          auto cell_x = cell_it.template axisValue<0>();
          auto cell_y = cell_it.template axisValue<1>();
          auto neighborhood_factor = m_neighborhood_func({bmu_x, bmu_y}, {cell_x, cell_y}, i, iter_no);
          
          // Compute the factor of the current iteration
          auto learn_factor = m_learning_restraint_func(i, iter_no);
          
          // Get the weights of the cell and update them
          auto& cell_weights = *cell_it;
          for (std::size_t wi = 0; wi < ND; ++wi) {
            cell_weights[wi] = cell_weights[wi] + neighborhood_factor * learn_factor * (input_weights[wi] - cell_weights[wi]);
          }
          
        }
      } 
    }
  }
  
private:
  
  NeighborhoodFunc::Signature m_neighborhood_func;
  LearningRestraintFunc::Signature m_learning_restraint_func;
  
};

}
}

#endif /* SOM_SOMTRAINER_H */

