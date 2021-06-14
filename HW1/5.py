import matplotlib.pyplot as plt
import numpy as np
import random

theta = 0.639
# theta_h_data = []
# gen_risk_data = []
avg_risks = []
j = 100
ns = 10

def main():
    print(theta)
    for n in range(ns):
        total_risk = 0
        for i in range(j):
            total_risk += train(n+1)
        avg_risks.append(total_risk/j)
        print(n+1, ' : ', avg_risks[n])
    n_list = ['1','2','3','4','5','6','7','8','9','10']
    plt.bar(n_list, avg_risks)
    # plt.title('title name')
    plt.xlabel('n')
    plt.ylabel('Average Risk')
    plt.show()
    

def train(n):
    max_l = -1
    min_r = 1
    theta_h = -2
    for i in range(n):
        # get s_i
        x_i = random.uniform(-1,1)
        y_i = -1 if x_i<theta else 1
        # update min and max
        if y_i==-1 :
            if x_i > max_l:
                max_l = x_i
        else:
            if x_i < min_r:
                min_r = x_i
    #calc theta
    theta_h = (min_r+max_l)/2
    gen_risk = abs(theta_h-theta)/2
    # print('theta: ', theta, ', theta_h: ', theta_h, ', gen_risk: ', gen_risk)
    # theta_h_data.append(theta_h)
    # gen_risk_data.append(gen_risk)
    return gen_risk

if __name__ == "__main__":
    main()