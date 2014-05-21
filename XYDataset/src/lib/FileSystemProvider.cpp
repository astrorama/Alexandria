/**
 * @file FileSytemProvider.icpp
 *
 * @date Apr 14, 2014
 * @author Nicolas Morisset
 */

#include <exception>
#include <boost/filesystem.hpp>
#include <boost/algorithm/string.hpp>
#include "ElementsKernel/ElementsException.h"
#include "XYDataset/FileSystemProvider.h"

namespace fs = boost::filesystem;

namespace XYDataset {

//-----------------------------------------------------------------------------
//                              Constructor
//-----------------------------------------------------------------------------

FileSystemProvider::FileSystemProvider(const std::string& root_path, std::unique_ptr<FileParser> parser)
                   : XYDatasetProvider(), m_root_path(root_path), m_parser(std::move(parser)) {

  std::vector<std::string> string_vector{};

  // Make sure the group finishes with a "/" and only one
  size_t pos = m_root_path.find_last_not_of("/");
  if (  pos != m_root_path.length()-1) {
    m_root_path = m_root_path.substr(0, pos+1) + "/";
  }

  // Convert path to boost filesytem object
  fs::path fspath(m_root_path);
  if (!fs::exists(fspath)) {
    throw ElementsException() << "Root path not found : " << fspath;
  }

  // Get all files below the root directory
  if (fs::is_directory(fspath)) {
    fs::recursive_directory_iterator it {m_root_path};
    fs::recursive_directory_iterator endit;
    while(it != endit)
    {
      if (fs::is_regular_file(*it))
      {
        std::string dataset_name = m_parser->getName(it->path().string());
        // Remove the root part
        std::string str = it->path().string();
        str = str.substr(m_root_path.length(), str.length());
        // Split by the character '/'
        std::vector<std::string> groups {};
        boost::split(groups, str, boost::is_any_of("/"));
        // The last string is the file name, so we remove it
        groups.pop_back();
        QualifiedName qualified_name {groups, dataset_name};
        // Fill up a map
        auto ret = m_map.insert(make_pair(qualified_name, it->path().string()));
        // Check for unique record
        if (!ret.second) {
          throw ElementsException() << "Qualified name can not be inserted "
                                    << "in the map. Qualify name : "
                                    << qualified_name.qualifiedName()
                                    << " Path :" << it->path().string();
        }
      }
      ++it;
    }
  }
  else {
    throw ElementsException() << " Root path : " << fspath.string() << " is not a directory!";
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

 std::vector<QualifiedName> qualified_name_vector{};

 // Fill up vector with qualified name from the map
 // Insert all qualified name where path contains the group name at the
 // first position
 for (auto it : m_map ) {
     auto qualified_name = it.first;
      if (boost::starts_with(qualified_name.qualifiedName(), my_group)) {
         qualified_name_vector.push_back(qualified_name);
     }
 } // Eof for

 return (qualified_name_vector);
}

//-----------------------------------------------------------------------------
//                             getDataset function
//-----------------------------------------------------------------------------

std::unique_ptr<XYDataset> FileSystemProvider::getDataset(const QualifiedName & qualified_name) {

 std::string filename {};

 auto it = m_map.find(qualified_name);
 if (it != m_map.end()) {
    filename = it->second;
 }

 return (m_parser->getDataset(filename));
}

} /* namespace XYDataset */
