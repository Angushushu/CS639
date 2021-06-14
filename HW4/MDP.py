import math
import numpy as np
import random
import matplotlib.pyplot as plt

class MDP:
    def __init__(self, n, p):
        self.n = n
        self.p = p
        self.cur_s = 1
        self.n_states = 2*n+1
        self.P_ = np.zeros((3*self.n_states,self.n_states)) # in, out, clockwise
        for s in range(self.n_states):
            if s%n == 0:
                self.P_[s][s] = self.P_[s+self.n_states][s] = self.P_[s+2*self.n_states][s] = 1
            else:
                self.P_[s][max(s-n,0)] = 1
                if s>0 and s<n: # s=2...n
                    self.P_[self.n_states+s][s+n] = 1
                elif s>n+0 and s<2*n: # s=n+2...2n
                    self.P_[self.n_states+s][s] = 1
                self.P_[2*self.n_states+s][s+1] = 1
    
    def reset(self):
        self.cur_s = 1
        return self.cur_s
    
    def do(self, s, a): # a = 0:in/1:out/2:clockwise
        if np.random.multinomial(1, [self.p,1-self.p])[0] == 1:
            s_ = 1
        else:
            s_ = np.argmax(self.P_[s+a*self.n_states])
        r = 0
        if s == 0:
            r = -1
        elif s == self.n:
            r = 2
        elif s == 2*self.n:
            r = 1
        return [r, s_]

        
