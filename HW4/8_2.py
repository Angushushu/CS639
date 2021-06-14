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
P_h = np.zeros((S*A,S))
pi = np.zeros((S,1)) #0:in/1:out/2:clockwise
f = np.zeros((S*A,1))

gamma = 0.99

def main():
    init()
    for t in range(1000):
        trial()
    print(pi)

def trial():
    # update f
    for i in range(S*A):
        tempt = r_h[i][0]+gamma*get_E(i)
        f[i][0] = tempt
    # update pi
    for i in range(S):
        pi[i] = np.argmax([f[i],f[S+i],f[2*S+i]])

def get_E(i):
    sum = 0
    for j in range(S): #j is s'
        sum+=P_h[i][j]*max([f[j], f[S+j], f[2*S+j]]) # f should from 
    return sum

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
            r_h[i+j*S] = r_h[i+j*S]/count[i][j]

if __name__ == "__main__":
    main()
