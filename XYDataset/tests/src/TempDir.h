/** 
 * @file TempDir.h
 * @date May 27, 2014
 * @author Nikolaos Apostolakos
 */

#ifndef TEMPDIR_H
#define	TEMPDIR_H

#include <boost/filesystem.hpp>

struct TempDir {
  TempDir() {
    name = boost::filesystem::temp_directory_path() / boost::filesystem::unique_path();
    boost::filesystem::create_directory(name);
    name_str = name.native();
  }
  ~TempDir() {
    boost::filesystem::remove_all(name);
  }
  boost::filesystem::path name;
  std::string name_str;
};

#endif	/* TEMPDIR_H */

