
add_subdirectory(App)
if(BUILD_GUI)
    add_subdirectory(Gui)
endif(BUILD_GUI)

set(gbStructure_Scripts
    Init.py
)

if(BUILD_GUI)
    list (APPEND gbStructure_Scripts InitGui.py)
endif(BUILD_GUI)

add_custom_target(gbStructureScripts ALL
    SOURCES ${gbStructure_Scripts}
)

fc_target_copy_resource_flat(gbStructureScripts
    ${CMAKE_CURRENT_SOURCE_DIR}
    ${CMAKE_BINARY_DIR}/Mod/gbStructure
    ${gbStructure_Scripts}
)

install(
    FILES
        ${gbStructure_Scripts}
    DESTINATION
        Mod/gbStructure
)
