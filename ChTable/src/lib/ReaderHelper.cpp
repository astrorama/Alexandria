/** 
 * @file src/lib/ReaderHelper.cpp
 * @date April 21, 2014
 * @author Nikolaos Apostolakos
 */

#include "ReaderHelper.h"

namespace Euclid {
namespace ChTable {

std::shared_ptr<ColumnInfo> createColumnInfo(const std::vector<std::string>& names,
                                             const std::vector<std::type_index>& types) {
  std::vector<ColumnInfo::info_type> info_list {};
  for (size_t i=0; i< names.size(); ++i) {
    info_list.push_back({names[i], types[i]});
  }
  return std::shared_ptr<ColumnInfo>(new ColumnInfo{std::move(info_list)});
}

}
} // end of namespace Euclid