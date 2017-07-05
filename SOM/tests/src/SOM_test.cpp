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

/**
 * @file tests/src/SOM_test.cpp
 * @date 06/21/17
 * @author nikoapos
 */

#include <boost/test/unit_test.hpp>

#include "SOM/SOM.h"
#include "SOM/SOMTrainer.h"
#include "SOM/InitFunc.h"
#include "SOM/SOMProjector.h"
#include "SOM/SOMProjector.h"
#include "SOM/serialize.h"

#include <iostream>

using namespace Euclid::SOM;

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE (SOM_test)

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_CASE( example_test ) {

  SOM<2> som {5, 5, InitFunc::uniformRandom(0, 1)};
  som.findBMU({1,2});
  som.findBMU({1,2}, {0.1, 0.4});
  
  std::vector<std::pair<double,double>> trainset {
    {1,1}, {0,0}, {0,1}, {1,0}
  };
  
  SOMTrainer trainer {NeighborhoodFunc::linearUnitDisk(3), LearningRestraintFunc::linear()};
  auto weight_func = [](const std::pair<double,double>& p) {
    std::array<double, 2> res;
    res[0] = p.first;
    res[1] = p.second;
    return res;
  };
  trainer.train(som, 5, trainset.begin(), trainset.end(), weight_func);
  
  
  auto adder = [](int& cell, const std::pair<double, double>&) {
    cell += 1;
  };
  auto projection = SOMProjector::project<int>(som, trainset.begin(), trainset.end(), weight_func, adder);
  for (auto it=projection.begin(); it!= projection.end(); ++it) {
    std::cout << '(' << it.axisValue<0>() << ',' << it.axisValue<1>() << ") : " << *it << '\n';
  }
  
  
}

//-----------------------------------------------------------------------------

BOOST_AUTO_TEST_SUITE_END ()


