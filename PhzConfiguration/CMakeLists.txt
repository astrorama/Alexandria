elements_subdir(PhzConfiguration 0.1)

elements_depends_on_subdirs(XYDataset)

#===== Libraries ===============================================================

elements_add_library(PhzConfiguration src/lib/*.cpp
                     LINK_LIBRARIES XYDataset
                     INCLUDE_DIRS XYDataset
                     PUBLIC_HEADERS PhzConfiguration)