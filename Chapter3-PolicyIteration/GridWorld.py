"""
Implementation of grid world
"""

import numpy as np


class GridWorld():
    def __init__(self, grid_size):

        # Grid information
        self.grid_size = grid_size
        self.grid = np.zeros((grid_size, grid_size))
        self.terminal_states = [(0, 0), (grid_size-1, grid_size-1)]

        # initial positio
        self.position = None

        self.action_space = {0: "right",
                        1: "left",
                        2: "up",
                        3: "down"}

        self.action_map = {0: (0, 1),
                           1: (0, -1),
                           2: (-1, 0),
                           3: (1, 0)}
    
    def outside_grid(self,state):
        if state[0] > self.grid_size-1:
            return True
        elif state[0] < 0:
            return True
        elif state[1] > self.grid_size-1:
            return True
        elif state[1] < 0:
            return True
        else:
            return False

    def dynamics(self, snext,reward,sk,ak):
        
        # are we within the jump
        position_difference_x = snext[0]-sk[0]
        position_difference_y = snext[1]-sk[1]
        if (position_difference_x > 1 or position_difference_y > 1) or (position_difference_x > 1 and position_difference_y > 1):
                return 0
        
        # does our action lead us to this state
        action_taken_state = (sk[0]+ak[0], sk[1]+ak[1])
        if self.outside_grid(action_taken_state):
            action_taken_state = sk
        
        # correct snext
        if snext != action_taken_state:
            return 0

        return 1

    def get_next_states(self, state, action):
        action = self.action_map[action]
        action_taken_state = (state[0]+action[0], state[1]+action[1])
        if self.outside_grid(action_taken_state):
            action_taken_state = state
        return [action_taken_state]







