import gym
env = gym.make("FrozenLake-v1",is_slippery=False)
env.reset()
env.render()

P = {0: {0: [(0.3333333333333333, 0, 0.0, False), (0.3333333333333333, 0, 0.0, False), (0.3333333333333333, 4, 0.0, False)], 1: [(0.3333333333333333, 0, 0.0, False), (0.3333333333333333, 4, 0.0, False), (0.3333333333333333, 1, 0.0, False)], 2: [(0.3333333333333333, 4, 0.0, False), (0.3333333333333333, 1, 0.0, False), (0.3333333333333333, 0, 0.0, False)], 3: [(0.3333333333333333, 1, 0.0, False), (0.3333333333333333, 0, 0.0, False), (0.3333333333333333, 0, 0.0, False)]}, 1: {0: [(0.3333333333333333, 1, 0.0, False), (0.3333333333333333, 0, 0.0, False), (0.3333333333333333, 5, 0.0, True)], 1: [(0.3333333333333333, 0, 0.0, False), (0.3333333333333333, 5, 0.0, True), (0.3333333333333333, 2, 0.0, False)], 2: [(0.3333333333333333, 5, 0.0, True), (0.3333333333333333, 2, 0.0, False), (0.3333333333333333, 1, 0.0, False)], 3: [(0.3333333333333333, 2, 0.0, False), (0.3333333333333333, 1, 0.0, False), (0.3333333333333333, 0, 0.0, False)]}, 2: {0: [(0.3333333333333333, 2, 0.0, False), (0.3333333333333333, 1, 0.0, False), (0.3333333333333333, 6, 0.0, False)], 1: [(0.3333333333333333, 1, 0.0, False), (0.3333333333333333, 6, 0.0, False), (0.3333333333333333, 3, 0.0, False)], 2: [(0.3333333333333333, 6, 0.0, False), (0.3333333333333333, 3, 0.0, False), (0.3333333333333333, 2, 0.0, False)], 3: [(0.3333333333333333, 3, 0.0, False), (0.3333333333333333, 2, 0.0, False), (0.3333333333333333, 1, 0.0, False)]}, 3: {0: [(0.3333333333333333, 3, 0.0, False), (0.3333333333333333, 2, 0.0, False), (0.3333333333333333, 7, 0.0, True)], 1: [(0.3333333333333333, 2, 0.0, False), (0.3333333333333333, 7, 0.0, True), (0.3333333333333333, 3, 0.0, False)], 2: [(0.3333333333333333, 7, 0.0, True), (0.3333333333333333, 3, 0.0, False), (0.3333333333333333, 3, 0.0, False)], 3: [(0.3333333333333333, 3, 0.0, False), (0.3333333333333333, 3, 0.0, False), (0.3333333333333333, 2, 0.0, False)]}, 4: {0: [(0.3333333333333333, 0, 0.0, False), (0.3333333333333333, 4, 0.0, False), (0.3333333333333333, 8, 0.0, False)], 1: [(0.3333333333333333, 4, 0.0, False), (0.3333333333333333, 8, 0.0, False), (0.3333333333333333, 5, 0.0, True)], 2: [(0.3333333333333333, 8, 0.0, False), (0.3333333333333333, 5, 0.0, True), (0.3333333333333333, 0, 0.0, False)], 3: [(0.3333333333333333, 5, 0.0, True), (0.3333333333333333, 0, 0.0, False), (0.3333333333333333, 4, 0.0, False)]}, 5: {0: [(1.0, 5, 0, True)], 1: [(1.0, 5, 0, True)], 2: [(1.0, 5, 0, True)], 3: [(1.0, 5, 0, True)]}, 6: {0: [(0.3333333333333333, 2, 0.0, False), (0.3333333333333333, 5, 0.0, True), (0.3333333333333333, 10, 0.0, False)], 1: [(0.3333333333333333, 5, 0.0, True), (0.3333333333333333, 10, 0.0, False), (0.3333333333333333, 7, 0.0, True)], 2: [(0.3333333333333333, 10, 0.0, False), (0.3333333333333333, 7, 0.0, True), (0.3333333333333333, 2, 0.0, False)], 3: [(0.3333333333333333, 7, 0.0, True), (0.3333333333333333, 2, 0.0, False), (0.3333333333333333, 5, 0.0, True)]}, 7: {0: [(1.0, 7, 0, True)], 1: [(1.0, 7, 0, True)], 2: [(1.0, 7, 0, True)], 3: [(1.0, 7, 0, True)]}, 8: {0: [(0.3333333333333333, 4, 0.0, False), (0.3333333333333333, 8, 0.0, False), (0.3333333333333333, 12, 0.0, True)], 1: [(0.3333333333333333, 8, 0.0, False), (0.3333333333333333, 12, 0.0, True), (0.3333333333333333, 9, 0.0, False)], 2: [(0.3333333333333333, 12, 0.0, True), (0.3333333333333333, 9, 0.0, False), (0.3333333333333333, 4, 0.0, False)], 3: [(0.3333333333333333, 9, 0.0, False), (0.3333333333333333, 4, 0.0, False), (0.3333333333333333, 8, 0.0, False)]}, 9: {0: [(0.3333333333333333, 5, 0.0, True), (0.3333333333333333, 8, 0.0, False), (0.3333333333333333, 13, 0.0, False)], 1: [(0.3333333333333333, 8, 0.0, False), (0.3333333333333333, 13, 0.0, False), (0.3333333333333333, 10, 0.0, False)], 2: [(0.3333333333333333, 13, 0.0, False), (0.3333333333333333, 10, 0.0, False), (0.3333333333333333, 5, 0.0, True)], 3: [(0.3333333333333333, 10, 0.0, False), (0.3333333333333333, 5, 0.0, True), (0.3333333333333333, 8, 0.0, False)]}, 10: {0: [(0.3333333333333333, 6, 0.0, False), (0.3333333333333333, 9, 0.0, False), (0.3333333333333333, 14, 0.0, False)], 1: [(0.3333333333333333, 9, 0.0, False), (0.3333333333333333, 14, 0.0, False), (0.3333333333333333, 11, 0.0, True)], 2: [(0.3333333333333333, 14, 0.0, False), (0.3333333333333333, 11, 0.0, True), (0.3333333333333333, 6, 0.0, False)], 3: [(0.3333333333333333, 11, 0.0, True), (0.3333333333333333, 6, 0.0, False), (0.3333333333333333, 9, 0.0, False)]}, 11: {0: [(1.0, 11, 0, True)], 1: [(1.0, 11, 0, True)], 2: [(1.0, 11, 0, True)], 3: [(1.0, 11, 0, True)]}, 12: {0: [(1.0, 12, 0, True)], 1: [(1.0, 12, 0, True)], 2: [(1.0, 12, 0, True)], 3: [(1.0, 12, 0, True)]}, 13: {0: [(0.3333333333333333, 9, 0.0, False), (0.3333333333333333, 12, 0.0, True), (0.3333333333333333, 13, 0.0, False)], 1: [(0.3333333333333333, 12, 0.0, True), (0.3333333333333333, 13, 0.0, False), (0.3333333333333333, 14, 0.0, False)], 2: [(0.3333333333333333, 13, 0.0, False), (0.3333333333333333, 14, 0.0, False), (0.3333333333333333, 9, 0.0, False)], 3: [(0.3333333333333333, 14, 0.0, False), (0.3333333333333333, 9, 0.0, False), (0.3333333333333333, 12, 0.0, True)]}, 14: {0: [(0.3333333333333333, 10, 0.0, False), (0.3333333333333333, 13, 0.0, False), (0.3333333333333333, 14, 0.0, False)], 1: [(0.3333333333333333, 13, 0.0, False), (0.3333333333333333, 14, 0.0, False), (0.3333333333333333, 15, 1.0, True)], 2: [(0.3333333333333333, 14, 0.0, False), (0.3333333333333333, 15, 1.0, True), (0.3333333333333333, 10, 0.0, False)], 3: [(0.3333333333333333, 15, 1.0, True), (0.3333333333333333, 10, 0.0, False), (0.3333333333333333, 13, 0.0, False)]}, 15: {0: [(1.0, 15, 0, True)], 1: [(1.0, 15, 0, True)], 2: [(1.0, 15, 0, True)], 3: [(1.0, 15, 0, True)]}}

