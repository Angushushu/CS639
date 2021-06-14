import math
import numpy as np
import matplotlib.pyplot as plt

S = 10
A = 2
H = 10 #?
K = 1000
P = np.zeros((S*A,S)) #P of environment
for i in range(S-1):
    P[i][i+1] = 1 #e
    P[10+S-i-1][S-i-2] = 1 #w
P[9][9] = 1 #e
P[10+0][0] = 1 #w
Q = np.zeros((S*A,H)) # V_hs
r = np.zeros((S*A,1))
r[8][0] = 1
r[10+1][0] = 0.5
pi = [['.' for x in range(S)] for y in range(H)] #< for west, > for east

def main():
    for k in range(K):
        trial()
    for h in range(H):
        print('h =',h,''.join(pi[h]))


def trial():
    for h in range(H):
        # obtain Q(s', pi(s'))'s
        Q_h = np.zeros((S,1))
        if h != 0:
            for i in range(S):
                Q_h[i][0] = Q[i][H-h] if pi[H-h][i] == '>' else Q[10+i][H-h]      
        temp = np.matmul(np.asmatrix(P), Q_h)
        for sa in range(S*A):
            Q[sa][H-1-h] = r[sa] + temp[sa] # r+EmaxQ_h+1(s',a')
        # update pi
        for s in range(S):
            if Q[s][H-1-h] > Q[10+s][H-1-h]:
                pi[H-1-h][s] = '>'
            elif Q[s][H-1-h] < Q[10+s][H-1-h]:
                pi[H-1-h][s] = '<'
            else:
                pi[H-1-h][s] = '.'

if __name__ == "__main__":
    main()