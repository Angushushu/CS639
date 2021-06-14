import math
import numpy as np
import matplotlib.pyplot as plt

k = 11
n = 10000 # what's n?
total_reward = [0]*k #for i arms, used by mu_h
T = [0]*k #for i arms, used by mu_h
rr_Rs = []
cum_rewards = [0]*n

def main():
    global total_reward
    global T
    for j in range(100):
        trial(j)
        total_reward = [0]*k
        T = [0]*k
    plt.xlabel('random_Rs')
    plt.ylabel('frequency')
    plt.hist(rr_Rs)
    plt.show()
    print('mean of nn_R: ', np.mean(rr_Rs))
    print('standard devietion of nn_R: ', np.std(rr_Rs))
    ts = []
    for i in range(n):
        ts.append(i+1)
    plt.xlabel('t')
    plt.ylabel('cum_rewards')
    plt.plot(ts, cum_rewards)
    plt.show()

def trial(j):
    cum_reward = 0
    rr_R = 0
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
        cum_reward += X_t
        cum_rewards[t] += cum_reward/100
        total_reward[A_t] += X_t
        rr_R += mu(0) - X_t
    # print('rr_R:', rr_R)
    rr_Rs.append(rr_R)

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