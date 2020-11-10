#!/bin/bash
#SBATCH --job-name=pato
#SBATCH --output=job.out 
#SBATCH --error=job.err 
#SBATCH --account=jsu101
#SBATCH --time=20:00:00
#SBATCH --nodes=3
#SBATCH --ntasks=12
#SBATCH --cpus-per-task=1
#SBATCH --gpus=12
#SBATCH --partition=gpu

module purge
module load gpu/1.0 openmpi/4.0.4 amber/20
module load slurm


export EXE=pmemd.cuda_SPFP.MPI


#$EXE -O -i 30pdt.in -p ctv.hmr.parm7 -c ctv.rst7 -x mdcrd.nc -cpin incph_ctv -cpout outcph_ctv
srun -n 12 $EXE -ng 12 -groupfile groupfile
