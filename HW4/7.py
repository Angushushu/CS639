import math
import numpy as np
import random
import matplotlib.pyplot as plt
from MDP import MDP

n = 3
S = 2*n+1
A = 3
T = 10000
mdp = MDP(n, 0.1) # n,p
count = np.zeros((S,A))
count_ = np.zeros((S*A,S))
r_h = np.zeros((S,A))

s = mdp.reset()
for t in range(T):
    a = np.argmax(np.random.multinomial(1,[1/3]*3))
    ret = mdp.do(s,a)
    count[s][a] += 1
    count_[s+a*S][ret[1]] += 1
    r_h[s][a] += ret[0]
    s = ret[1]

for i in range(S):
    for j in range(A):
        print('count(s=%2d, a=%2d)=%2d, hatP(.|s,a): ' % (i+1, j+1, count[i][j]), end='')
        for k in range(S):
            print(round(count_[i+j*S][k]/count[i][j],3), end='  ')
        print('r =',round(r_h[i][j]/count[i][j],3))
    
