elements_subdir(PhzModeling 0.1)

elements_depends_on_subdirs(ElementsKernel)
elements_depends_on_subdirs(PhzConfiguration)

find_package(Boost REQUIRED COMPONENTS program_options)

#===== Executables =============================================================
                  
elements_add_executable(CreateModelPhotometry src/program/CreateModelPhotometry.cpp
                  LINK_LIBRARIES ElementsKernel PhzConfiguration
                  INCLUDE_DIRS ElementsKernel PhzConfiguration)
