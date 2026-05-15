cmake_minimum_required(VERSION 2.8.3)

project(oryxbot_description)

find_package(catkin REQUIRED
	geometry_msgs
	roscpp
	std_msgs 
	std_srvs
	message_generation
	arm_controller
	tf2_ros
	tf
)
add_service_files(
	FILES
	FK.srv
	IK.srv
)
generate_messages(
	DEPENDENCIES
	geometry_msgs std_msgs
)
catkin_package(
   CATKIN_DEPENDS geometry_msgs roscpp std_msgs std_srvs message_runtime
)

include_directories(
  include
  ${catkin_INCLUDE_DIRS}
)

add_executable(fk_swiftpro src/fk_swiftpro.cpp)
add_dependencies(fk_swiftpro ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
target_link_libraries(fk_swiftpro ${catkin_LIBRARIES})

add_executable(ik_swiftpro src/ik_swiftpro.cpp)
add_dependencies(ik_swiftpro ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
target_link_libraries(ik_swiftpro ${catkin_LIBRARIES})

add_executable(pose_swiftpro src/pose_swiftpro.cpp)
add_dependencies(pose_swiftpro ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
target_link_libraries(pose_swiftpro ${catkin_LIBRARIES}) 

install(TARGETS fk_swiftpro ik_swiftpro pose_swiftpro
  RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

install(DIRECTORY include/
  DESTINATION ${CATKIN_PACKAGE_INCLUDE_DESTINATION}
  FILES_MATCHING PATTERN "*.h" PATTERN "*.hh"
  PATTERN ".svn" EXCLUDE
)

catkin_install_python(PROGRAMS
  scripts/draw_ma.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

foreach(dir config launch maps meshes scripts xacro srv world)
  install(DIRECTORY ${dir}/
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/${dir})
endforeach(dir)
