elements_subdir(PhysicsUtils)

elements_depends_on_subdirs(MathUtils)

#===== Libraries ===============================================================
elements_add_library(PhysicsUtils src/lib/*.cpp
					 LINK_LIBRARIES MathUtils
                     PUBLIC_HEADERS PhysicsUtils)


#===== Boost tests =============================================================
elements_add_unit_test(CosmologicalParameters_test tests/src/CosmologicalParameters_test.cpp
                       LINK_LIBRARIES PhysicsUtils TYPE Boost)

elements_add_unit_test(CosmologicalDistances_test tests/src/CosmologicalDistances_test.cpp
                       LINK_LIBRARIES PhysicsUtils MathUtils TYPE Boost)
