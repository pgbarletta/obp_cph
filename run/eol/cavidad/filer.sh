#!/bin/bash

pdb="eol"
k=0

for i in `cat lista`
do
    k=`expr $k + 1`
    ph=$(echo $i | cut -d ";" -f 1)
    phh=$(echo $i | cut -d ";" -f 2)
    
    # vol por idx
#    mkdir ${k}
    cd ${k}
    ANA2 ../plantillas/fix_cut_top_apo_10.pdb -c ../plantillas/obp.cfg -d /home/pbarletta/labo/20/cph_obp/run/${pdb}/pdt/${ph}ph/${pdb}_${k}.nc -o vol_trj_${pdb}_${k}
    cd ..

    # vol por pH
#    mkdir ${ph}ph
    cd ${ph}ph
    ANA2 ../plantillas/fix_cut_top_apo_10.pdb -c ../plantillas/obp.cfg -d /home/pbarletta/labo/20/cph_obp/run/${pdb}/all_pdt/${ph}ph/${pdb}_${ph}.nc -o vol_trj_${pdb}_${ph}
    cd ..
done

exit 0