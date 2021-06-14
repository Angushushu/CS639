import math
import numpy as np
import random
import matplotlib.pyplot as plt
from MDP import MDP

delta = 0.1 # capital delta
gamma = 0.99

traj_s = []
traj_a = []
traj_r = []
tdelta = []
mdp = MDP(1, 0.2, 0.5, 0.1, 0.001) #m_c, m_p, l, tri, delta

def main():
    # s_0
    s = np.array([[math.pi/180], [0], [0], [0]])
    r = None
    t = 0
    while r!=0:
        a = pi(s)
        if t<20:
            print('--------',t,'--------')
            print('s:\n', s)
            print('a:', a)
            
        traj_s.append(s)
        traj_a.append(a)
        s,r = mdp.step(s, a)
        if t<20:
            print('r:', r)
        traj_r.append(r)
        tdelta.append(t*delta) # 把最后一位删掉
        if r!=0:
            t += 1 # in the end, t is t+1
    traj_a.pop()
    traj_r.pop()
    # tdelta.pop()
    t -= 1 

    # figures
    thetas = []

    xs = []
    print(t)
    print(len(traj_s))
    for i in range(t+2):
        thetas.append(traj_s[i][0][0])
        xs.append(traj_s[i][2][0])
    plt.xlabel('i*delta')
    plt.ylabel('theta')
    plt.plot(tdelta, thetas, 'o', color='red', markersize=1)
    plt.show()
    plt.ylabel('x')
    plt.plot(tdelta, xs, 'o', color='blue', markersize=1)
    plt.show()

    # gain vlue
    gain = 0
    for i in range(len(traj_r)):
        gain += (gamma**i)*traj_r[i]
    print(gain)
    # print(thetas)
    # print()
    # print(xs)
    # print(traj_a)
    

def pi(s):
    if s[0][0]>0:
        return 10
    elif s[0][0]<0:
        return -10
    else:
        return 0

if __name__ == "__main__":
    main()