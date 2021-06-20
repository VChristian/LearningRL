#!/usr/bin/env python3

"""
K-Bandit environment.
"""

import numpy as np

class kBanditEnv():
    def __init__(self, k, init_reward_distribution=np.random.normal, reward_var=1):
        self.k = k
        self.reward_init = init_reward_distribution
        self.reward_distribution = np.random.normal
        self.reward_variance = reward_var
        self.levers = [None]*k

    def reset(self):
        for i in range(self.k):
            self.levers[i] = self.reward_init()

    def step(self, action):
        return self.reward_distribution(self.levers[action], scale=self.reward_variance)
