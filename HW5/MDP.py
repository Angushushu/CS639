import math
import numpy as np
import random
import matplotlib.pyplot as plt
from physic import physic

class MDP:
    def __init__(self, m_c, m_p, l, tri, delta):
        self.physic = physic(m_c, m_p, l, tri, delta)
    
    def step(self, s, F):
    # def step(self, s, F, print):
        if abs(s[0][0])>=(math.pi/2) or abs(s[2][0])>=10:
            return np.array([[s[0][0]],[s[1][0]],[s[2][0]],[s[3][0]]]),0 # s',r
        self.physic.init_s(s[0][0], s[1][0], s[2][0], s[3][0])
        self.physic.interval_update(F)
        return np.array([[self.physic.s[0][0]],[self.physic.s[1][0]],[self.physic.s[2][0]],[self.physic.s[3][0]]]),1 # s',r