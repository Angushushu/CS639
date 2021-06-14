import math
import numpy as np
import random
import matplotlib.pyplot as plt
from MDP import MDP

n = 3
S = 2*n+1
A = 3
T = 10000
alpha = 0.5
epsilon = 0.1
gamma = 0.99
Q_h = np.zeros((S, A))
mdp = MDP(n, 0.1)

def main():
    plt.xlabel('t')
    plt.ylabel('max_aQ^h_t(2,a)')
    # s initialized automatically
    s = mdp.reset()
    a = None
    a_ = None
    plt.plot(0, np.max(Q_h[1]), 'o', color='black', markersize=1)
    if np.random.multinomial(1, [epsilon, 1-epsilon])[0]==1:
        a = np.argmax(np.random.multinomial(1, [1/3]*3))
    else:
        a = np.argmax(Q_h[s])
    for t in range(T):
        ret = mdp.do(s,a)
        if np.random.multinomial(1, [epsilon, 1-epsilon])[0]==1:
            a_ = np.argmax(np.random.multinomial(1, [1/3]*3))
        else:
            a_ = np.argmax(Q_h[ret[1]])
        Q_h[s][a] = Q_h[s][a] + alpha*(ret[0] + gamma*Q_h[ret[1]][a_] - Q_h[s][a])
        s = ret[1]
        a = a_
        plt.plot(t+1, np.max(Q_h[1]), 'o', color='black', markersize=1)
    
    pi = np.zeros((S,1))
    V_h = np.zeros((S,1))
    for i in range(S):
        V_h[i][0] = max(Q_h[i])
        pi[i][0] = np.argmax(Q_h[i])
    print('Q_h\n',Q_h)
    print('V_h\n',V_h)
    print('pi\n',pi)

    plt.show()

if __name__ == '__main__':
    main()

    