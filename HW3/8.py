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

P[0][0] = 1
P[0][1] = 0
P[10][0] = 1

P[9][9] = 1 #e
P[10+9][9] = 1
P[10+9][8] = 0

r = np.zeros((S*A,1))
r[8][0] = 1
r[10+1][0] = 0.5
Q = np.zeros((S*A,1))
pi = np.ones((S,1)) #0 for west, 1 for east

def main():
    for k in range(K):
        trial()
    print(pi)
    print(Q)
    print(np.hstack((Q[10:S*A][:], Q[0:10][:])))

def trial():
    # update f
    for i in range(S*A):
        tempt = r[i][0]+get_E(i)
        Q[i][0] = tempt
    # update pi
    for i in range(S):
        pi[i] = 0 if Q[i][0].item()<Q[10+i][0].item() else 1

def get_E(i):
    for j in range(S):
        if P[i][j]==1:
            return Q[j][0] if Q[j][0]>=Q[10+j][0] else Q[10+j][0] # E P*maxQ(s',a')

if __name__ == "__main__":
    main()