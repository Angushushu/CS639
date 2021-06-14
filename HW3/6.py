import math
import numpy as np
import matplotlib.pyplot as plt

S = 10
A = 2
K = 1000
P = np.zeros((S*A,S)) #P of environment
for i in range(S-1):
    P[i][i+1] = 1 #e
    P[10+S-i-1][S-i-2] = 1 #w
P[9][9] = 1 #e
P[10+0][0] = 1 #w

r = np.zeros((S*A,1))
r[8][0] = 1
r[10+1][0] = 0.5
gamma = 0.01
mu = (0.1*np.ones((S,1)))
f = np.zeros((S*A,1))
pi = np.ones((S,1)) #0 for west, 1 for east

def main():
    for k in range(K):
        trial()
    print(pi)

def trial():
    max_d = 0
    # update f
    for i in range(S*A):
        tempt = r[i][0]+gamma*get_E(i)
        if abs(f[i][0]-tempt) > max_d:
            max_d = abs(f[i][0]-tempt)
        f[i][0] = tempt
    # update pi
    for i in range(S):
        pi[i] = 0 if f[i][0].item()<f[10+i][0].item() else 1

    return max_d

def get_E(i):
    for j in range(S):
        if P[i][j]==1:
            return f[j][0] if f[j][0]>=f[10+j][0] else f[10+j][0] # max f(s',a')

if __name__ == "__main__":
    main()