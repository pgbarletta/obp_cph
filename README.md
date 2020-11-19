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
```

P/ q los cpouts, en vez de estar ordenados según réplica, lo estén en base
a pH.

##### Luego, obtengo los pKas y las poblaciones de c/ aminoácido: (ej. con la prote "apo")

cphstats -i ~/labo/20/cph_obp/top_files/incph_apo reordered_cpouts.pH_20 -o 20_pka --population 20_pop 
cphstats -i ~/labo/20/cph_obp/top_files/incph_apo reordered_cpouts.pH_25 -o 25_pka --population 25_pop 
cphstats -i ~/labo/20/cph_obp/top_files/incph_apo reordered_cpouts.pH_30 -o 30_pka --population 30_pop 
cphstats -i ~/labo/20/cph_obp/top_files/incph_apo reordered_cpouts.pH_35 -o 35_pka --population 35_pop 
cphstats -i ~/labo/20/cph_obp/top_files/incph_apo reordered_cpouts.pH_40 -o 40_pka --population 40_pop 
cphstats -i ~/labo/20/cph_obp/top_files/incph_apo reordered_cpouts.pH_45 -o 45_pka --population 45_pop 
cphstats -i ~/labo/20/cph_obp/top_files/incph_apo reordered_cpouts.pH_50 -o 50_pka --population 50_pop 
cphstats -i ~/labo/20/cph_obp/top_files/incph_apo reordered_cpouts.pH_55 -o 55_pka --population 55_pop 
cphstats -i ~/labo/20/cph_obp/top_files/incph_apo reordered_cpouts.pH_60 -o 60_pka --population 60_pop 
cphstats -i ~/labo/20/cph_obp/top_files/incph_apo reordered_cpouts.pH_65 -o 65_pka --population 65_pop 
cphstats -i ~/labo/20/cph_obp/top_files/incph_apo reordered_cpouts.pH_70 -o 70_pka --population 70_pop 
cphstats -i ~/labo/20/cph_obp/top_files/incph_apo reordered_cpouts.pH_75 -o 75_pka --population 75_pop 

## Notas

##### Residuos protonables:

4   GL4
5   GL4
11  HIP
13  GL4
20  GL4
24  AS4
30  AS4
33  GL4
37  AS4
39  GL4
40  AS4
48  GL4
58  AS4
73  GL4
77  AS4
78  GL4
87  AS4
93  GL4
94  GL4
97  HIP
117 AS4

##### 5

# Rehago todo

 - 1e/ 2e/ y pre_pdt/ ya no valen más
 - Tengo un bajón de Epotencial en la equilibración pq hice el calentamiento a V=cte y luego saqué los restraints
    a vol constante también. Finalmente pasé a Pr=cte p/ la equilibración y ahí se acomodó la caja (achicó, aumentó densidad)
    No creo q sea pbma.
 - Ahora hay nuevas topologías `apo.hmr.parm7` q tienen hydrogen mass reweighted. Permiten correr a 4fs
