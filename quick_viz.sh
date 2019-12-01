
# quick_viz.sh

ENV='MsPacmanNoFrameskip-v4'
HDF5_FILE='Experiments/NSR_ES_MsPacman/snapshot_iter00015_rew515.h5'

python -m scripts.viz $ENV $HDF5_FILE
