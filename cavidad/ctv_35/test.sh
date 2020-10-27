#!/bin/bash

ANA2 top_cluster.c0.pdb -c obp.cfg -t 0ch
ANA2 top_cluster.c1.pdb -c obp.cfg -t 1ch
ANA2 top_cluster.c2.pdb -c obp.cfg -t 2ch

ANA2 top_cluster.c0.pdb -c obp.cfg -f 0cav
ANA2 top_cluster.c1.pdb -c obp.cfg -f 1cav
ANA2 top_cluster.c2.pdb -c obp.cfg -f 2cav



exit 0
