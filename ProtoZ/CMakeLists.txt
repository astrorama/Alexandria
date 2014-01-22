elements_subdir(ProtoZ 1.0)

elements_depends_on_subdirs(ElementsKernel)
elements_depends_on_subdirs(ChDataHandling)
elements_depends_on_subdirs(ChDataModel)
elements_depends_on_subdirs(ChTools)

find_package(Boost REQUIRED COMPONENTS program_options serialization)


#===== Libraries ===============================================================

elements_add_library(ProtoZ src/lib/*.cpp src/lib/parameter/*.cpp src/lib/matrix/*.cpp
                  LINK_LIBRARIES ${CMAKE_DL_LIBS} Boost ChTools ChDataModel ChDataHandling ElementsKernel
                  INCLUDE_DIRS Boost ChTools ChDataModel ChDataHandling ElementsKernel
                  PUBLIC_HEADERS ProtoZ)

                  
#===== Boost Tests =============================================================
# They must include also the tests/src/TestMain.cpp

elements_add_unit_test(FluxModeling_tests tests/src/*_test.cpp tests/src/TestMain.cpp
                       LINK_LIBRARIES ChDataHandling ChDataModel ChTools ProtoZ TYPE Boost)

#elements_add_unit_test(ProduceFluxMatrixToFile tests/src/ProduceFluxMatrixToFile.cpp tests/src/TestMain.cpp
#                      LINK_LIBRARIES ChDataHandling ChDataModel ChTools ProtoZ TYPE Boost)
                       
#===== Executables =============================================================

elements_add_unit_test(FluxToPdf_tests tests/src/FluxToPdf_test.cpp tests/src/TestMain.cpp
                       LINK_LIBRARIES ChDataHandling ChDataModel ChTools ProtoZ TYPE Boost
                       TIMEOUT 20)

#===== Executables =============================================================
                  
elements_add_executable(ProtoZflux src/program/ProtoZflux.cpp
                  LINK_LIBRARIES ${CMAKE_DL_LIBS} ProtoZ
                  INCLUDE_DIRS ProtoZ
                  PUBLIC_HEADERS ProtoZ)

elements_add_executable(ProtoZpdf src/program/ProtoZpdf.cpp
                  LINK_LIBRARIES ${CMAKE_DL_LIBS} ProtoZ
                  INCLUDE_DIRS ProtoZ
                  PUBLIC_HEADERS ProtoZ)

elements_add_executable(ProtoZmarg src/program/ProtoZmarg.cpp
                  LINK_LIBRARIES ${CMAKE_DL_LIBS} ProtoZ
                  INCLUDE_DIRS ProtoZ
                  PUBLIC_HEADERS ProtoZ)

elements_install_python_modules()

#-------------------------------------------------------------------------------
# CMAKE_SOURCE_DIR         = directory of the project (workspace, e.g. /.../Alexandria)
# CMAKE_CURRENT_SOURCE_DIR = directory of the package (e.g. /.../Alexandria/ChDataHandling)
#-------------------------------------------------------------------------------
