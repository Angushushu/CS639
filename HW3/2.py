import math
import numpy as np
import matplotlib.pyplot as plt

S = 10
P_pi = np.zeros((S,S)) # (s',s) 0 for west, 1 for east
for i in range(S-1):
    P_pi[i][i+1] = 1
# P_pi[9][9] = 1 # go east
P_pi[9][9] = 0 # better pi
P_pi[9][8] = 1 # better pi
r_pi = np.zeros((S,1))
r_pi[8] = 1
gamma = 0.99

def main():
    print("P_pi\n",P_pi)
    I = np.mat(np.eye(S,S))
    C = (I-gamma*P_pi).I #indicates the possibility of reaching s' in the future?
    print("C\n",C) #1a
    print("r_pi\n", r_pi)
    V_pi = np.matmul(C,r_pi)
    print("V_pi\n",V_pi) #2a how to explain?
    mu = (0.1*np.ones((S,1)))
    v_pi = np.matmul(mu.T, V_pi)
    print("v_pi\n",v_pi.item()) #2b

if __name__ == "__main__":
    main()