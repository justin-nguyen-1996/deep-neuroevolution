#!/bin/sh
#NAME=exp_`date "+%m_%d_%H_%M_%S"`
#ALGO=$1
#EXP_FILE=$2
#tmux new -s $NAME -d
#tmux send-keys -t $NAME '. scripts/local_env_setup.sh' C-m
#tmux send-keys -t $NAME 'python -m es_distributed.main master --master_socket_path /tmp/es_redis_master.sock --algo '$ALGO' --exp_file '"$EXP_FILE" C-m
#tmux split-window -t $NAME
#tmux send-keys -t $NAME '. scripts/local_env_setup.sh' C-m
#tmux send-keys -t $NAME 'python -m es_distributed.main workers --master_host localhost --relay_socket_path /tmp/es_redis_relay.sock --algo '$ALGO' --num_workers 40' C-m
#tmux a -t $NAME

# wget download.redis.io/releases/redis-4.0.8.tar.gz

### ES
#. scripts/local_env_setup.sh
#python -m es_distributed.main master --master_socket_path /tmp/es_redis_master.sock --algo es --exp_file configurations/frostbite_es.json

### GA (doesn't work)
#. scripts/local_env_setup.sh
#python -m es_distributed.main master --master_socket_path /tmp/es_redis_master.sock --algo ga --exp_file configurations/frostbite_ga.json

ALGO=$1
EXP_FILE=$2
. scripts/local_env_setup.sh
python -m es_distributed.main master --master_socket_path /tmp/es_redis_master.sock --algo "$ALGO" --exp_file "$EXP_FILE"
