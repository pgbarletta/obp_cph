#!/bin/bash

pdb="ctv"

for i in `cat lista`
do
    ph=$(echo $i | cut -d ";" -f 1)
    phh=$(echo $i | cut -d ";" -f 2)
    mkdir ${ph}ph
    sed s/30/${ph}/g plantillas/get_p_cpp > ${ph}ph/get_p_cpp
    sed s/30/${ph}/g plantillas/get_p1_cpp > ${ph}ph/get_p1_cpp
    sed s/30/${ph}/g plantillas/get_p2_cpp > ${ph}ph/get_p2_cpp
    sed s/30/${ph}/g plantillas/get_p3_cpp > ${ph}ph/get_p3_cpp
    sed s/30/${ph}/g plantillas/get_p4_cpp > ${ph}ph/get_p4_cpp
    sed s/30/${ph}/g plantillas/get_p5_cpp > ${ph}ph/get_p5_cpp
    sed s/30/${ph}/g plantillas/get_p6_cpp > ${ph}ph/get_p6_cpp
    sed s/30/${ph}/g plantillas/get_p7_cpp > ${ph}ph/get_p7_cpp

    sed s/3.0/${phh}/g plantillas/get_p_cpp > ${ph}ph/get_p_cpp
    sed s/3.0/${phh}/g plantillas/get_p1_cpp > ${ph}ph/get_p1_cpp
    sed s/3.0/${phh}/g plantillas/get_p2_cpp > ${ph}ph/get_p2_cpp
    sed s/3.0/${phh}/g plantillas/get_p3_cpp > ${ph}ph/get_p3_cpp
    sed s/3.0/${phh}/g plantillas/get_p4_cpp > ${ph}ph/get_p4_cpp
    sed s/3.0/${phh}/g plantillas/get_p5_cpp > ${ph}ph/get_p5_cpp
    sed s/3.0/${phh}/g plantillas/get_p6_cpp > ${ph}ph/get_p6_cpp
    sed s/3.0/${phh}/g plantillas/get_p7_cpp > ${ph}ph/get_p7_cpp

    sed s/30/${ph}/g plantillas/strip_cpp > ${ph}ph/strip_cpp
    cpptraj < ${ph}ph/get_p_cpp
    cpptraj < ${ph}ph/get_p1_cpp
    cpptraj < ${ph}ph/get_p2_cpp
    cpptraj < ${ph}ph/get_p3_cpp
    cpptraj < ${ph}ph/get_p4_cpp
    cpptraj < ${ph}ph/get_p5_cpp
    cpptraj < ${ph}ph/get_p6_cpp
    cpptraj < ${ph}ph/get_p7_cpp
    cd ${ph}ph
    mv ../*nc .
    cpptraj < strip_cpp
    rm *_${pdb}.nc
    cd ..
done

exit 0
