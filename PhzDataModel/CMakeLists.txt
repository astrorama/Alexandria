elements_subdir(PhzDataModel 0.1)

elements_depends_on_subdirs(ChCatalog)
elements_depends_on_subdirs(ChMatrix)
elements_depends_on_subdirs(XYDataset)

find_package(Boost REQUIRED COMPONENTS serialization)