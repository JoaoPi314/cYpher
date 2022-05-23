cmake_minimum_required(VERSION 3.15)
project(tdd_cesar)
# Generate the library libcesar
add_library(libcesar src/cesar.cpp)
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/src/)
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/include/)
# For Google Test
enable_testing()
add_subdirectory(tests)