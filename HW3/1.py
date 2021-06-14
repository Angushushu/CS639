import math
import numpy as np
import matplotlib.pyplot as plt

S = 10
P_pi = np.zeros((S,S)) # (s,s') 0 for west, 1 for east
for i in range(S-1):
    P_pi[i][i+1] = 1
P_pi[9][9] = 1
gamma = .99

def main():
    print(P_pi)
    I = np.mat(np.eye(S,S))
    C = (I-gamma*P_pi).I.round(2) #indicates the possibility of reaching s' in the future?
    print(C)

if __name__ == "__main__":
    main()