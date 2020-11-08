#!/bin/bash

# Reference input file
infile=30pdt.in

for PH in {3.0,3.5,4.0,4.5,5.0,5.5,6.0,7.0}
do

    newfile=${infile%.ref}.$PH
    cp $infile $newfile
    sed -i "s/PH/$PH/g" $newfile
    mkdir $PH
    mv $newfile $PH/.
done

