#===============================================================================
# Load elements_subdir macro here
# Examples:
#   For declaring a project module:
#         elements_subdir(ElementsExamples)
#===============================================================================
elements_subdir(Histogram)

#===============================================================================
# Load elements_depends_on_subdirs macro here
#   For creating a dependency onto an other accessible module
#         elements_depends_on_subdirs(ElementsKernel)
#===============================================================================
elements_depends_on_subdirs(ElementsKernel)
elements_depends_on_subdirs(AlexandriaKernel)

#===============================================================================
# Declare the library dependencies here
# Example:
#         elements_add_library(ElementsExamples src/Lib/*.cpp
#                     LINK_LIBRARIES Boost ElementsKernel
#                     INCLUDE_DIRS Boost ElementsKernel
#                     PUBLIC_HEADERS ElementsExamples)
#===============================================================================
elements_add_library(Histogram
        LINKER_LANGUAGE CXX
        LINK_LIBRARIES ElementsKernel GridContainer
        PUBLIC_HEADERS Histogram)

#===============================================================================
# Declare the Boost tests here
# Example:
# elements_add_unit_test(BoostClassExample tests/src/Boost/ClassExample_test.cpp
#                       EXECUTABLE BoostClassExample_test
#                       INCLUDE_DIRS ElementsExamples
#                       LINK_LIBRARIES ElementsExamples TYPE Boost)
#===============================================================================
elements_add_unit_test(BinEdges_test tests/src/BinEdges_test.cpp
        LINK_LIBRARIES Histogram
        TYPE Boost)
elements_add_unit_test(Histogram_test tests/src/Histogram_test.cpp
        LINK_LIBRARIES Histogram
        TYPE Boost)
