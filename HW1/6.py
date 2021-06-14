import matplotlib.pyplot as plt
import numpy as np
import random

theta = 0.639
xs = []
# avg_risks = []
n = 7

def main():
    plt.ylim(-1, 1)
    x_l = -2
    x_r = 2
    print(theta)
    q = 0 #count queries
    t = 0 #coutnt round
    while q < n:
        x_t = random.uniform(-1,1)
        # print('l: ', x_l, 'r: ', x_r)
        plt.plot(t+1, x_t, 'o', color='black')
        plt.plot([t+1, t+1], [x_l, x_r], 'k', lw=2)
        if x_t > x_l and  x_t < x_r:
            plt.plot([t+1, t+1], [x_l, x_r], 'b', lw=2)
            y_t = get_y(x_t)
            if y_t == -1:
                x_l = x_t
            else:
                x_r = x_t
            q += 1
        t += 1
    plt.show()
    
def get_y(x):
    return -1 if x<theta else 1

if __name__ == "__main__":
    main()