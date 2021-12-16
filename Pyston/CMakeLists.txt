CMAKE_MINIMUM_REQUIRED(VERSION 2.8.5)

#===============================================================================
# Load elements_subdir macro here
# Examples:
#   For declaring a project module:
#         elements_subdir(ElementsExamples)
#===============================================================================
elements_subdir(Pyston)

#===============================================================================
# Load elements_depends_on_subdirs macro here
#   For creating a dependency onto an other accessible module
#         elements_depends_on_subdirs(ElementsKernel)
#===============================================================================
elements_depends_on_subdirs(ElementsKernel)

#===============================================================================
# Add the find_package macro (a pure CMake command) here to locate the
# libraries.
# Examples:
#          find_package(CppUnit)
#===============================================================================
find_package(PythonInterp ${PYTHON_EXPLICIT_VERSION} REQUIRED)
find_package(PythonLibs ${PYTHON_EXPLICIT_VERSION} REQUIRED)
find_package(BoostPython ${PYTHON_EXPLICIT_VERSION})
find_package(Boost 1.53 REQUIRED COMPONENTS filesystem timer)
find_package(PythonInterp ${PYTHON_EXPLICIT_VERSION} REQUIRED)
find_package(PythonLibs ${PYTHON_EXPLICIT_VERSION} REQUIRED)
find_package(BoostPython ${PYTHON_EXPLICIT_VERSION})

#===============================================================================
# Declare the library dependencies here
# Example:
#         elements_add_library(ElementsExamples src/Lib/*.cpp
#                     INCLUDE_DIRS Boost ElementsKernel
#                     LINK_LIBRARIES Boost ElementsKernel
#                     PUBLIC_HEADERS ElementsExamples)
#===============================================================================
elements_add_library(Pyston src/lib/*.cpp
        INCLUDE_DIRS
          Boost BoostPython
          PythonLibs PythonInterp
          ElementsKernel SEImplementation
        LINK_LIBRARIES
          Boost BoostPython
          PythonLibs PythonInterp
          ElementsKernel
        PUBLIC_HEADERS Pyston)

#===============================================================================
# Declare the executables here
# Example:
# elements_add_executable(ElementsProgramExample src/Program/ProgramExample.cpp
#                        INCLUDE_DIRS Boost ElementsExamples
#                        LINK_LIBRARIES Boost ElementsExamples)
#===============================================================================
#elements_add_executable(Example src/program/Example.cpp
#        INCLUDE_DIRS ElementsKernel Pyston
#        LINK_LIBRARIES ElementsKernel Pyston)

#===============================================================================
# Declare the Boost tests here
# Example:
# elements_add_unit_test(BoostClassExample tests/src/Boost/ClassExample_test.cpp
#                       EXECUTABLE BoostClassExample_test
#                       INCLUDE_DIRS ElementsExamples
#                       LINK_LIBRARIES ElementsExamples TYPE Boost)
#===============================================================================
elements_add_unit_test(PystonAttributeSetTest tests/src/AttributeSet_test.cpp
        LINK_LIBRARIES Pyston
        TYPE Boost)
elements_add_unit_test(PystonBinaryOperatorTest tests/src/BinaryOperator_test.cpp
        LINK_LIBRARIES Pyston
        TYPE Boost)
elements_add_unit_test(PystonCastTest tests/src/Cast_test.cpp
        LINK_LIBRARIES Pyston
        TYPE Boost)
elements_add_unit_test(PystonConstantTest tests/src/Constant_test.cpp
        LINK_LIBRARIES Pyston
        TYPE Boost)
elements_add_unit_test(PystonFullChainTest tests/src/FullChain_test.cpp
        LINK_LIBRARIES Pyston
        TYPE Boost)
elements_add_unit_test(PystonExpressionTreeBuilderTest tests/src/ExpressionTreeBuilder_test.cpp
        LINK_LIBRARIES Pyston
        TYPE Boost)
elements_add_unit_test(PystonMultithreadTest tests/src/Multithread_test.cpp
        LINK_LIBRARIES Pyston
        TYPE Boost)
elements_add_unit_test(PystonUnaryOperatorTest tests/src/UnaryOperator_test.cpp
        LINK_LIBRARIES Pyston
        TYPE Boost)

#===============================================================================
# Use the following macro for python modules, scripts and aux files:
#  elements_install_python_modules()
#  elements_install_scripts()
#===============================================================================

#===============================================================================
# Declare the Python programs here
# Examples :
# elements_add_python_program(PythonProgramExample
#                             ElementsExamples.PythonProgramExample)
#===============================================================================

#===============================================================================
# Add the elements_install_conf_files macro
# Examples:
#          elements_install_conf_files()
#===============================================================================
# elements_install_conf_files()
