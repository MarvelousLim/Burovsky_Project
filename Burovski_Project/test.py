import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

y_0 = 3
threshold_low = 1
threshold_high = 2

def derv_ivp(t, y):
    global direction

    if (y < threshold_low):
        direction = 1
    if (y > threshold_high):
        direction = -1

    return direction

t = (0.0, 10.0)
direction = -1
sol = integrate.solve_ivp(derv_ivp, t, (y_0,), max_step = 0.01)

plt.plot(sol.t, sol.y[0,:], 'o')
plt.grid()
plt.show()