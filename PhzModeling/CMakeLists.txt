elements_subdir(PhzModeling 0.1)

elements_depends_on_subdirs(ElementsKernel)
elements_depends_on_subdirs(XYDataset)
elements_depends_on_subdirs(GridContainer)
elements_depends_on_subdirs(SourceCatalog)
elements_depends_on_subdirs(MathUtils)
elements_depends_on_subdirs(PhzConfiguration)
elements_depends_on_subdirs(PhzDataModel)

find_package(Boost REQUIRED COMPONENTS serialization)

#===== Boost tests =============================================================

elements_add_unit_test(RedshiftFunctor_test tests/src/RedshiftFunctor_test.cpp
                       LINK_LIBRARIES XYDataset TYPE Boost)
