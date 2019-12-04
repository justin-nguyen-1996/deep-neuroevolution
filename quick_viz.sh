
# quick_viz.sh

# Source venv
. env_activate.sh

# MsPacman
#ENV='MsPacmanNoFrameskip-v4'
#HDF5_FILE='Experiments/NSR_ES_MsPacman/snapshot_iter00060_rew904.h5'

# Frostbite ES
#ENV='FrostbiteNoFrameskip-v4'
#HDF5_FILE='Experiments/ES_Frostbite/snapshot_iter00020_rew1006.h5'

# Frostbite normal ram state BC
#ENV='FrostbiteNoFrameskip-v4'
#HDF5_FILE='Experiments/NSR_ES_Frostbite/snapshot_iter00040_rew1271.h5'

# Frostbite BC stepping on ice
ENV='FrostbiteNoFrameskip-v4'
HDF5_FILE='Experiments/NSR_ES_Frostbite_BC_StepOnIce/snapshot_iter00035_rew2921.h5'

python3 -m scripts.viz $ENV $HDF5_FILE
