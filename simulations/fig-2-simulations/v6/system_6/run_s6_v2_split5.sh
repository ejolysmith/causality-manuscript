#!/bin/bash
#SBATCH --job-name=euan_mik_job           # Job name
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=40
#SBATCH --mail-type=END,FAIL          # Mail events (NONE, BEGIN, END, FAIL, AL$
#SBATCH --mail-user=euan.joly.smith@utoronto.ca # Where to send mail
#SBATCH --time=24:00:00 
#SBATCH --job-name s6_v2_split5
#SBATCH --output=s6_v2_output_%j.txt
#SBATCH --mail-user=euan.joly.smith@utoronto.ca
#SBATCH --mail-type=ALL



#source /scratch/smitheua/venv/bin/activate
#pip install numpy

module load NiaEnv/2019b

module load python/3.8.5

#module load scipy-stack



python -u s6_v2_e.py 40 5
