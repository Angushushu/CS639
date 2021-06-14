import math
import numpy as np
import matplotlib.pyplot as plt

k = 11
n = 10000 # what's n?
total_reward = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] #for i arms, used by mu_h
T = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] #for i arms, used by mu_h

def main():
    plt.ylabel('i')
    plt.xlabel('t')
    for t in range(n):
        A_t = argmax() # choose i for this t, notice it starts from 0
        X_t = get_reward(A_t)
        total_reward[A_t] += X_t #get rewards and update mu_h
        T[A_t] += 1
        #Q1
        if t < 20:
            print(t+1, ' ', A_t+1, ' ', mu(A_t), ' ', X_t, ' ', T[A_t], ' ', mu_h(A_t), ' ', UCB(A_t)) # this UCB is w/ t instead of t-1
        plt.plot(t+1, A_t+1, 'o', markersize=1, color='black')
    
    #Q2
    mu_hs = []
    UCBs = []
    for i in range(k):
        mu_hs.append(mu_h(i))
        UCBs.append(UCB(i))
    print('T: ', T)
    print('mu_hs: ', mu_hs)
    print('UCBs: ', UCBs)
    plt.show()

def argmax():
    max_UCB = 0
    max_i = -1
    for i in range(k):
        temp = UCB(i)
        if temp == -1:
            return i
        if temp > max_UCB:
            max_UCB = temp
            max_i = i
    return max_i

def UCB(i): #delta=1/n**2
    if T[i] == 0: #here T[i] is T_i(t-1)
        return -1
    return mu_h(i) + math.sqrt(2*math.log(n**2)/T[i])
    
def mu_h(i): #mu_i(t-1)
    return total_reward[i]/T[i]

# environment
def get_reward(i):
    return np.random.default_rng().normal(mu(i), 1)

def mu(i):
    i += 1 #start from 1
    return (k-i)/(k-1)

if __name__ == "__main__":
    main()