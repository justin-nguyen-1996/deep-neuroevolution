
# quick_viz.sh

ENV='MsPacmanNoFrameskip-v4'
HDF5_FILE='Experiments/NSR_ES_MsPacman/snapshot_iter00060_rew904.h5'

python -m scripts.viz $ENV $HDF5_FILE
