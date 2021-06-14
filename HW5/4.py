import math
import numpy as np
import random
import matplotlib.pyplot as plt
from MDP import MDP

delta = 0.1 # capital delta
gamma = 0.99
a_s = [10,-10,0]

mdp = MDP(1, 0.2, 0.5, 0.1, 0.001)

# stepsize_w = 0.00001
stepsize_w = 0.01
stepsize_theta = 0.00001

w = np.zeros((3,1))
theta = np.zeros((3,1))

def main():
    global w
    global theta
    global stepsize_w
    global stepsize_theta
    gain_s = []
    e_s = []
    w_s_1 = []
    w_s_2 = []
    w_s_3 = []
    theta_s_1 = []
    theta_s_2 = []
    theta_s_3 = []

    for roll in range(2000):
        traj_s, traj_a, traj_r = get_rollout()

        w_s_1.append(w[0][0]) #
        w_s_2.append(w[1][0]) #
        w_s_3.append(w[2][0]) #
        theta_s_1.append(w[0][0]) #
        theta_s_2.append(w[1][0]) #
        theta_s_3.append(w[2][0]) #
        
        # partial derivative
        for h in range(len(traj_a)):
            # G vlue starts from h, for algorithm
            G = 0
            gain = 0
            for i in range(h,len(traj_r)):
                G += (gamma**(i-h))*traj_r[i]
            # gain for gain_s
            for i in range(len(traj_r)):
                gain += (gamma**(i))*traj_r[i]
            
            pi_w_s = pi(traj_s[h])
            sum = pi_w_s[0]*phi(traj_s[h],0) + pi_w_s[1]*phi(traj_s[h],1) + pi_w_s[2]*phi(traj_s[h],2)
            

            d = G-np.matmul(w.T,sum)
            w = w + stepsize_w*d*sum
            
            part = phi(traj_s[h], traj_a[h]) - sum
            theta = theta + stepsize_theta*d*part
            # pi_w_s = pi(traj_s[h])
            # w += stepsize*(G-np.matmul(w.T,phi(traj_s[h],-1)))*phi(traj_s[h],-1)
            # sum = pi_w_s[0]*phi(traj_s[h],0) + pi_w_s[1]*phi(traj_s[h],1) + pi_w_s[2]*phi(traj_s[h],2)
            # part = phi(traj_s[h], traj_a[h]) - sum
            # theta += stepsize*(G-np.matmul(w.T,phi(traj_s[h],-1)))*part
        
            # stepsize_w *= 0.9999
            # stepsize_w = 0.001/roll if roll>0 else stepsize_w
            # if roll%100 == 0:
            #     if random.randrange(0,1) == 1:
            #         stepsize_w = 0.00001
            #     else:
            #         stepsize_theta = 0.1/roll if roll>0 else stepsize_theta
        if roll!=0:
            stepsize_w = 0.01/roll

        gain_s.append(gain)
        e_s.append(roll+1)
    print('Q4 - avg_gain: ', np.mean(gain_s))

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
    
    plt.xlabel('episode number')
    plt.ylabel('(theta_1, theta_2, theta_3)^T')
    plt.plot(e_s, theta_s_1, 'o', color='yellow', markersize=1)
    plt.plot(e_s, theta_s_2, 'o', color='magenta', markersize=1)
    plt.plot(e_s, theta_s_3, 'o', color='cyan', markersize=1)
    plt.legend(["theta1", "theta2","theta3"])
    plt.show()
    
def get_rollout():
    # clear rollout
    traj_s = []
    traj_a = []
    traj_r = []
    t = 0
    # s_0
    theta_0 = np.random.normal(0, 0.1) #sd here
    # theta_0 = math.pi/180
    s = np.array([[theta_0], [0], [0], [0]])
    r = 1
    while r!=0:
        a = np.argmax(np.random.multinomial(1, pi(s))) # 0 for 10, 1 for -10, 2 for 0
        traj_s.append(s)
        traj_a.append(a)
        s,r = mdp.step(s, a_s[a])
        traj_r.append(r)
        if r!=0:
            t += 1
    traj_a.pop()
    traj_r.pop()
    t -= 1
    
    return traj_s, traj_a, traj_r

def pi(s):
    denominator = math.exp(np.matmul(theta.T,phi(s,0)))+math.exp(np.matmul(theta.T,phi(s,1)))+math.exp(np.matmul(theta.T,phi(s,2)))
    pi_as = []
    pi_as.append(math.exp(np.matmul(theta.T,phi(s,0)))/denominator) # 10
    pi_as.append(math.exp(np.matmul(theta.T,phi(s,1)))/denominator) # -10
    pi_as.append(math.exp(np.matmul(theta.T,phi(s,2)))/denominator) # 0
    return pi_as


def phi(s,a):
    force = a_s[a]
    phi = np.zeros((3,1))
    phi[0][0] = force if s[0][0]>(5*math.pi/180) else 0
    phi[1][0] = force if s[0][0]<(-5*math.pi/180) else 0
    phi[2][0] = force*s[1][0]
    return phi

if __name__ == "__main__":
    main()