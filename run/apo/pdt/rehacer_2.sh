#!/bin/bash

# convierto los nombres de los archivos de Roitberg a mis nombres.
pdb1=apo
pdb2=apo
k=1

for PH in 3.5 4.0 4.5 5.0 5.5 6.0 7.0
do
    k=`expr $k + 1`

    sed s/3.0/${PH}/g 3.0/strip_cpp > ${PH}/strip_cpp
    sed -i s/apo_1/apo_${k}/g ${PH}/strip_cpp

    cd ${PH}
    cpptraj < strip_cpp
    cd ..
done

