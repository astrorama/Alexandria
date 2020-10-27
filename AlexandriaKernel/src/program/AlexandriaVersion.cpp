/**
 * @file src/program/AlexandriaVersion.cpp
 * @date 10/26/20
 * @author aalvarez
 *
 * @copyright (C) 2012-2020 Euclid Science Ground Segment
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
 *
 */

#include <map>
#include <string>

#include <boost/program_options.hpp>
#include "ElementsKernel/ProgramHeaders.h"
#include "ALEXANDRIA_VERSION.h"

using boost::program_options::options_description;
using boost::program_options::variable_value;

class AlexandriaVersion : public Elements::Program {

public:

  options_description defineSpecificProgramOptions() override {
    options_description options {};
    return options;
  }

  Elements::ExitCode mainMethod(std::map<std::string, variable_value>&) override {
    std::cout << ALEXANDRIA_VERSION_STRING << std::endl;
    return Elements::ExitCode::OK;
  }

};

MAIN_FOR(AlexandriaVersion)



