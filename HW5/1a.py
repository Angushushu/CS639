import math
import numpy as np
import random
import matplotlib.pyplot as plt
from physic import physic

physic = physic(1, 0.2, 0.5, 0.1, 0.001) #m_c, m_p, l, tri, delta
physic.init_s(math.pi, 0, 0, 1) #theta, theta_v, x, x_v
physic.interval_update(0)