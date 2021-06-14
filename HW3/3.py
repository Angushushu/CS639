import math
import numpy as np
import matplotlib.pyplot as plt

S = 10
A = 2
P_pi = np.zeros((S*A,S*A))
for i in range(S-1):
    P_pi[i][i+1] = 1
    P_pi[10+S-i-1][S-i-2] = 1
P_pi[9][9] = 1
P_pi[10+0][0] = 1
r_pi = np.zeros((S*A,1)) # 0 west, 1 east
r_pi[10+1][0] = 0.5
r_pi[8][0] = 1
gamma = 0.99

def main():
    I = np.mat(np.eye(S*A,S*A))
    C = (I-gamma*P_pi).I
    C_ee = C[0:10,0:10]
    C_ew = C[0:10,10:S*A]
    C_we = C[10:S*A,0:10]
    C_ww = C[10:S*A,10:S*A]
    temp = np.matmul(C,r_pi)
    Q = np.hstack((temp[10:S*A][:],temp[0:10][:]))

    print('P_pi\n', P_pi.round(2))
    print('C\n', C.round(2))
    print(C[0:10,0:10].round(2))

    print('C_ww \n', C_ww.round(2))
    print('C_we \n', C_we.round(2))
    print('C_ee \n', C_ee.round(2))
    print('C_ew \n', C_ew.round(2))
    
    print('Q \n', Q)


if __name__ == "__main__":
    main()