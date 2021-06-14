import matplotlib.pyplot as plt
import numpy
import random

theta = 0.639
theta_h_data = []
gen_risk_data = []

def main():
    print(theta)
    for i in range(100000):
        train()
    plt.hist(theta_h_data, bins = 100)
    fig1 = plt.gcf()
    fig1.set_size_inches(7.2, 4.2)
    fig1.savefig('C:/Users/Admin/Desktop/CS639/theta_h.png', dpi=100)
    plt.close()
    
    plt.hist(gen_risk_data, bins = 100)
    fig2 = plt.gcf()
    fig2.set_size_inches(7.2, 4.2)
    fig2.savefig('C:/Users/Admin/Desktop/CS639/gen_risk.png', dpi=100)
    

def train():
    max_l = -1
    min_r = 1
    theta_h = -2
    for i in range(1):
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
    theta_h_data.append(theta_h)
    gen_risk_data.append(gen_risk)

if __name__ == "__main__":
    main()