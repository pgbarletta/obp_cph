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

Junto las trayectorias. Traiga la trayectoria pre_pdt a pdt.

En: ~/labo/20/cph_obp/run/apo/pdt$

mv ../pre_pdt/30ph/30p_apo.nc 30ph
mv ../pre_pdt/35ph/35p_apo.nc 35ph
mv ../pre_pdt/40ph/40p_apo.nc 40ph
mv ../pre_pdt/45ph/45p_apo.nc 45ph
mv ../pre_pdt/50ph/50p_apo.nc 50ph
mv ../pre_pdt/55ph/55p_apo.nc 55ph
mv ../pre_pdt/60ph/60p_apo.nc 60ph
mv ../pre_pdt/65ph/65p_apo.nc 65ph
mv ../pre_pdt/70ph/70p_apo.nc 70ph
mv ../pre_pdt/75ph/75p_apo.nc 75ph

En: ~/labo/20/cph_obp/run/ctv/pdt$

mv ../pre_pdt/30ph/30p_ctv.nc 30ph
mv ../pre_pdt/35ph/35p_ctv.nc 35ph
mv ../pre_pdt/40ph/40p_ctv.nc 40ph
mv ../pre_pdt/45ph/45p_ctv.nc 45ph
mv ../pre_pdt/50ph/50p_ctv.nc 50ph
mv ../pre_pdt/55ph/55p_ctv.nc 55ph
mv ../pre_pdt/60ph/60p_ctv.nc 60ph
mv ../pre_pdt/65ph/65p_ctv.nc 65ph
mv ../pre_pdt/70ph/70p_ctv.nc 70ph
mv ../pre_pdt/75ph/75p_ctv.nc 75ph

En: ~/labo/20/cph_obp/run/eol/pdt$

mv ../pre_pdt/30ph/30p_eol.nc 30ph
mv ../pre_pdt/35ph/35p_eol.nc 35ph
mv ../pre_pdt/40ph/40p_eol.nc 40ph
mv ../pre_pdt/45ph/45p_eol.nc 45ph
mv ../pre_pdt/50ph/50p_eol.nc 50ph
mv ../pre_pdt/55ph/55p_eol.nc 55ph
mv ../pre_pdt/60ph/60p_eol.nc 60ph
mv ../pre_pdt/65ph/65p_eol.nc 65ph
mv ../pre_pdt/70ph/70p_eol.nc 70ph
mv ../pre_pdt/75ph/75p_eol.nc 75ph

#### 6

Junto las 8 trayectorias
sed 's/30/35/g' 30_strip_cpp > ../35ph/35_strip_cpp
sed 's/30/40/g' 30_strip_cpp > ../40ph/40_strip_cpp
sed 's/30/45/g' 30_strip_cpp > ../45ph/45_strip_cpp
sed 's/30/50/g' 30_strip_cpp > ../50ph/50_strip_cpp
sed 's/30/55/g' 30_strip_cpp > ../55ph/55_strip_cpp
sed 's/30/60/g' 30_strip_cpp > ../60ph/60_strip_cpp
sed 's/30/65/g' 30_strip_cpp > ../65ph/65_strip_cpp
sed 's/30/70/g' 30_strip_cpp > ../70ph/70_strip_cpp
sed 's/30/75/g' 30_strip_cpp > ../75ph/75_strip_cpp

#### 7 

Junto las 8 trayectorias de los 10 pHs:

30ph$ cpptraj < 30_strip_cpp
35ph$ cpptraj < 35_strip_cpp
40ph$ cpptraj < 40_strip_cpp
45ph$ cpptraj < 45_strip_cpp
50ph$ cpptraj < 50_strip_cpp
55ph$ cpptraj < 55_strip_cpp
60ph$ cpptraj < 60_strip_cpp
65ph$ cpptraj < 65_strip_cpp
70ph$ cpptraj < 70_strip_cpp
75ph$ cpptraj < 75_strip_cpp

#### 8
En ~/labo/20/cph_obp/run/apo$

mv pdt/30ph/1_apo.nc all_pdt/
mv pdt/35ph/2_apo.nc all_pdt/
mv pdt/40ph/3_apo.nc all_pdt/
mv pdt/45ph/4_apo.nc all_pdt/
mv pdt/50ph/5_apo.nc all_pdt/
mv pdt/55ph/6_apo.nc all_pdt/
mv pdt/60ph/7_apo.nc all_pdt/
mv pdt/65ph/8_apo.nc all_pdt/
mv pdt/70ph/9_apo.nc all_pdt/
mv pdt/75ph/10_apo.nc all_pdt/

#### 9

Todos los pH (salvo apo/45ph, apo/75ph) tienen al menos uno de los 8 fragmentos incompletos, con 2499 frames en vez de 2500.
Lo bueno es q el frame faltante está en el archivo restart q escribe al final. Así q corro este
script de cpptraj (ej):

```
parm ../../../../top_files/apo.prmtop

trajin 35p7_apo.nc
trajin 35p7_apo.rst7
trajout t35p7_apo.nc

go
```

y luego:
```
$ mv t35p7_apo.nc 35p7_apo.nc
```

#### 10

30ph/
35ph/
40ph/
45ph/
50ph/
55ph/
60ph/
65ph/
70ph/
75ph/

