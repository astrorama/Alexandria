elements_subdir(Faros 1.0)

elements_depends_on_subdirs(ElementsKernel)
elements_depends_on_subdirs(ChDataHandling)
elements_depends_on_subdirs(ChDataModel)
elements_depends_on_subdirs(ChTools)

find_package(Boost REQUIRED COMPONENTS filesystem thread system)


#===== Libraries ===============================================================

elements_add_library(Faros src/*.cpp
                  LINK_LIBRARIES ${CMAKE_DL_LIBS} Boost ChTools ChDataModel ChDataHandling ElementsKernel
                  INCLUDE_DIRS Boost ChTools ChDataModel ChDataHandling ElementsKernel
                  PUBLIC_HEADERS Faros)


#===== Boost Tests =============================================================
# They must include also the tests/src/TestMain.cpp

#-------------
# All_test

elements_add_unit_test(Faros_all_tests tests/src/*_test.cpp tests/src/TestMain.cpp
                       LINK_LIBRARIES ChDataHandling ChDataModel ChTools Faros TYPE Boost)

elements_add_unit_test(Faros_SedIntegration_test tests/src/SedIntegration_test.cpp tests/src/TestMain.cpp
                       LINK_LIBRARIES ChDataHandling ChDataModel ChTools Faros TYPE Boost)

#elements_add_unit_test(Faros_SedIntegration_SED_Through_All_Filters tests/src/SedIntegration_SED_Through_All_Filters.cpp tests/src/TestMain.cpp
#                       LINK_LIBRARIES ChDataHandling ChDataModel ChTools Faros TYPE Boost)

#elements_add_unit_test(Faros_Magnitude_SED_Through_All_Filters tests/src/Magnitude_SED_Through_All_Filters.cpp tests/src/TestMain.cpp
#                       LINK_LIBRARIES ChDataHandling ChDataModel ChTools Faros TYPE Boost)


elements_add_unit_test(Faros_interpolation_tests tests/src/Interpolation_test.cpp tests/src/TestMain.cpp
                       LINK_LIBRARIES ChDataHandling ChDataModel ChTools Faros TYPE Boost)



#-------------------------------------------------------------------------------
# CMAKE_SOURCE_DIR         = directory of the project (workspace, e.g. /.../Alexandria)
# CMAKE_CURRENT_SOURCE_DIR = directory of the package (e.g. /.../Alexandria/ChDataHandling)
#-------------------------------------------------------------------------------
