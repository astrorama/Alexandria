elements_subdir(PhzExecutables 0.1)

elements_depends_on_subdirs(ElementsKernel)
elements_depends_on_subdirs(ChMatrix)
elements_depends_on_subdirs(ChCatalog)
elements_depends_on_subdirs(ChMath)
elements_depends_on_subdirs(PhzConfiguration)
elements_depends_on_subdirs(PhzDataModel)
elements_depends_on_subdirs(PhzModeling)

find_package(Boost REQUIRED COMPONENTS program_options serialization)

#===== Executables =============================================================
                  
elements_add_executable(CreateModelPhotometry src/program/CreateModelPhotometry.cpp
                  LINK_LIBRARIES Boost ElementsKernel PhzConfiguration ChCatalog ChMath
                  INCLUDE_DIRS Boost ElementsKernel PhzConfiguration PhzDataModel ChMatrix PhzModeling)
