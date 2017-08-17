#-*- coding:utf-8 -*-
#########################################################################
# File Name: FrozenLake-v0.py
# Author: Nichol.Shen
# mail: nichol_shen@yahoo.com
#########################################################################
#!/usr/bin/env python3

import gym 
from gym import wrappers

env = gym.make('FrozenLake-v0')
env = wrappers.Monitor(env, './gym-results')
observation = env.reset()
for _ in range(1000):
    env.render()
    action = env.action_space.sample()
    observation, reward, done, info = env.step(action)
    if done:
        env.reset()

env.close()
gym.upload('./gym-results',api_key='sk_FYp0Gc1dQU69epifs7ZE6w')

