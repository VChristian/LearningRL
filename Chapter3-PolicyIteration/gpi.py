"""
Generalized Policy Iteration
"""

import numpy as np

from GridWorld import GridWorld
from policy import random_policy


def policy_evaluation(env, grid_size, policy, tolerance = 1e-5):
    def update(state,gamma,valuek):
        update_increment = 0

        # if we aren't at a terminal state compute update
        if state not in env.terminal_states:
            for a in range(len(env.action_space.items())):
                prob_s,action = policy.policy_distribution(state,a)
                possible_next_states = env.get_next_states(state,a)

                inter_sum = 0
                for snext in possible_next_states:
                    inter_sum += env.dynamics(snext,-1,state,action)*(-1+gamma*valuek[snext[0],snext[1]])
                update_increment += prob_s*inter_sum
        return update_increment

    flag = True
    value_function = np.zeros((grid_size,grid_size))
    while flag:
        temp = np.zeros((grid_size,grid_size))
        abs_diff = -1
        for i in range(grid_size):
            for j in range(grid_size):
                temp[i,j] = update((i,j),1,value_function)
                diff = abs(value_function[i,j]-temp[i,j])
                if abs_diff < diff:
                    abs_diff = diff
        value_function = temp
        if abs_diff < tolerance:
            flag = False
    return value_function

def policy_improvement():
    pass


if __name__ == "__main__":
    env = GridWorld(4)
    policy = random_policy(4)
    value_function = policy_evaluation(env,4,policy)
    print(value_function)
