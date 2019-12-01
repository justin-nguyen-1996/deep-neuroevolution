#!/bin/sh

if [ $# != 2 ]; then
    echo 'Needs two arguments (algo and config file)'
    exit
fi

# Set variables for the arguments
ALGO=$1
EXP_FILE=$2
# Create tmux session in detached mode
tmux new -d
# Create splits in both windows
tmux new-window
tmux split-window -t :0.0 -v
tmux split-window -t :1.0 -v
# Send commands to first window's panes (redis setup)
tmux send-keys -t :0.0 'redis-server redis_config/redis_master.conf' C-m
tmux send-keys -t :0.1 'redis-server redis_config/redis_local_mirror.conf' C-m
# Send commands to second window's pane 0 (master setup for ES)
tmux send-keys -t :1.0 '. scripts/local_env_setup.sh' C-m
tmux send-keys -t :1.0 'python -m es_distributed.main master --master_socket_path /tmp/es_redis_master.sock --algo '$ALGO' --exp_file '"$EXP_FILE" C-m
# Send commands to second window's pane 1 (worker setup for ES)
tmux send-keys -t :1.1 '. scripts/local_env_setup.sh' C-m
tmux send-keys -t :1.1 'sleep 30' C-m
tmux send-keys -t :1.1 'python -m es_distributed.main workers --master_host localhost --relay_socket_path /tmp/es_redis_relay.sock --algo '$ALGO' --num_workers 40' C-m
# Attach to tmux session
#tmux attach # NOTE: don't attach because TACC servers don't have tty terminals
