import math
import numpy as np
import random
import matplotlib.pyplot as plt
from MDP import MDP

delta = 0.1 # capital delta
gamma = 0.99
a_s = [10,-10,0]

mdp = MDP(1, 0.2, 0.5, 0.1, 0.001)

stepsize_w = 0.00001
stepsize_theta = 0.00001
w = np.zeros((3,1))
theta = np.zeros((3,1))

def main():
    global w
    global theta
    gain_s = []
    e_s = []
    w_s_1 = []
    w_s_2 = []
    w_s_3 = []

    for episode in range(8000):
        traj_s, traj_a, G = get_rollout_gain()
        '''
        for h in range(len(traj_a)):
            # update w
            pi_w_s_ = pi(traj_s[h])
            phi_s = pi_w_s_[0]*phi(traj_s[h],0) + pi_w_s_[1]*phi(traj_s[h],1) + pi_w_s_[2]*phi(traj_s[h],2)
            # phi_s = phi(traj_s[h],np.argmax(pi_w_s_))
            # phi_s = phi(traj_s[h],0) + phi(traj_s[h],1) + phi(traj_s[h],2)
            print(phi_s)
            w = w + stepsize_w*(G-np.matmul(w.T,phi_s))*phi_s
            # update theta
            pi_w_s = pi(traj_s[h])
            sum = pi_w_s[0]*phi(traj_s[h],0) + pi_w_s[1]*phi(traj_s[h],1) + pi_w_s[2]*phi(traj_s[h],2)
            part = phi(traj_s[h], traj_a[h]) - sum
            theta = theta + stepsize_theta*(G-np.matmul(w.T,phi_s))*part
        '''
        sum_part = 0 # for theta
        sum_phi = 0 # for w
        for h in range(len(traj_a)):
            pi_w_s = pi(traj_s[h])
            sum = pi_w_s[0]*phi(traj_s[h],0) + pi_w_s[1]*phi(traj_s[h],1) + pi_w_s[2]*phi(traj_s[h],2)
            sum_part += phi(traj_s[h], traj_a[h]) - sum
            sum_phi += phi(traj_s[h], traj_a[h])
        w_s_1.append(w[0][0]) #
        w_s_2.append(w[1][0]) #
        w_s_3.append(w[2][0]) #
        
        phi_s = sum_phi/len(traj_a)
        w = w + stepsize_w*(G-np.matmul(w.T,phi_s))*phi_s
        theta = theta + stepsize_theta*(G-np.matmul(w.T,phi_s))*sum_part

        gain_s.append(G)
        e_s.append(episode+1)

    # figures
    plt.xlabel('episode number')
    plt.ylabel('gain')
    plt.plot(e_s, gain_s, 'o', color='green', markersize=1)
    plt.show()
    plt.ylabel('w_1')
    plt.plot(e_s, w_s_1, 'o', color='red', markersize=1)
    plt.show()
    plt.ylabel('w_2')
    plt.plot(e_s, w_s_2, 'o', color='red', markersize=1)
    plt.show()
    plt.ylabel('w_3')
    plt.plot(e_s, w_s_3, 'o', color='red', markersize=1)
    plt.show()
    
def get_rollout_gain():
    # clear rollout
    traj_s = []
    traj_a = []
    traj_r = []
    t = 0
    # s_0
    theta_0 = np.random.normal(0, 0.01)
    s = np.array([[theta_0], [0], [0], [0]])
    r = None
    while r!=0:
        a = np.argmax(np.random.multinomial(1, pi(s))) # 0 for 10, 1 for -10, 2 for 0
        traj_s.append(s)
        traj_a.append(a)
        s,r = mdp.step(s, a_s[a]) # s', r
        traj_r.append(r)
        t += 1
    traj_s.append(s)
    # gain vlue
    gain = 0
    for i in range(t):
        gain += (gamma**i)*traj_r[i]
    
    return traj_s, traj_a, gain

def pi(s):
    denominator = math.exp(np.matmul(theta.T,phi(s,0)))+math.exp(np.matmul(theta.T,phi(s,1)))+math.exp(np.matmul(theta.T,phi(s,2)))
    pi_as = []
    pi_as.append(math.exp(np.matmul(theta.T,phi(s,0)))/denominator) # 10
    pi_as.append(math.exp(np.matmul(theta.T,phi(s,1)))/denominator) # -10
    pi_as.append(math.exp(np.matmul(theta.T,phi(s,2)))/denominator) # 0
    return pi_as


def phi(s,a):
    phi = np.zeros((3,1))
    phi[0][0] = a_s[a] if s[0][0]>(5*math.pi/180) else 0
    phi[1][0] = a_s[a] if s[0][0]<(-5*math.pi/180) else 0
    phi[2][0] = a_s[a]*s[2][0]
    return phi

if __name__ == "__main__":
    main()