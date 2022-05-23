cmake_minimum_required(VERSION 3.15)
project(tdd_caesar)
# Generate the library libcaesar
add_library(libcaesar src/caesar.cpp)
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/src/)
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/include/)
# For Google Test
enable_testing()
add_subdirectory(tests)