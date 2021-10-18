/*
 * Copyright (C) 2012-2021 Euclid Science Ground Segment
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
 * @file src/lib/ReaderHelper.cpp
 * @date April 21, 2014
 * @author Nikolaos Apostolakos
 */

#include "ReaderHelper.h"

namespace Euclid {
namespace Table {

std::shared_ptr<ColumnInfo> createColumnInfo(const std::vector<std::string>&     names,
                                             const std::vector<std::type_index>& types,
                                             const std::vector<std::string>&     units,
                                             const std::vector<std::string>&     descriptions) {
  std::vector<ColumnInfo::info_type> info_list{};
  for (size_t i = 0; i < names.size(); ++i) {
    info_list.emplace_back(names[i], types[i], units[i], descriptions[i]);
  }
  return std::shared_ptr<ColumnInfo>(new ColumnInfo{std::move(info_list)});
}

}  // namespace Table
}  // end of namespace Euclid
