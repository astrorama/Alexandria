elements_subdir(PhzExecutables 0.1)

elements_depends_on_subdirs(ElementsKernel)
elements_depends_on_subdirs(GridContainer)
elements_depends_on_subdirs(SourceCatalog)
elements_depends_on_subdirs(ChMath)
elements_depends_on_subdirs(PhzConfiguration)
elements_depends_on_subdirs(PhzDataModel)
elements_depends_on_subdirs(PhzModeling)
elements_depends_on_subdirs(PhzLikelihood)

find_package(Boost REQUIRED COMPONENTS program_options serialization)

#===== Executables =============================================================
                  
elements_add_executable(CreateModelPhotometry src/program/CreateModelPhotometry.cpp
                  LINK_LIBRARIES Boost ElementsKernel PhzConfiguration SourceCatalog ChMath
                  INCLUDE_DIRS Boost ElementsKernel PhzConfiguration PhzDataModel GridContainer PhzModeling)
                  
elements_add_executable(PhotometryToLikelihood src/program/PhotometryToLikelihood.cpp
                  LINK_LIBRARIES Boost ElementsKernel PhzConfiguration SourceCatalog ChMath
                  INCLUDE_DIRS Boost ElementsKernel PhzConfiguration PhzDataModel GridContainer PhzLikelihood)
                  
elements_add_executable(ExportModelDataset src/program/ExportModelDataset.cpp
                  LINK_LIBRARIES Boost ElementsKernel PhzConfiguration SourceCatalog ChMath
                  INCLUDE_DIRS Boost ElementsKernel PhzConfiguration PhzDataModel GridContainer PhzModeling)

#---Python modules, Scripts, conf and aux files --------------------------------

elements_install_conf_files()
elements_install_python_modules()
elements_install_scripts()
