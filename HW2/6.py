import math
import numpy as np
import matplotlib.pyplot as plt

d = 2
k = n = 1000
m_2 = (k+1)/(k-1)
I_d = np.mat(np.eye(d,d))
lmbda = 1
theta_h = np.mat([[0.0], [0.0]]) #what's the initial value?
theta = np.mat([[-1/(k-1), k/(k-1)]]).T
V = lmbda*I_d # for V.I

UCBs = [0, 0, 0, 0, 0] # for print

def main():
    global V
    sum_XA = np.mat([[0.0],[0.0]])
    for t in range(n):
        A_t = a(4) if t==0 else a(argmax())
        X_t = get_reward(A_t)
        V = V + A_t*(A_t.T)
        sum_XA += X_t*A_t
        theta_h = V.I*sum_XA
        if t<4 or t==999:
            print('Iteration', t+1, ': -----------------------------------------------')
            if t != 0:
                print('UCB 1, 2, 5, 999, 1000 =', UCBs[0], UCBs[1], UCBs[2], UCBs[3], UCBs[4])
                print('A', t+1, ' = ', A_t)
            print('X', t+1, ' = ', X_t)
            print('V', t+1, ' = ', V)
            print('hat_theta_', t+1, ' = ', theta_h)

def argmax():
    max_val = float('-inf')
    max_i = float('-inf')
    for i in range(k):
        temp = calc_for_max(i)
        if temp > max_val:
            max_val = temp
            max_i = i
        if i == 0:
            UCBs[0] = temp
        elif i == 1:
            UCBs[1] = temp
        elif i == 499:
            UCBs[2] = temp
        elif i == 998:
            UCBs[3] = temp
        elif i == 999:
            UCBs[4] = temp
    return max_i

def calc_for_max(i):
    sqrt_beta = m_2*math.sqrt(lmbda)+math.sqrt(2*math.log(n)+math.log(np.linalg.det(V)/(lmbda**d)))
    return a(i).T*theta_h + sqrt_beta*math.sqrt(a(i).T*(V.I)*a(i))

def a(i):
    return np.mat([[i+1, 1]]).T

def get_reward(B_t):
    R_metrix = B_t.T*theta + np.random.default_rng().normal(0, 1)
    return R_metrix.item()

if __name__ == "__main__":
    main()
