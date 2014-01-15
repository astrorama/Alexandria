elements_subdir(Integration 1.0)

elements_depends_on_subdirs(ChDataHandling)
elements_depends_on_subdirs(ChDataModel)
elements_depends_on_subdirs(ChTools)


#===== Integration tests =======================================================

#-----------------------
# ImportCosmosAscii_main

# Primary main program to test the ChDataHandling and ChDataModel functionality
elements_add_unit_test(ImportCosmosAscii_main tests/src/ImportCosmosAscii_main.cpp
                       LINK_LIBRARIES  ChDataHandling ChDataModel ChTools TYPE CppUnit)

if(ELEMENTS_BUILD_TESTS)
  set_property(TEST Integration.ImportCosmosAscii_main PROPERTY WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/tests/conf)
endif()


#-----------------------
# ProgramOptions_CommandLine_only

elements_add_unit_test(ProgramOptions_CommandLine_only tests/src/ProgramOptions_CommandLine_only.cpp
                       LINK_LIBRARIES  ChDataHandling ChDataModel ChTools TYPE CppUnit)

if(ELEMENTS_BUILD_TESTS)
  set_property(TEST Integration.ProgramOptions_CommandLine_only PROPERTY WORKING_DIRECTORY ${CMAKE_SOURCE_DIR})
endif()

#-----------------------
# ProgramOptions_CommandLine_2_only

elements_add_unit_test(ProgramOptions_CommandLine_2_only tests/src/ProgramOptions_CommandLine_2_only.cpp
                       LINK_LIBRARIES  ChDataHandling ChDataModel ChTools TYPE CppUnit)

if(ELEMENTS_BUILD_TESTS)
  set_property(TEST Integration.ProgramOptions_CommandLine_2_only PROPERTY WORKING_DIRECTORY ${CMAKE_SOURCE_DIR})
endif()

#------------
# Filter_main

elements_add_unit_test(Filter_main tests/src/Filter_main.cpp
                       LINK_LIBRARIES ChDataHandling ChDataModel ChTools TYPE CppUnit)

if(ELEMENTS_BUILD_TESTS)
  set_property(TEST Integration.Filter_main PROPERTY WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/tests/conf)
endif()






#-------------------------------------------------------------------------------
# CMAKE_SOURCE_DIR         = directory of the project (workspace, e.g. /.../Alexandria)
# CMAKE_CURRENT_SOURCE_DIR = directory of the package (e.g. /.../Alexandria/ChDataHandling)
#-------------------------------------------------------------------------------
