"""
Policy for grid world
"""

import numpy as np


class random_policy():
    def __init__(self, grid_size):
        self.action_space = {0: "right",
                             1: "left",
                             2: "up",
                             3: "down"}
        self.action_map = {0: (0, 1),
                           1: (0, -1),
                           2: (-1, 0),
                           3: (1, 0)}
        self.pi = {}

        for i in range(grid_size):
            for j in range(grid_size):
                self.pi[(i, j)] = [1/4, 1/4, 1/4, 1/4]

    def policy_distribution(self, state, action):
        """
        Given a state return an action

        :param state: position tuple
        """

        prob_action = self.pi[state][action]
        return prob_action, self.action_map[action]

    def update_action_probability(self):
        """
        Policy Improvement step
        """
        pass
