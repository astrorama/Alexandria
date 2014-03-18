elements_subdir(ChDataHandling 1.0)

elements_depends_on_subdirs(ChDataModel)
elements_depends_on_subdirs(ChTools)

find_package(Boost REQUIRED COMPONENTS filesystem thread system)
find_package(Cfitsio)
find_package(CCfits)


#===== Libraries ===============================================================

elements_add_library(ChDataHandling src/*.cpp
                  LINK_LIBRARIES ${CMAKE_DL_LIBS} Boost Cfitsio CCfits ChTools ChDataModel
                  INCLUDE_DIRS Boost Cfitsio CCfits ChTools ChDataModel
                  PUBLIC_HEADERS ChDataHandling)


#===== Boost Tests =============================================================
# They must include also the tests/src/TestMain.cpp

#-----------------------
# ImportCosmosAscii_test

elements_add_unit_test(ImportCosmosAscii_test tests/src/ImportCosmosAscii_test.cpp tests/src/TestMain.cpp
                       LINK_LIBRARIES ChDataHandling ChDataModel ChTools TYPE Boost)

if(ELEMENTS_BUILD_TESTS)
  set_property(TEST ChDataHandling.ImportCosmosAscii_test PROPERTY WORKING_DIRECTORY ${CMAKE_SOURCE_DIR})
endif()

#-------------
# Factory_test

elements_add_unit_test(Factory_test tests/src/Factory_test.cpp tests/src/TestMain.cpp
                       LINK_LIBRARIES ChDataHandling ChDataModel ChTools TYPE Boost)

if(ELEMENTS_BUILD_TESTS)
  set_property(TEST ChDataHandling.Factory_test PROPERTY WORKING_DIRECTORY ${CMAKE_SOURCE_DIR})
endif()

#-------------------
# AsciiImporter_test

elements_add_unit_test(AsciiImporter_test tests/src/AsciiImporter_test.cpp tests/src/TestMain.cpp
                       LINK_LIBRARIES ChDataHandling ChDataModel ChTools TYPE Boost)

if(ELEMENTS_BUILD_TESTS)
  set_property(TEST ChDataHandling.AsciiImporter_test PROPERTY WORKING_DIRECTORY ${CMAKE_SOURCE_DIR})
endif()

#-------------------
# AsciiCosmosImporter_test

elements_add_unit_test(AsciiCosmosImporter_test tests/src/AsciiCosmosImporter_test.cpp tests/src/TestMain.cpp
                       LINK_LIBRARIES ChDataHandling ChDataModel ChTools TYPE Boost)

if(ELEMENTS_BUILD_TESTS)
  set_property(TEST ChDataHandling.AsciiCosmosImporter_test PROPERTY WORKING_DIRECTORY ${CMAKE_SOURCE_DIR})
endif()

#-------------------
# AsciiFilterImporter_test

elements_add_unit_test(AsciiFilterImporter_test tests/src/AsciiFilterImporter_test.cpp tests/src/TestMain.cpp
                       LINK_LIBRARIES ChDataHandling ChDataModel ChTools TYPE Boost)

if(ELEMENTS_BUILD_TESTS)
  set_property(TEST ChDataHandling.AsciiFilterImporter_test PROPERTY WORKING_DIRECTORY ${CMAKE_SOURCE_DIR})
endif()

#-------------------
# AsciiSedImporter_test

elements_add_unit_test(AsciiSedImporter_test tests/src/AsciiSedImporter_test.cpp tests/src/TestMain.cpp
                       LINK_LIBRARIES ChDataHandling ChDataModel ChTools TYPE Boost)

if(ELEMENTS_BUILD_TESTS)
  set_property(TEST ChDataHandling.AsciiSedImporter_test PROPERTY WORKING_DIRECTORY ${CMAKE_SOURCE_DIR})
endif()

#-------------------
# FitsImageImporter_test

elements_add_unit_test(FitsImageImporter_test tests/src/FitsImageImporter_test.cpp tests/src/TestMain.cpp
                       LINK_LIBRARIES ChDataHandling ChDataModel ChTools TYPE Boost)

if(ELEMENTS_BUILD_TESTS)
  set_property(TEST ChDataHandling.FitsImageImporter_test PROPERTY WORKING_DIRECTORY ${CMAKE_SOURCE_DIR})
endif()

#-------------------
# Areader_test

elements_add_unit_test(Areader_test tests/src/Areader_test.cpp tests/src/TestMain.cpp
                       LINK_LIBRARIES ChDataHandling ChDataModel ChTools TYPE Boost)

if(ELEMENTS_BUILD_TESTS)
  set_property(TEST ChDataHandling.Areader_test PROPERTY WORKING_DIRECTORY ${CMAKE_SOURCE_DIR})
endif()

#-------------------------
# ChDataHandling_all_tests

elements_add_unit_test(ChDataHandling_all_tests tests/src/*_test.cpp tests/src/TestMain.cpp
                       LINK_LIBRARIES ChDataHandling ChDataModel ChTools TYPE Boost)

if(ELEMENTS_BUILD_TESTS)
  set_property(TEST ChDataHandling.ChDataHandling_all_tests PROPERTY WORKING_DIRECTORY ${CMAKE_SOURCE_DIR})
endif()
