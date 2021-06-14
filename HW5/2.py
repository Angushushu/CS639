import math
import numpy as np
import random
import matplotlib.pyplot as plt
from MDP import MDP

delta = 0.1 # here is capital delta

traj_s = []
traj_a = []
traj_r = []
tdelta = []
mdp = MDP(1, 0.2, 0.5, 0.1, 0.001)

def main():
    # s_0
    theta_0 = np.random.normal(0, 0.01)
    s = np.array([[theta_0], [0], [0], [0]])
    r = None
    t = 0
    while r!=0:
        a = pi(s)
        traj_s.append(s)
        traj_a.append(a)
        s,r = mdp.step(s, pi(s))
        traj_r.append(r)
        tdelta.append(t*delta)
        t += 1
    traj_s.append(s)
    tdelta.append(t*delta)

    # figures
    thetas = []
    xs = []
    print(t)
    print(len(traj_s))
    print(traj_s[t][0][0])
    for i in range(t+1):
        thetas.append(traj_s[i][0][0])
        xs.append(traj_s[i][2][0])
    plt.xlabel('i*delta')
    plt.ylabel('theta')
    plt.plot(tdelta, thetas, 'o', color='red', markersize=1)
    plt.show()
    plt.ylabel('x')
    plt.plot(tdelta, xs, 'o', color='blue', markersize=1)
    plt.show()

def pi(s):
    if s[0][0]>0:
        return 10
    elif s[0][0]<0:
        return -10
    else:
        return 0

if __name__ == "__main__":
    main()