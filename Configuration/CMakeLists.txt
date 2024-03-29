#===============================================================================
# Load elements_subdir macro here
# Examples:
#   For declaring a project module:
#         elements_subdir(ElementsExamples)
#===============================================================================
elements_subdir(Configuration)

#===============================================================================
# Load elements_depends_on_subdirs macro here
#   For creating a dependency onto an other accessible module
#         elements_depends_on_subdirs(ElementsKernel)
#===============================================================================
elements_depends_on_subdirs(ElementsKernel)
elements_depends_on_subdirs(SourceCatalog)
elements_depends_on_subdirs(Table)

#===============================================================================
# Add the find_package macro (a pure CMake command) here to locate the
# libraries.
# Examples:
#          find_package(CppUnit)
#===============================================================================
find_package(Boost REQUIRED COMPONENTS program_options)

#===============================================================================
# Declare the library dependencies here
# Example:
#         elements_add_library(ElementsExamples src/Lib/*.cpp
#                     LINK_LIBRARIES Boost ElementsKernel
#                     INCLUDE_DIRS Boost ElementsKernel
#                     PUBLIC_HEADERS ElementsExamples)
#===============================================================================
elements_add_library(Configuration src/lib/*.cpp
                     LINK_LIBRARIES ElementsKernel Boost SourceCatalog Table
                     PUBLIC_HEADERS Configuration)

#===============================================================================
# Declare the executables here
# Example:
# elements_add_executable(ElementsProgramExample src/Program/ProgramExample.cpp
#                        LINK_LIBRARIES Boost ElementsExamples
#                        INCLUDE_DIRS Boost ElementsExamples)
#===============================================================================

#===============================================================================
# Declare the Boost tests here
# Example:
# elements_add_unit_test(BoostClassExample tests/src/Boost/ClassExample_test.cpp
#                       EXECUTABLE BoostClassExample_test
#                       INCLUDE_DIRS ElementsExamples
#                       LINK_LIBRARIES ElementsExamples TYPE Boost)
#===============================================================================
elements_add_unit_test(Configuration_test tests/src/Configuration_test.cpp
                     LINK_LIBRARIES Configuration
                     TYPE Boost)
elements_add_unit_test(ConfigManager_test tests/src/ConfigManager_test.cpp
                     LINK_LIBRARIES Configuration
                     TYPE Boost)
elements_add_unit_test(CatalogConfig_test tests/src/CatalogConfig_test.cpp
                     LINK_LIBRARIES Configuration
                     TYPE Boost)
elements_add_unit_test(SpecZCatalogConfig_test tests/src/SpecZCatalogConfig_test.cpp
                     LINK_LIBRARIES Configuration
                     TYPE Boost)
elements_add_unit_test(PhotometryCatalogConfig_test tests/src/PhotometryCatalogConfig_test.cpp
                     LINK_LIBRARIES Configuration
                     TYPE Boost)
elements_add_unit_test(PhotometricBandMappingConfig_test tests/src/PhotometricBandMappingConfig_test.cpp
                     LINK_LIBRARIES Configuration
                     TYPE Boost)
elements_add_unit_test(ProgramOptionsHelper_test tests/src/ProgramOptionsHelper_test.cpp
                     LINK_LIBRARIES Configuration
                     TYPE Boost)

#===============================================================================
# Declare the Python programs here
# Examples :
# elements_add_python_program(PythonProgramExample
#                             ElementsExamples.PythonProgramExample)
#===============================================================================

#===============================================================================
# Use the following macro for python modules, scripts and aux files:
#  elements_install_python_modules()
#  elements_install_scripts()
#===============================================================================

#===============================================================================
# Add the elements_install_conf_files macro
# Examples:
#          elements_install_conf_files()
#===============================================================================
