#!/bin/bash

pdb="ctv"
k=0
cpp_1="cluster_idx_cpp"
cpp_2="cluster_ph_cpp"

for i in `cat lista`
do
    k=`expr $k + 1`
    ph=$(echo $i | cut -d ";" -f 1)
    phh=$(echo $i | cut -d ";" -f 2)
    
    # Cluster por idx
    mkdir ${k}
    sed s/30/${ph}/g plantillas/${cpp_1} > ${k}/${cpp_1}
    sed -i s/apo/${pdb}/g ${k}/${cpp_1}
    sed -i s/${pdb}_1/${pdb}_${k}/g ${k}/${cpp_1}

    cd ${k}
    sed -i s/top_cluster/top_cluster_${k}/g ${cpp_1}
    sed -i s/avg_cluster/avg_cluster_${k}/g ${cpp_1}
    cpptraj < ${cpp_1}
    cd ..

    # Cluster por pH
    mkdir ${ph}ph
    sed s/30/${ph}/g plantillas/${cpp_2} > ${ph}ph/${cpp_2}
    sed -i s/apo/${pdb}/g ${ph}ph/${cpp_2}

    cd ${ph}ph
    sed -i s/top_cluster/top_cluster_${ph}/g ${cpp_2}
    sed -i s/avg_cluster/avg_cluster_${ph}/g ${cpp_2}
    cpptraj < ${cpp_2}
    cd ..
done

exit 0
