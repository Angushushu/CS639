import math
import numpy as np
import random
import matplotlib.pyplot as plt
from MDP import MDP

env = MDP(10, 0.1) # n,p
pi_all_in = [0]*21
pi_all_out = [1]*21
pi_all_clockwise = [2]*21
visits = [0]*21
visits[1] = 1
s = 0

# all-in
for step in range(10000):
    if step == 0:
        s = env.reset()
    res = env.do(s, pi_all_in[s])
    r = res[0]
    s = res[1]
    visits[s] += 1

print('All-in\n', visits)
visits = [0]*21
visits[1] = 1

# all-out
for step in range(10000):
    if step == 0:
        s = env.reset()
    res = env.do(s, pi_all_out[s])
    r = res[0]
    s = res[1]
    visits[s] += 1

print('All-out\n', visits)
visits = [0]*21
visits[1] = 1

# all-clockwise
for step in range(10000):
    if step == 0:
        s = env.reset()
    res = env.do(s, pi_all_clockwise[s])
    r = res[0]
    s = res[1]
    visits[s] += 1

print('All-clockwise\n', visits)
visits = [0]*21
visits[1] = 1

# uniform
for step in range(10000):
    if step == 0:
        s = env.reset()
    res = env.do(s, np.argmax(np.random.multinomial(1, [1/3]*3)))
    r = res[0]
    s = res[1]
    visits[s] += 1

print('Uniform\n', visits)
    
