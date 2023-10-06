CMAKE_MINIMUM_REQUIRED(VERSION 2.8.12)


#---------------------------------------------------------------
# Load macros and functions for Elements-based projects
find_package(ElementsProject)
#---------------------------------------------------------------
add_definitions(-D_LIBCPP_ENABLE_CXX17_REMOVED_UNARY_BINARY)

set(CXX_SUGGEST_OVERRIDE ON
    CACHE STRING "Enable the -Wsuggest-override warning"
    FORCE)

# Declare project name and version
elements_project(Alexandria 2.31.0 USE Elements 6.2.3 DESCRIPTION "SDC-CH common library for the Euclid project")
