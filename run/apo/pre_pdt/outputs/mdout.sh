#!/bin/bash

# Extract heat and equil mdout info
perl process_mdout.perl $1

input=$1
preid=${input:0:2}

mv summary.ETOT     "$preid"etot.dat
mv summary.EPTOT   "$preid"eptot.dat
mv summary.EKTOT   "$preid"ektot.dat
mv summary.TEMP    "$preid"temp.dat
mv summary.PRES    "$preid"pres.dat
mv summary.VOLUME  "$preid"vol.dat
mv summary.DENSITY "$preid"density.dat

rm summary*

