"""
Generalized Policy Iteration
"""

import numpy as np

from GridWorld import GridWorld
from policy import random_policy


def policy_evaluation(env, policy, gamma=1 ,tolerance = 1e-5):
    """
    Evaluate policy and return value function.

    :param env: Environment
    :param grid_size: Size of the grid
    :param policy: policy
    :param tolerance: our error tolerance
    :return: array of values for each state
    """
    def update(state,gamma,valuek):
        update_increment = 0

        # if we aren't at a terminal state compute update
        if state not in env.terminal_states:
            for a in range(len(env.action_space.items())):
                prob_s,action = policy.policy_distribution(state,a)
                possible_next_states = env.get_next_states(state,a)
                inter_sum = 0
                for snext in possible_next_states:
                    state_transition_prob = env.dynamics(snext,env.reward(action,state),state,action)
                    reward = (env.reward(action, state)+gamma*valuek[snext])
                    inter_sum += state_transition_prob*reward
                update_increment += prob_s*inter_sum
        return update_increment

    flag = True
    states = env.get_states()
    value_function = {key:0 for key in states}
    while flag:
        temp = {key:0 for key in states}
        abs_diff = -1
        for s in states:
            temp[s] = update(s,gamma,value_function)
            diff = abs(value_function[s]-temp[s])
            if abs_diff < diff:
                abs_diff = diff
        value_function = temp
        if abs_diff < tolerance:
            flag = False
    return value_function


def policy_improvement(env, policy, value_function, gamma = 1):
    policy_stable = True
    states = env.get_states()
    max_action_value = {s:[] for s in states}
    for s in states:
        for action in policy.action_map.values():
            possible_next_states = env.get_next_states(s,action)
            reward = [1]
            q_value = 0
            for s_prime in possible_next_states:
                for r in reward:
                    state_transition_prob = env.dynamics(s_prime, r, s, action)
                    discounted_reward_est = r+gamma*value_function[s]
                    q_value += state_transition_prob*discounted_reward_est
            max_action_value[s].append((action,q_value))
    possible_updates = [key for key,val in max_action_value.items() if len(val)>0]
    if len(possible_updates) > 0:
        policy.update_action_probability(possible_updates[0], max_action_value[possible_updates[0]])
        policy_stable = False
    return policy_stable


def policy_iteration(env, policy, value_function,gamma,tolerance):
    policy_stable = False
    while not policy_stable:
        value_function = policy_evaluation(env,policy,gamma,tolerance)
        policy_stable = policy_improvement(env, policy, value_function, gamma)
    return value_function, policy


def value_iteration():
    pass


if __name__ == "__main__":
    env = GridWorld(4)
    policy = random_policy(4)
    value_function = policy_evaluation(env,4,policy)
    print(value_function)
