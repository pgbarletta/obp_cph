# 

Acá está el config viejo *bu_obp.cfg*, la selección es:
```
included_area_residues = 10 17 27 43 54 56 71 72 75 81 88 100 107 108 111 113 116
```

y la nueva selección es:
```
included_area_residues = 8 15 25 41 52 54 69 70 73 79 86 98 105 106 109 111 113
```

Esto se debe a q los volúmenes, NDD y VGV, los calculo con los PDBs cortados p/
descartar los extremos (Nterm: resi 1:2, Cterm: resi 116:119) q no fueron
incluídos en el cálculo de PCA. Esto desplaza la numeración en 2 números y me
obliga a corregir el último residuo de la selección.
