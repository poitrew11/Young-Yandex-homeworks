# coding: utf-8

import numpy as np

n_states = 500  # for Taxi-v3
n_actions = 6   # for Taxi-v3

def select_elites(states_batch, actions_batch, reward_batch, percentile=50):
    elite_states, elite_actions = [], []
    reward_indices = [i for i, r in enumerate(reward_batch) if r >= np.percentile(reward_batch, percentile)]
    for i in reward_indices:
        elite_states.extend(states_batch[i])
        elite_actions.extend(actions_batch[i])
    return elite_states, elite_actions


def update_policy(elite_states, elite_actions, n_states=n_states, n_actions=n_actions):
    new_policy = np.zeros((n_states, n_actions))
    for s, a in zip(elite_states, elite_actions):
        new_policy[s, a] += 1
    for s in range(n_states):
        total = np.sum(new_policy[s])
        if total > 0:
            new_policy[s] /= total
        else:
            new_policy[s] = np.ones(n_actions) / n_actions
    return new_policy


def generate_session(env, policy, t_max=int(10**4)):
    states, actions = [], []
    total_reward = 0.0
    s, info = env.reset()

    for t in range(t_max):
        probabilities = policy[s]
        total = np.sum(probabilities)
        if total > 0:
            probabilities = probabilities / total
        else:
            probabilities = np.ones(len(probabilities)) / len(probabilities)
        
        a = np.random.choice(len(probabilities), p=probabilities)

        step_result = env.step(a)
        if len(step_result) == 4:
            new_s, r, done, info = step_result
        else:
            new_s, r, terminated, truncated, info = step_result
            done = terminated or truncated

        states.append(s)
        actions.append(a)
        total_reward += float(r)

        s = new_s
        if done:
            break

    return states, actions, total_reward
