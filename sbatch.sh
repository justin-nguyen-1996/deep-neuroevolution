#!/bin/bash

#----------------------------------------------------

#SBATCH -J jn_es                               # Job name
#SBATCH -o jn_es.o%j                           # Name of stdout output file
#SBATCH -e jn_es.e%j                           # Name of stderr error file
#SBATCH -p gtx                                 # Queue (partition) name
#SBATCH -N 1                                    # Total number of nodes (must be 1 for OpenMP)
#SBATCH -n 1                                    # Total number of mpi tasks (should be 1 for OpenMP)
#SBATCH --gres=gpu:1                            # Number of GPUs (per node)
#SBATCH -t 0:30:00                              # Run time (hh:mm:ss)
#SBATCH --mail-user=2014justinnguyen@gmail.com
#SBATCH --mail-type=all                         # Send email at begin and end of job

# Other commands must follow all #SBATCH directives...

./run_all.sh es configurations/frostbite_es.json  # Do not use ibrun or any other MPI launcher

#---------------------------------------------------

