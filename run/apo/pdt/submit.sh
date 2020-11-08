#!/bin/bash
#SBATCH --job-name=pato
#SBATCH --output=job.out 
#SBATCH --error=job.err 
#SBATCH --account=jsu101
#SBATCH --time=15:00:00
#SBATCH --nodes=2
#SBATCH --ntasks=8
#SBATCH --cpus-per-task=1
#SBATCH --gpus=8
#SBATCH --partition=gpu

module purge
module load gpu/1.0 openmpi/4.0.4 amber/20
module load slurm


export EXE=pmemd.cuda_SPFP.MPI


#$EXE -O -i 30pdt.in -p ctv.hmr.parm7 -c ctv.rst7 -x mdcrd.nc -cpin incph_ctv -cpout outcph_ctv
srun -n 8 $EXE -ng 8 -groupfile groupfile
