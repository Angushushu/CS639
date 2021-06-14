import math
import numpy as np
import random
import matplotlib.pyplot as plt

class physic:
    def __init__(self, m_c, m_p, l, tri, delta): #m_c, m_p, l, tri, delta
        self.l = l
        self.m_c = m_c
        self.m_p = m_p
        self.g = 9.8
        self.tri = tri
        self.delta = delta
        self.s = None
    
    def init_s(self, a, a_v, x, x_v): #a, a_v, x, x_v
        self.s = np.array([[a],[a_v],[x],[x_v]])

    # def interval_update(self, F):
    def interval_update(self, F): # for 2a

        # a_s = []
        # x_s = []
        # i_delta = []

        for i in range(int(self.tri/self.delta)):
            # self.sub_interval_update(F)
            if i == 0:
                self.sub_interval_update(F, True) # for 2a
            else:
                self.sub_interval_update(F, False)
            # For Q1
        #     if i < 10:
        #         print(round(i*self.delta,6), round(self.s[0][0],6), round(self.s[1][0],6), round(self.s[2][0],6), round(self.s[3][0],6))
        #         # print(i*self.delta, self.s[0][0], self.s[1][0], self.s[2][0], self.s[3][0])
        #     a_s.append(self.s[0][0])
        #     x_s.append(self.s[2][0])
        #     i_delta.append(i*self.delta)
        # plt.xlabel('i*delta')
        # plt.ylabel('theta')
        # plt.plot(i_delta, a_s, 'o', color='red', markersize=1)
        # plt.show()
        # plt.ylabel('x')
        # plt.plot(i_delta, x_s, 'o', color='blue', markersize=1)
        # plt.show()

    # def sub_interval_update(self, F):
    def sub_interval_update(self, F, printable): # for 2a
        a = self.s[0][0]
        a_v = self.s[1][0]
        a_a = self.get_angle_a(a, a_v, F)

        # if printable:
        #     print('a_a:', a_a)

        x = self.s[2][0]
        x_v = self.s[3][0]
        x_a = self.get_cart_a(a, a_v, a_a, F)

        # if printable:
        #     print('x_a:', x_a)

        self.s = np.array([[a+a_v*self.delta],[a_v+a_a*self.delta],[x+x_v*self.delta],[x_v+x_a*self.delta]])

    def get_angle_a(self, a, a_v, F):
        parentheses1 = (-F-self.m_p*self.l*(a_v**2)*math.sin(a))/(self.m_c+self.m_p)
        parentheses2 = 4.0/3-self.m_p*(math.cos(a)**2)/(self.m_c+self.m_p)
        return (self.g*math.sin(a)+math.cos(a)*parentheses1)/(self.l*parentheses2)

    def get_cart_a(self, a, a_v, a_a, F):
        numerator = F+self.m_p*self.l*((a_v**2)*math.sin(a)-a_a*math.cos(a))
        return numerator/(self.m_c+self.m_p)
