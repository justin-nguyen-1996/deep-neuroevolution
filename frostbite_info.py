import sys
import numpy as np
import gym
from matplotlib import pyplot as plt

# Obs:     (210, 160, 3)
# Actions: 18
#
# Blue water                       : [0     28    136]
# White ice                        : [214   214   214]
# Blue status HUD                  : [45    50    184]
# Light blue numbers in status HUD : [132   144   252]
# Gray igloo                       : [142   142   142]
# Black igloo door                 : [0     0     0]
# Stepped on blue ice              : [84    138   210]
#
# First row of actual game screen    : 7 (beginning of status HUD)
# First column of actual game screen : 8 (beginning of water)
# Last row of actual game screen     : 184 (end of water)
# Last column of actual game screen  : 159 (end of water)
#
# First row of igloo: 35
# Last row of igloo: 54
# Left most column of igloo: 112
# Right most column of igloo: 143
#
# First row of water : 78 (beginning of water)
# First row of ice   : 96

def printAllColors(env, ob):
    obs_shape = env.observation_space.shape
    num_actions = env.action_space.n
    for r in range(obs_shape[0]):
        for c in range(obs_shape[1]):
            print(f'color at ({r},{c}): {ob[r][c]}')

def main():
    env = gym.make("FrostbiteNoFrameskip-v4")
    ob = env.reset()
    env.render()
    obs_shape = env.observation_space.shape
    num_actions = env.action_space.n

    begin_water_row    = 78
    end_water_row      = 184+1
    begin_water_col    = 8
    end_water_col      = 159+1

    for x in range(10000):
        a = 5
        ob, r, done, _ = env.step(a)
#        num_stepped_on_ice = 0
#        for r in range(begin_water_row, end_water_row):
#            for c in range(begin_water_col, end_water_col):
#                if np.all(ob[r][c] == [84, 138, 210]):
#                    num_stepped_on_ice += 1
        num_stepped_on_ice = len(np.where(ob[begin_water_row:end_water_row] == [84, 138, 210])[0])/3
        print(f'num_stepped_on_ice: {num_stepped_on_ice}')
        env.render()
#    printAllColors(env, ob)
    while True:
        pass

main()
