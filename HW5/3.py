import math
import numpy as np
import random
import matplotlib.pyplot as plt
from MDP import MDP

delta = 0.1 # capital delta
gamma = 0.99
# alpha = math.pi/180 # 13.99
alpha = math.pi/80 # 13.99
a_s = [10,-10,0]

mdp = MDP(1, 0.2, 0.5, 0.1, 0.001)

stepsize = 0.00001
w = np.zeros((3,1))

def main():
    gain_s = []
    e_s = []
    w_s_1 = []
    w_s_2 = []
    w_s_3 = []

    for episode in range(2000):
    # for episode in range(1):
        global w
        # print('w:',w)
        traj_s, traj_a, G = get_rollout_gain()
        # partial derivative
        sum_part = 0
        # print('-----------------update w--------------')
        for h in range(len(traj_a)):
            # print('h =', h)
            pi_w_s = pi(traj_s[h])
            sum = pi_w_s[0]*phi(traj_s[h],0) + pi_w_s[1]*phi(traj_s[h],1) + pi_w_s[2]*phi(traj_s[h],2)
            # print('sum =', sum)
            # print('phi =', phi(traj_s[h], traj_a[h]))
            sum_part += phi(traj_s[h], traj_a[h]) - sum
            # print('sum_part =', sum_part)
        w_s_1.append(w[0][0]) #
        w_s_2.append(w[1][0]) #
        w_s_3.append(w[2][0]) #
        w = w + stepsize*G*sum_part
        # print('w:',w)
        gain_s.append(G)
        e_s.append(episode+1)

        # print('w:', w)

    print('Q3 - avg_gain: ', np.mean(gain_s))

    # figures
    plt.xlabel('episode number')
    plt.ylabel('gain')
    plt.plot(e_s, gain_s, 'o', color='green', markersize=1)
    plt.show()
    plt.xlabel('episode number')
    plt.ylabel('(w_1, w_2, w_3)^T')
    plt.plot(e_s, w_s_1, 'o', color='yellow', markersize=1)
    plt.plot(e_s, w_s_2, 'o', color='magenta', markersize=1)
    plt.plot(e_s, w_s_3, 'o', color='cyan', markersize=1)
    plt.legend(["w1", "w2","w3"])
    plt.show()

    
    
def get_rollout_gain():
    # clear rollout
    traj_s = []
    traj_a = []
    traj_r = []
    t = 0
    # s_0
    theta_0 = np.random.normal(0, 0.1) #sd here
    # theta_0 = 0.003
    s = np.array([[theta_0], [0], [0], [0]])
    r = None
    while r!=0:
        a = np.argmax(np.random.multinomial(1, pi(s))) # 0 for 10, 1 for -10, 2 for 0
        # a = np.argmax(pi(s)) # 0 for 10, 1 for -10, 2 for 0 # test
        # if t<20:
        #     print('--------',t,'--------')
        #     print('s:\n', s)
        #     print('a:', a_s[a])
        traj_s.append(s)
        traj_a.append(a)
        s,r = mdp.step(s, a_s[a]) # s', r
        # if t<20:
        #     print('r:', r)
        #     print('pi_s:',pi(s))
        traj_r.append(r)
        if r!=0:
            t += 1 # in the end, t is t+1
    traj_a.pop()
    traj_r.pop()
    t -= 1
    # print('t:', t)
    # gain vlue
    gain = 0
    for i in range(len(traj_r)):
        gain += (gamma**i)*traj_r[i]
    
    return traj_s, traj_a, gain

def pi(s):
    denominator = math.exp(np.matmul(w.T,phi(s,0)))+math.exp(np.matmul(w.T,phi(s,1)))+math.exp(np.matmul(w.T,phi(s,2)))
    pi_as = []
    pi_as.append(math.exp(np.matmul(w.T,phi(s,0)))/denominator) # 10
    pi_as.append(math.exp(np.matmul(w.T,phi(s,1)))/denominator) # -10
    pi_as.append(math.exp(np.matmul(w.T,phi(s,2)))/denominator) # 0
    return pi_as


def phi(s,a):
    phi = np.zeros((3,1))
    phi[0][0] = a_s[a] if s[0][0]>(5*math.pi/180) else 0
    phi[1][0] = a_s[a] if s[0][0]<(-5*math.pi/180) else 0
    phi[2][0] = a_s[a]*s[1][0]
    return phi

if __name__ == "__main__":
    main()