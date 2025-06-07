#!/bin/bash
#SBATCH --partition=generalq          # Queue
#SBATCH --job-name=euan_mik_job           # Job name
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=20
#SBATCH --mail-type=END,FAIL          # Mail events (NONE, BEGIN, END, FAIL, AL$
#SBATCH --mail-user=euan.joly.smith@utoronto.ca # Where to send mail
#SBATCH --mem-per-cpu=18M
#SBATCH --time=5-00   #5 days 0 hours
#SBATCH --job-name s2_v2_split3
#SBATCH --output=s2_v2_output_%j.txt
#SBATCH --mail-user=euan.joly.smith@utoronto.ca
#SBATCH --mail-type=ALL



source /scratch/smitheua/venv/bin/activate
#pip install numpy
#module load python3
#module load scipy-stack



python3 -u s2_v2_e.py 20 3
