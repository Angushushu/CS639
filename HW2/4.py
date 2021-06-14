import math
import numpy as np
import matplotlib.pyplot as plt

k = 11
n = 10000 # what's n?
total_reward = [0]*k #for i arms, used by mu_h
T = [0]*k #for i arms, used by mu_h

def main():
    for t in range(n):
        A_t = None
        X_t = None
        if t < k:
            A_t = t
        else:
            max_mu_h = -99
            for i in range(k):
                if mu_h(i) > max_mu_h:
                    A_t = i
                    max_mu_h = mu_h(i)
        T[A_t] += 1
        X_t = get_reward(A_t)
        total_reward[A_t] += X_t
        if t < 20:
            print(t+1, ' ', A_t+1, ' ', X_t, ' ', T[A_t], ' ', mu_h(A_t))

def mu_h(i): #mu_i(t-1)
    return 0 if total_reward[i] == 0 else total_reward[i]/T[i]

# environment
def get_reward(i):
    return np.random.default_rng().normal(mu(i), 1)

def mu(i):
    i += 1 #start from 1
    return (k-i)/(k-1)

if __name__ == "__main__":
    main()