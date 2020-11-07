#!/bin/bash

cd 30ph
cpptraj < get_p_cpp
cpptraj < get_p1_cpp
cpptraj < get_p2_cpp
cpptraj < get_p3_cpp
cpptraj < get_p4_cpp
cpptraj < get_p5_cpp
cpptraj < get_p6_cpp
cpptraj < get_p7_cpp

cpptraj < strip_cpp
rm *_apo.nc
cd ..

cd 35ph
cpptraj < get_p_cpp
cpptraj < get_p1_cpp
cpptraj < get_p2_cpp
cpptraj < get_p3_cpp
cpptraj < get_p4_cpp
cpptraj < get_p5_cpp
cpptraj < get_p6_cpp
cpptraj < get_p7_cpp

cpptraj < strip_cpp
rm *_apo.nc
cd ..

cd 40ph
cpptraj < get_p_cpp
cpptraj < get_p1_cpp
cpptraj < get_p2_cpp
cpptraj < get_p3_cpp
cpptraj < get_p4_cpp
cpptraj < get_p5_cpp
cpptraj < get_p6_cpp
cpptraj < get_p7_cpp

cpptraj < strip_cpp
rm *_apo.nc
cd ..

cd 45ph
cpptraj < get_p_cpp
cpptraj < get_p1_cpp
cpptraj < get_p2_cpp
cpptraj < get_p3_cpp
cpptraj < get_p4_cpp
cpptraj < get_p5_cpp
cpptraj < get_p6_cpp
cpptraj < get_p7_cpp

cpptraj < strip_cpp
rm *_apo.nc
cd ..

cd 50ph
cpptraj < get_p_cpp
cpptraj < get_p1_cpp
cpptraj < get_p2_cpp
cpptraj < get_p3_cpp
cpptraj < get_p4_cpp
cpptraj < get_p5_cpp
cpptraj < get_p6_cpp
cpptraj < get_p7_cpp

cpptraj < strip_cpp
rm *_apo.nc
cd ..

cd 55ph
cpptraj < get_p_cpp
cpptraj < get_p1_cpp
cpptraj < get_p2_cpp
cpptraj < get_p3_cpp
cpptraj < get_p4_cpp
cpptraj < get_p5_cpp
cpptraj < get_p6_cpp
cpptraj < get_p7_cpp

cpptraj < strip_cpp
rm *_apo.nc
cd ..

cd 60ph
cpptraj < get_p_cpp
cpptraj < get_p1_cpp
cpptraj < get_p2_cpp
cpptraj < get_p3_cpp
cpptraj < get_p4_cpp
cpptraj < get_p5_cpp
cpptraj < get_p6_cpp
cpptraj < get_p7_cpp

cpptraj < strip_cpp
rm *_apo.nc
cd ..

cd 65ph
cpptraj < get_p_cpp
cpptraj < get_p1_cpp
cpptraj < get_p2_cpp
cpptraj < get_p3_cpp
cpptraj < get_p4_cpp
cpptraj < get_p5_cpp
cpptraj < get_p6_cpp
cpptraj < get_p7_cpp

cpptraj < strip_cpp
rm *_apo.nc
cd ..

cd 70ph
cpptraj < get_p_cpp
cpptraj < get_p1_cpp
cpptraj < get_p2_cpp
cpptraj < get_p3_cpp
cpptraj < get_p4_cpp
cpptraj < get_p5_cpp
cpptraj < get_p6_cpp
cpptraj < get_p7_cpp

cpptraj < strip_cpp
rm *_apo.nc
cd ..

cd 75ph
cpptraj < get_p_cpp
cpptraj < get_p1_cpp
cpptraj < get_p2_cpp
cpptraj < get_p3_cpp
cpptraj < get_p4_cpp
cpptraj < get_p5_cpp
cpptraj < get_p6_cpp
cpptraj < get_p7_cpp

cpptraj < strip_cpp
rm *_apo.nc
cd ..

exit 0
