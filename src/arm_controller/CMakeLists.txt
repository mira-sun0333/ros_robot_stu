cmake_minimum_required(VERSION 2.8.3)
project(arm_controller)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  geometry_msgs
  message_generation
)

add_message_files(FILES control.msg)
add_service_files(FILES move.srv)

generate_messages(DEPENDENCIES geometry_msgs)

catkin_package(CATKIN_DEPENDS message_runtime)
