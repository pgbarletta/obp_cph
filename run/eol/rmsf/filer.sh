#!/bin/bash

pdb="eol"
k=0
cpp_rmsf="rmsf_cpp"

for i in `cat lista`
do
    k=`expr $k + 1`
    ph=$(echo $i | cut -d ";" -f 1)
    phh=$(echo $i | cut -d ";" -f 2)
    
    # PCA por idx
    mkdir ${k}
    
    sed s/30/${ph}/g plantillas/${cpp_rmsf} > ${k}/${cpp_rmsf}
    sed -i s/apo_1/${pdb}_${k}/g ${k}/${cpp_rmsf}
    sed -i s/apo/${pdb}/g ${k}/${cpp_rmsf}
    sed -i "s/\/1\//\/${k}\//g" ${k}/${cpp_rmsf}

    cd ${k}
    cpptraj < ${cpp_pca}
    cpptraj < ${cpp_fit}
    cpptraj < ${cpp_rmsf}
    cd ..

    # PCA por pH
    mkdir ${ph}ph

    sed s/30/${ph}/g plantillas/${cpp_rmsf} > ${ph}ph/${cpp_rmsf}
    sed -i s/apo_1/${pdb}_${ph}/g ${ph}ph/${cpp_rmsf}
    sed -i s/apo/${pdb}/g ${ph}ph/${cpp_rmsf}
    sed -i "s/\/1\//\/${ph}ph\//g" ${ph}ph/${cpp_rmsf}
    
    cd ${ph}ph
    cpptraj < ${cpp_pca}
    cpptraj < ${cpp_fit}
    cpptraj < ${cpp_rmsf}
    cd ..
done

exit 0
