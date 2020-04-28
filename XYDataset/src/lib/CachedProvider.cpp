/**
 * @file src/lib/CachedProvider.cpp
 * @date 08/14/18
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

#include "XYDataset/CachedProvider.h"

namespace Euclid {
namespace XYDataset {


CachedProvider::CachedProvider(std::shared_ptr<Euclid::XYDataset::XYDatasetProvider> provider)
  : m_provider(provider)
{
}


std::vector<QualifiedName> CachedProvider::listContents(const std::string &group) {
  auto i = m_list_cache.find(group);
  if (i == m_list_cache.end()) {
    auto contents = m_provider->listContents(group);
    i = m_list_cache.insert(std::make_pair(group, contents)).first;
  }
  return i->second;
}


std::unique_ptr<XYDataset> CachedProvider::getDataset(const Euclid::XYDataset::QualifiedName &qualified_name) {
  auto i = m_dataset.find(qualified_name);
  if (i == m_dataset.end()) {
    auto dataset = m_provider->getDataset(qualified_name);
    i = m_dataset.insert(std::make_pair(qualified_name, std::move(dataset))).first;
  }
  if (i->second)
    return std::unique_ptr<XYDataset>(new XYDataset(*i->second));
  else
    return nullptr;
}

std::string CachedProvider::getParameter(const QualifiedName& qualified_name, const std::string& key_word){
   return m_provider->getParameter(qualified_name, key_word);
}

}  // namespace XYDataset
}  // namespace Euclid
