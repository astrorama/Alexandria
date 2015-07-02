elements_subdir(PhysicsUtils)

elements_depends_on_subdirs(MathUtils)

#===== Libraries ===============================================================
elements_add_library(PhysicsUtils src/lib/*.cpp
					 LINK_LIBRARIES MathUtils
                     PUBLIC_HEADERS PhysicsUtils)


#===== Boost tests =============================================================
elements_add_unit_test(Cosmology_test tests/src/Cosmology_test.cpp
                       LINK_LIBRARIES PhysicsUtils MathUtils TYPE Boost)
