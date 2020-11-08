#!/bin/bash

# convierto los nombres de los archivos de Roitberg a mis nombres.
apo=pdb

for PH in 3.0 3.5 4.0 4.5 5.0 5.5 6.0 7.0
do
    cd ${PH}

    mv 30pdt.in.${PH} ${PH}pdt.in
    mv cpout.${PH} ${PH}cpout_p1_$pdb
    mv cprestrt.${PH} ${PH}cprst_p1_${pdb}.rst7
    mv mdcrd.${PH}.nc ${PH}p1_${pdb}.nc
    mv mdout.${PH} ${PH}pdt1.out
    mv rst.rst7 ${PH}p1_${pdb}.rst7

    cd ..
done

