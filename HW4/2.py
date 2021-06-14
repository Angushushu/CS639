import math
import numpy as np
import random
import matplotlib.pyplot as plt
from MDP import MDP

n = 3
env = MDP(n, 0.1) # n,p
gamma = 0.99
S = env.n_states
P_pi = np.zeros((S,S))
#
P_pi[0][0] = 0.9
P_pi[3][3] = 0.9
P_pi[6][6] = 0.9
# 2, 3 clockwise
P_pi[1][2] = 0.9
P_pi[2][3] = 0.9
# 5, 6 in
P_pi[4][1] = 0.9
P_pi[5][2] = 0.9
for i in range(7):
    P_pi[i][1] += 0.1

r_pi = np.zeros((S,1))
r_pi[0][0] = -1
r_pi[n][0] = 2
r_pi[2*n][0] = 1

I = np.mat(np.eye(S,S))
C = (I-gamma*P_pi).I
V_pi = np.matmul(C,r_pi)
v_pi = V_pi[1][0]

print(V_pi)
print(v_pi.item())
