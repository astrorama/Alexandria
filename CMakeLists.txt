CMAKE_MINIMUM_REQUIRED(VERSION 2.8.5)


#---------------------------------------------------------------
# Load macros and functions for Elements-based projects
find_package(ElementsProject)
#---------------------------------------------------------------
add_definitions(-D_LIBCPP_ENABLE_CXX17_REMOVED_UNARY_BINARY)

set(CXX_SUGGEST_OVERRIDE ON
    CACHE STRING "Enable the -Wsuggest-override warning"
    FORCE)

# Declare project name and version
elements_project(Alexandria 2.29 USE Elements 6.1.2 DESCRIPTION "SDC-CH common library for the Euclid project")
