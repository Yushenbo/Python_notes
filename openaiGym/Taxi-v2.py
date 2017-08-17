#-*- coding:utf-8 -*-
#########################################################################
# File Name: Texi-v1.py
# Author: Nichol.Shen
# mail: nichol_shen@yahoo.com
#########################################################################
#!/usr/bin/env python3

import gym
env = gym.make('Taxi-v2')
obersvation = env.reset()
for _ in range(10000):
    env.render()
    action = env.action_space.sample()
    observation, reward, done, info = env.step(action)
