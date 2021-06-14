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

r = np.zeros((S,A))
r[8][0] = 1
r[1][1] = 0.5
# gamma = 0.99
gamma = 0.99
mu = (0.1*np.ones((S,1)))
Q = np.zeros((S,A))
log_max_d = []
pi = np.ones((S,1)) #0 for west, 1 for east
ks = []

def main():
    records, pi = value_iteration()
    plt.xlabel('k')
    plt.ylabel('log diff')
    plt.plot(records)
    plt.show()
    print(Q)
    print(pi)

def policy_improvement(q):
    new_q = np.zeros((S, A))

    states = [s for s in range(0, S)]
    for s in range(S):
        for a in range(A):
            s_next = np.random.choice(states, p=P[s+a*S])
            new_q[s][a] = r[s][a] + gamma*np.max(q[s_next])
    # print(new_q)
    return new_q

def value_iteration():
    global Q
    records = []

    for k in range(1, K+1):
        new_q = policy_improvement(Q)
        max_diff = np.max(np.abs(new_q - Q))

        records.append([k, max_diff])
        Q = new_q
    
    return records, np.argmax(Q,axis=1)


if __name__ == "__main__":
    main()