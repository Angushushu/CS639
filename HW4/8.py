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
r_h = np.zeros((S*A,1))
P_h = np.zeros((S*A,S*A))
pi = np.zeros((S,1)) #0:in/1:out/2:clockwise

gamma = 0.99

def main():
    init()
    for t in range(1000):
        trial()
    
    print(pi)

def trial():
    P_pi = np.zeros((S*A,S*A))
    # P_pi = P*pi
    for r in range(S):
        for c in range(S):
            if pi[c] == 0: #r?
                P_pi[r][c] = P_h[r][c]
                P_pi[S+r][c] = P_h[S+r][c]
                P_pi[2*S+r][c] = P_h[2*S+r][c]
            elif pi[c] == 1:
                P_pi[r][S+c] = P_h[r][S+c]
                P_pi[S+r][S+c] = P_h[S+r][S+c]
                P_pi[2*S+r][S+c] = P_h[2*S+r][S+c]
            else:
                P_pi[r][2*S+c] = P_h[r][2*S+c]
                P_pi[S+r][2*S+c] = P_h[S+r][2*S+c]
                P_pi[2*S+r][2*S+c] = P_h[2*S+r][2*S+c]

    I = np.mat(np.eye(S*A,S*A))
    C = (I-gamma*P_pi).I
    temp = np.matmul(C,r_h)
    Q = np.hstack((temp[0:S][:],temp[S:2*S],temp[2*S:3*S]))
    # update pi
    for i in range(S):
        pi[i] = np.argmax(Q[i])

def init():
    s = mdp.reset()
    for t in range(T):
        a = np.argmax(np.random.multinomial(1,[1/3]*3))
        ret = mdp.do(s,a)
        count[s][a] += 1
        count_[s+a*S][ret[1]] += 1
        r_h[s+a*S] += ret[0]
        s = ret[1]

    for i in range(S):
        for j in range(A):
            for k in range(S):
                P_h[i+j*S][k] = count_[i+j*S][k]/count[i][j]
                P_h[i+j*S][S+k] = P_h[i+j*S][k]
                P_h[i+j*S][2*S+k] = P_h[i+j*S][k]
            r_h[i+j*S] = r_h[i+j*S]/count[i][j]

if __name__ == "__main__":
    main()
