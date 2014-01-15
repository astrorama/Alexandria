elements_subdir(PCA 1.0)

find_package(Boost REQUIRED COMPONENTS filesystem thread system program_options)

#---Libraries---------------------------------------------------------------
elements_add_library(PCA src/*.cpp
                  LINK_LIBRARIES ${CMAKE_DL_LIBS} Boost
                  INCLUDE_DIRS Boost
                  PUBLIC_HEADERS PCA)

#===== Boost Tests =============================================================
# They must include also the tests/src/TestMain.cpp

#-------------------
# MakePCARing_test

elements_add_unit_test(MakePCARing_test tests/src/MakePCARing_test.cpp tests/src/TestMain.cpp
                       LINK_LIBRARIES PCA ChDataHandling ChDataModel ChTools TYPE Boost)

if(ELEMENTS_BUILD_TESTS)
  set_property(TEST PCA.MakePCARing_test PROPERTY WORKING_DIRECTORY ${CMAKE_SOURCE_DIR})
endif()


#-------------------------------------------------------------------------------
# CMAKE_SOURCE_DIR         = directory of the project (workspace, e.g. /.../Alexandria)
# CMAKE_CURRENT_SOURCE_DIR = directory of the package (e.g. /.../Alexandria/ChDataHandling)
#-------------------------------------------------------------------------------