def compute_sum(P, V, s, a, gamma):
    # V is a list containing the estimated value for every state
    # len(V) = nb_states
    total = 0  # state value for state s
    for p, s_prime, r, _ in P[s][a]:
        total += p * (r + gamma * V[s_prime])
    return total


import numpy as np 

def policy_iteration(env, gamma, theta):
    nb_states = env.observation_space.n
    nb_actions = env.action_space.n
    # 1. Initialization
    V = np.zeros(nb_states)
    pi = np.zeros(nb_states)
    
    while True:
    
        # 2. Policy Evaluation
        while True:
            delta = 0
            for s in range(nb_states):
                v = V[s]
             
              
                delta = max(delta, abs(v - V[s]))
            if delta < theta: break

        # 3. Policy Improvement
        policy_stable = True
 
        for s in range(nb_states):
    
            old_action = pi[s]
            pi[s] = np.argmax([compute_sum(P, V=V, s=s, a=a, gamma=gamma) for a in range(nb_actions)])
           
            if old_action != pi[s]: policy_stable = False
        if policy_stable: break
        
    return V, pi

V, pi = policy_iteration(env, gamma=1.0, theta=1e-8)

def value_iteration(env, gamma, theta):
    nb_states = env.observation_space.n
    nb_actions = env.action_space.n
    V = np.zeros(nb_states)
    
    while True:
        delta = 0
        for s in range(nb_states):
            v = V[s]
            V[s] = max([compute_sum(P, V=V, s=s, a=a, gamma=gamma) for a in range(nb_actions)])  
                
            delta = max(delta, abs(v - V[s]))
    

        if delta < theta: break
    

    # Output a deterministic policy
    pi = np.zeros(nb_states)
    for s in range(nb_states):

        pi[s] = np.argmax([compute_sum(P, V=V, s=s, a=a, gamma=gamma) for a in range(nb_actions)])

    return V, pi

V, pi = value_iteration(env, gamma=1.0, theta=1e-8)
print(V,pi)
