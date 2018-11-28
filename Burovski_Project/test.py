import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

y_0 = 3
threshold_low = 1
threshold_high = 2
t = np.linspace(0.0, 10.0, 1000)
direction = -1

def derv(y, t):
    global direction

    if (y < threshold_low):
        direction = 1
    if (y > threshold_high):
        direction = -1

    return direction

sol = integrate.odeint(derv, y_0, t) #global variable

plt.plot(t, sol, 'o')
plt.grid()
plt.show()