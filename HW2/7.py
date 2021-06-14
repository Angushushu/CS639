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
T = [0]*k
i_s = [-1]*n
theta_h_0s = [-1]*n
theta_0s = [-1/(k-1)]*n
theta_h_1s = [-1]*n
theta_1s = [k/(k-1)]*n
total_R = 0

UCB_total_reward = [0]*k #for i arms, used by mu_h
T = [0]*k #for i arms, used by mu_h

def main():
    global V
    global total_R
    global theta_h #?
    sum_XA = np.mat([[0.0],[0.0]])
    for t in range(n):
        A_t = a(4) if t==0 else a(argmax())
        X_t = get_reward(A_t)
        V = V + A_t*(A_t.T)
        sum_XA += X_t*A_t
        theta_h = V.I*sum_XA
        total_R += X_t

        if t==0:
            print('t=1')
            print('A_t:', A_t)
            print('X_t:', X_t)
            print('V_t:', V)
            print('sum_XA:', sum_XA)
            print('theta_h:', theta_h)

        #Q7
        # if t%100==0:
        #     print(A_t)
        i = A_t[0][0].item()
        T[i-1] += 1
        i_s[t] = i
        theta_h_0s[t] = theta_h[0][0].item()
        theta_h_1s[t] = theta_h[1][0].item()
    
    t_s = [0]*n
    for i in range(n):
        t_s[i] = i+1
    for i in range(k):
        if T[i] != 0:
            print(i+1, ': ', T[i])
    plt.xlabel('t')
    plt.ylabel('arm')
    plt.plot(t_s, i_s, 'o', markersize=.5, color='black')
    plt.show()
    plt.ylabel('theta_h[0][0]')
    plt.plot(t_s, theta_0s, 'o', markersize=.3, color='yellow')
    plt.plot(t_s, theta_h_0s, 'o', markersize=.5, color='black')
    plt.show()
    plt.ylabel('theta_h[1][0]')
    plt.plot(t_s, theta_1s, 'o', markersize=.3, color='yellow')
    plt.plot(t_s, theta_h_1s, 'o', markersize=.5, color='black')
    plt.show()
    print('total_reward:', total_R)

def argmax():
    max_val = float('-inf')
    max_i = float('-inf')
    for i in range(k):
        temp = calc_for_max(i)
        if temp > max_val:
            max_val = temp
            max_i = i
    return max_i

def calc_for_max(i):
    global theta_h #?
    sqrt_beta = m_2*math.sqrt(lmbda)+math.sqrt(2*math.log(n)+math.log(np.linalg.det(V)/(lmbda**d)))
    return (a(i).T*theta_h).item() + sqrt_beta*math.sqrt((a(i).T*(V.I)*a(i)).item())

def a(i):
    return np.mat([[i+1, 1]]).T

def get_reward(B_t):
    R_metrix = B_t.T*theta + np.random.default_rng().normal(0, 1)
    return R_metrix.item()

if __name__ == "__main__":
    main()
