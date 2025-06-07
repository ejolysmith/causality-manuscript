#!/bin/bash
#SBATCH --job-name=euan_mik_job           # Job name
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=80
#SBATCH --mail-type=END,FAIL          # Mail events (NONE, BEGIN, END, FAIL, AL$
#SBATCH --mail-user=euan.joly.smith@utoronto.ca # Where to send mail
#SBATCH --time=48:00:00
#SBATCH --job-name rerun_s3
#SBATCH --output=rerun_s3_output_%j.txt
#SBATCH --mail-user=euan.joly.smith@utoronto.ca
#SBATCH --mail-type=ALL



source /scratch/smitheua/venv/bin/activate
pip install numpy



python -u s3_v1_rerun_2_e.py 80 1
python -u s3_v2_rerun_2_e.py 80 1
python -u s3_v3_rerun_2_e.py 80 1

