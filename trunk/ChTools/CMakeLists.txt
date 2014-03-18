elements_subdir(ChTools 1.0)
elements_depends_on_subdirs(ElementsKernel)

find_package(Boost REQUIRED COMPONENTS filesystem thread system program_options)

#---Libraries---------------------------------------------------------------
elements_add_library(ChTools src/*.cpp
                  LINK_LIBRARIES ${CMAKE_DL_LIBS} Boost
                  INCLUDE_DIRS Boost
                  PUBLIC_HEADERS ChTools)

#===== Boost Tests =============================================================
# They must include also the tests/src/TestMain.cpp


#-------------------------------------------------------------------------------
# CMAKE_SOURCE_DIR         = directory of the project (workspace, e.g. /.../Alexandria)
# CMAKE_CURRENT_SOURCE_DIR = directory of the package (e.g. /.../Alexandria/ChDataHandling)
#-------------------------------------------------------------------------------
