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
 * @file src/lib/FileSystemProvider.cpp
 *
 * @date Apr 14, 2014
 * @author Nicolas Morisset
 */

#include "XYDataset/FileSystemProvider.h"
#include "ElementsKernel/Exception.h"
#include "ElementsKernel/Logging.h"
#include "StringFunctions.h"
#include <boost/algorithm/string.hpp>
#include <boost/filesystem.hpp>
#include <fstream>
#include <set>
#include <string>
#include <unordered_set>

namespace fs = boost::filesystem;

namespace Euclid {
namespace XYDataset {

static Elements::Logging logger = Elements::Logging::getLogger("FileSystemProvider");

/**
 * Returns a list of the contents of the given directory. If the directory
 * contains the file order.txt, it will respect the order in this file. If the
 * directory contains files which are not mentioned in the order.txt, they are
 * appended at the end.
 * @param dir The directory to get the contents of
 * @return The contents of the directory, ordered as described in order.txt
 */
static std::vector<fs::path> getOrder(const fs::path& dir) {
  std::vector<fs::path> result{};

  // First add the files in the order.txt
  auto                            order_file = dir / "order.txt";
  std::unordered_set<std::string> ordered_names{};
  if (fs::exists(order_file)) {
    std::ifstream in{order_file.c_str()};
    while (in) {
      std::string line;
      getline(in, line);
      size_t comment_pos = line.find('#');
      if (comment_pos != std::string::npos) {
        line = line.substr(0, comment_pos);
      }
      boost::trim(line);
      if (!line.empty()) {
        auto name = dir / line;
        if (fs::exists(name)) {
          result.emplace_back(name);
          ordered_names.emplace(line);
        } else {
          logger.warn() << "Unknown name " << line << " in order.txt of " << dir << " directory";
        }
      }
    }
  }

  // Now we add any other files in the directory, which were not in the order.txt
  // file. We use a set in order to avoid sorting problem between platforms.
  std::set<fs::path> remaining_files{};
  for (fs::directory_iterator iter{dir}; iter != fs::directory_iterator{}; ++iter) {
    if (ordered_names.count(iter->path().filename().string()) == 0) {
      remaining_files.emplace(*iter);
    }
  }

  // Put the remaining files into the result vector
  for (auto& file : remaining_files) {
    result.emplace_back(file);
  }

  return result;
}

static std::vector<fs::path> getRecursiveDirectoryContents(const fs::path& dir) {
  std::vector<fs::path> result{};
  auto                  ordered_contents = getOrder(dir);
  for (auto& name : ordered_contents) {
    if (fs::is_directory(name)) {
      auto sub_dir_contents = getRecursiveDirectoryContents(name);
      result.insert(result.end(), sub_dir_contents.begin(), sub_dir_contents.end());
    } else {
      result.emplace_back(name);
    }
  }
  return result;
}

//-----------------------------------------------------------------------------
//                              Constructor
//-----------------------------------------------------------------------------

FileSystemProvider::FileSystemProvider(const std::string& root_path, std::unique_ptr<FileParser> parser)
    : XYDatasetProvider(), m_root_path(root_path), m_parser(std::move(parser)) {

  std::vector<std::string> string_vector{};

  // Make sure the root path finishes with a "/" and only one
  m_root_path = checkEndSlashes(m_root_path);

  // Convert path to boost filesytem object
  fs::path fspath(m_root_path);
  if (!fs::exists(fspath)) {
    throw Elements::Exception() << "From FileSystemProvider: root path not found : " << fspath;
  }

  // Get all files below the root directory
  if (fs::is_directory(fspath)) {
    auto dir_contents = getRecursiveDirectoryContents(fspath);
    for (auto& file : dir_contents) {
      if (fs::is_regular_file(file) && m_parser->isDatasetFile(file.string())) {
        std::string dataset_name = m_parser->getName(file.string());
        // Remove empty dataset name
        if (dataset_name.empty()) {
          continue;
        }
        // Remove the root part
        std::string str = file.string();
        str             = str.substr(m_root_path.length(), str.length());
        // Split by the character '/'
        std::vector<std::string> groups{};
        boost::split(groups, str, boost::is_any_of("/"));
        // The last string is the file name, so we remove it
        groups.pop_back();
        QualifiedName qualified_name{groups, dataset_name};
        // Fill up a map
        auto ret = m_name_file_map.insert(make_pair(qualified_name, file.string()));
        m_order_names.push_back(qualified_name);
        // Check for unique record
        if (!ret.second) {
          throw Elements::Exception() << "Qualified name can not be inserted "
                                      << "in the map. Qualify name : " << qualified_name.qualifiedName()
                                      << " Path :" << file.string();
        }
      }
    }
  } else {
    throw Elements::Exception() << " Root path : " << fspath.string() << " is not a directory!";
  }
}

//-----------------------------------------------------------------------------
//                             listContents function
//-----------------------------------------------------------------------------

std::vector<QualifiedName> FileSystemProvider::listContents(const std::string& group) {

  std::string my_group = group;
  // Make sure the group finishes with a "/" and only one
  while (!my_group.empty() && my_group.back() == '/') {
    my_group.pop_back();
  }
  // Make sure the group do not start with a "/"
  size_t pos = my_group.find_first_not_of("/");
  if (!my_group.empty() && pos != 0) {
    my_group = my_group.substr(pos);
  }
  if (!my_group.empty()) {
    my_group.push_back('/');
  }

  std::vector<QualifiedName> qualified_name_vector{};

  // Fill up vector with qualified name from the map
  // Insert all qualified name where path contains the group name at the
  // first position
  for (auto qualified_name : m_order_names) {
    if (boost::starts_with(qualified_name.qualifiedName(), my_group)) {
      qualified_name_vector.push_back(qualified_name);
    }
  }  // Eof for

  return (qualified_name_vector);
}

//-----------------------------------------------------------------------------
//                             getDataset function
//-----------------------------------------------------------------------------

std::unique_ptr<XYDataset> FileSystemProvider::getDataset(const QualifiedName& qualified_name) {

  auto it = m_name_file_map.find(qualified_name);
  return (it != m_name_file_map.end()) ? m_parser->getDataset(it->second) : nullptr;
}

std::string FileSystemProvider::getParameter(const QualifiedName& qualified_name, const std::string& key_word) {
  auto it = m_name_file_map.find(qualified_name);
  return (it != m_name_file_map.end()) ? m_parser->getParameter(it->second, key_word) : "";
}

} /* namespace XYDataset */
}  // end of namespace Euclid
