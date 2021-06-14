import math
import numpy as np
import random
import matplotlib.pyplot as plt
from physic import physic

physic = physic(1, 0.2, 0.5, 2, 0.001) #m_c, m_p, l, tri, delta
physic.init_s(math.pi, 0, 0, 0) #theta, theta_v, x, x_v
physic.interval_update(9.8*1.2)
# physic.interval_update(1)