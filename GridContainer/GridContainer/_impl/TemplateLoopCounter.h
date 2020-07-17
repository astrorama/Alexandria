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
 * @file GridContainer/_impl/TemplateLoopCounter.h
 * @date May 13, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef GRIDCONTAINER_TEMPLATELOOPCOUNTER_H
#define GRIDCONTAINER_TEMPLATELOOPCOUNTER_H

namespace Euclid {
namespace GridContainer {

/// This is a dummy class with a integer template parameter, which is used
/// as a counter for the template recursions.
template<int>
struct TemplateLoopCounter { };

}
} // end of namespace Euclid

#endif  /* GRIDCONTAINER_TEMPLATELOOPCOUNTER_H */

