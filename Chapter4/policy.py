"""
Policy file for DP.

All policies must hve the following:

policy_distribution function: return p(a|s), a

update_action_probability: update internal state

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

    def update_action_probability(self, state, actions):
        """
        Policy Improvement step
        """
        inverted_action_map = {val:key for key,val in self.action_map.items()}
        max_action = max(actions,key=lambda x:x[1])
        all_actions_updates = [pair[0] for pair in actions if pair[1]==max_action]
        prob_dist = self.pi[state]
        for a in all_actions_updates:
            action_index = inverted_action_map[a]
            prob_dist[action_index] += 1
        normalization_const = sum(prob_dist)
        for i in range(len(prob_dist)):
            prob_dist[i] /= normalization_const
        self.pi[state] = prob_dist

