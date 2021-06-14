import matplotlib.pyplot as plt
import numpy as np
import random

theta = 0.639
avg_risks = []
t_s = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
i_s = 10
runs = 100

def main():
    print(theta)
    for i in range(i_s):
        total_risk = 0
        for t in range(runs):
            total_risk += train(i)
        avg_risks.append(total_risk/runs)
        # print(n+1, ' : ', avg_risks[n])
    i_list = ['1','2','3','4','5','6','7','8','9','10']
    plt.bar(i_list, avg_risks)
    plt.xlabel('i')
    plt.ylabel('r_i')
    plt.show()
    plt.close()
    plt.plot(i_list, t_s, '-o')
    plt.xlabel('i')
    plt.ylabel('t_i')
    plt.show()

def train(i):
    x_l = -2
    x_r = 2
    q = 0 #count queries
    t = 0 #cout times
    while q < i+1:
        x_t = random.uniform(-1,1)
        if x_t > x_l and  x_t < x_r:
            y_t = get_y(x_t)
            if y_t == -1:
                x_l = x_t
            else:
                x_r = x_t
            q += 1
        t += 1
    t_s[i] += t
    theta_h = (x_l+x_r)/2
    risk = abs(theta_h-theta)/2
    return risk
    
def get_y(x):
    return -1 if x<theta else 1

if __name__ == "__main__":
    main()