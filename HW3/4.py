import math
import numpy as np
import matplotlib.pyplot as plt

S = 10
A = 2
P = np.zeros((S*A,S*A)) #P of environment
for i in range(S-1):
    P[i][i+1] = 1 #e
    P[i][10+i+1] = 1 #e
    P[10+S-i-1][S-i-2] = 1 #w
    P[10+S-i-1][10+S-i-2] = 1 #w
P[9][9] = 1 #e
P[9][10+9] = 1 #e
P[10+0][0] = 1 #w
P[10+0][10+0] = 1 #w

r_pi = np.zeros((S*A,1))
r_pi[8][0] = 1
r_pi[10+1][0] = 0.5
gamma = 0.99
pi = np.ones((S,1)) #0 for west, 1 for east
mu = (0.1*np.ones((S,1)))

def main():
    print('P\n',P)
    print('P[0][1]\n',P[0][1])
    for k in range(4):
        print('---------------------------------------------trial',k)
        trial()

def trial():
    P_pi = np.zeros((S*A,S*A))
    # P_pi = P*pi
    for r in range(S):
        for c in range(S):
            if pi[c] == 1: #r?
                P_pi[r][c] = P[r][c]
                P_pi[10+r][c] = P[10+r][c]
            else:
                P_pi[r][10+c] = P[r][10+c]
                P_pi[10+r][10+c] = P[10+r][10+c]
    print('P_pi\n',P_pi)

    I = np.mat(np.eye(S*A,S*A))
    C = (I-gamma*P_pi).I
    temp = np.matmul(C,r_pi)
    Q = np.asarray(np.hstack((temp[10:S*A][:], temp[0:10][:]))) # 0 for west, 1 for east

    #v_pi
    V_pi = np.zeros((S,1))
    for i in range(S):
        V_pi[i] = Q[i][0] if pi[i] == 0 else Q[i][1]
    v_pi = np.matmul(mu.T, V_pi)

    print('pi\n',pi)
    print('Q\n',Q)
    print('v_pi:',v_pi.item())

    #argmax
    for i in range(S):
        pi[i] = 1 if Q[i][1] > Q[i][0] else 0


if __name__ == "__main__":
    main()