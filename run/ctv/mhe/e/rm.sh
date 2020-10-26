#!/bin/bash
# En caso de q algo salga mal con la equilibración, corro esto p/ volver al estado original

ls ?equ.in | grep -v 0 | xargs rm
ls ??equ.in | grep -v 30 | xargs rm
rm *equ.out *nc *rst7

exit 0
