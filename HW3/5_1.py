import math
import numpy as np
import matplotlib.pyplot as plt

S = 10
A = 2
K = 1001
P = np.zeros((S*A,S)) #P of environment
for i in range(S-1):
    P[i][i+1] = 1 #e
    P[10+S-i-1][S-i-2] = 1 #w
P[9][9] = 1 #e
P[10+0][0] = 1 #w

r = np.zeros((S*A,1))
r[8][0] = 1
r[10+1][0] = 0.5
# gamma = 0.99
gamma = 0.99
mu = (0.1*np.ones((S,1)))
Q = np.zeros((S*A,1))
log_max_d = []
pi = np.ones((S,1)) #0 for west, 1 for east
ks = []

def main():
    acc_max_d = 0
    for k in range(K):
        log_max_d.append(math.log(trial()))
        ks.append(k+1)
    print(Q)
    print(pi)
    plt.xlabel('k')
    plt.ylabel('log||f_k-f_{k-1}||oo')
    plt.plot(ks, log_max_d)
    plt.show()

def trial():
    global Q
    new_q = np.zeros((S*A,1)) # this get me the correct answer
    max_d = -100
    # update f
    for i in range(S*A):
        tempt = r[i][0]+gamma*get_E(i) #temp = f_k+1
        if abs(Q[i][0]-tempt) > max_d:
            max_d = abs(Q[i][0]-tempt)
        new_q[i][0] = tempt
    # update pi
    for i in range(S):
        pi[i] = 0 if new_q[i][0].item()<new_q[10+i][0].item() else 1
    Q = new_q
    return max_d

def get_E(i):
    E = 0
    states = [s for s in range(0, S)]
    j = np.random.choice(states, p=P[i])
    # for j in range(S): #j=s'
    max_Q = Q[j][0] if Q[j][0]>Q[S+j][0] else Q[S+j][0] # max f(s',a')
    E += P[i][j]*max_Q
    return E

if __name__ == "__main__":
    main()