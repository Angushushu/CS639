import math
import numpy as np
import matplotlib.pyplot as plt

k = 11
n = 10000 # what's n?
total_reward = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] #for i arms, used by mu_h
T = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] #for i arms, used by mu_h

dr_Rs = []
random_Rs = []
pseudo_Rs = []
s_ts = [0]*n
ts = [0]*n

def main():
    global total_reward
    global T
    for j in range(100):
        print('trial ', j)
        trial()
        total_reward = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] #reset
        T = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    plt.xlabel('dr_R')
    plt.ylabel('frequency')
    plt.hist(dr_Rs, bins = 10)
    plt.show()
    plt.close()
    plt.xlabel('random_R')
    plt.ylabel('frequency')
    plt.hist(random_Rs, bins = 10)
    plt.show()
    plt.close()
    plt.xlabel('pseudo_R')
    plt.ylabel('frequency')
    plt.hist(pseudo_Rs, bins = 10)
    plt.show()
    plt.close()
    plt.xlabel('t')
    plt.ylabel('Average s_t')
    for t in range(n):
        ts[t] = t+1
    plt.plot(ts, s_ts)
    plt.show()
    print('mean dr_R: ', np.mean(dr_Rs))
    print('std dr_R: ', np.std(dr_Rs))
    print('mean random_R: ', np.mean(random_Rs))
    print('std random_R: ', np.std(random_Rs))
    print('mean pseudo_R: ', np.mean(pseudo_Rs))
    print('std pseudo_R: ', np.std(pseudo_Rs))

def trial():
    dr_R = 0
    random_R = 0
    pseudo_R = 0
    s_t = 0
    for t in range(n):
        A_t = argmax() # choose i for this t, notice it starts from 0
        X_t = get_reward(A_t)
        total_reward[A_t] += X_t #get rewards and update mu_h
        T[A_t] += 1

        #Q3
        s_t += X_t
        s_ts[t] += s_t/100 # for avg
        if A_t!=0:
            dr_R += get_reward(0) - X_t #X_t' - X_t
        random_R += mu(0) - X_t
        pseudo_R += mu(0) - mu(A_t)
    dr_Rs.append(dr_R)
    random_Rs.append(random_R)
    pseudo_Rs.append(pseudo_R)
    print(dr_R) 

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