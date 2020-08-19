# CpH OBP

## Corrigiendo strip

Mirando ```apo/mhe/e``` me di cuenta de que en los archivos ```strip_cpp_in``` me
faltó limpiar sodio y las corridas sin agua tienen 1 átomo de sodio. Por eso tuve
q crear una topología con 1 átomo de sodio y correr *cpp* cpptraj scripts para
limpiar las trayectorias

## pH constante

Luego de la corrida, mover todos los \*out al dir outputs/ (como siempre)
y todos los *cpout* a cph_outputs/ y ahí hacer:
```
cphstats --fix-remd reordered_cpouts *cpout*
mv reordered_cpouts.pH_3.00 reordered_cpouts.pH_30
mv reordered_cpouts.pH_3.50 reordered_cpouts.pH_35
mv reordered_cpouts.pH_4.00 reordered_cpouts.pH_40
mv reordered_cpouts.pH_4.50 reordered_cpouts.pH_45
mv reordered_cpouts.pH_5.00 reordered_cpouts.pH_50
mv reordered_cpouts.pH_5.50 reordered_cpouts.pH_55
mv reordered_cpouts.pH_6.00 reordered_cpouts.pH_60
mv reordered_cpouts.pH_6.50 reordered_cpouts.pH_65
mv reordered_cpouts.pH_7.00 reordered_cpouts.pH_70
mv reordered_cpouts.pH_7.50 reordered_cpouts.pH_75
```

P/ q los cpouts, en vez de estar ordenados según réplica, lo estén en base
a pH.

##### Luego, obtengo los pKas y las poblaciones de c/ aminoácido: (ej. con la prote "apo")

cphstats -i ~/labo/17/cph_obp/top_files/incph_apo reordered_cpouts.pH_30 -o 30_pka --population 30_pop 
cphstats -i ~/labo/17/cph_obp/top_files/incph_apo reordered_cpouts.pH_35 -o 35_pka --population 35_pop 
cphstats -i ~/labo/17/cph_obp/top_files/incph_apo reordered_cpouts.pH_40 -o 40_pka --population 40_pop 
cphstats -i ~/labo/17/cph_obp/top_files/incph_apo reordered_cpouts.pH_45 -o 45_pka --population 45_pop 
cphstats -i ~/labo/17/cph_obp/top_files/incph_apo reordered_cpouts.pH_50 -o 50_pka --population 50_pop 
cphstats -i ~/labo/17/cph_obp/top_files/incph_apo reordered_cpouts.pH_55 -o 55_pka --population 55_pop 
cphstats -i ~/labo/17/cph_obp/top_files/incph_apo reordered_cpouts.pH_60 -o 60_pka --population 60_pop 
cphstats -i ~/labo/17/cph_obp/top_files/incph_apo reordered_cpouts.pH_65 -o 65_pka --population 65_pop 
cphstats -i ~/labo/17/cph_obp/top_files/incph_apo reordered_cpouts.pH_70 -o 70_pka --population 70_pop 
cphstats -i ~/labo/17/cph_obp/top_files/incph_apo reordered_cpouts.pH_75 -o 75_pka --population 75_pop 

## Notas

##### 1  Nueva selección:
4
5
11
13
20
24
30
33
37
39
40
47
48
52
58
73
77
78
87
94
97
117

##### 2 Residuos protonables:
GL4 4                                   
GL4 5                                     
LYS 7                                     
HIP 11 
GL4 13 
LYS 18 
GL4 20 
AS4 24 
LYS 27 
AS4 30 
GL4 33 
AS4 37 
GL4 39 
AS4 40 
LYS 41 
LYS 42 
GL4 48 
LYS 52 
AS4 58 
LYS 59 
LYS 64 
LYS 69 
GL4 73 
AS4 77 
GL4 78 
LYS 82 
AS4 87 
GL4 93 
GL4 94 
HIP 97 
LYS 99 
LYS 102
LYS 109
LYS 111
LYS 114
AS4 117

##### 5
