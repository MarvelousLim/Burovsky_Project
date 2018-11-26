import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

y_0 = 1
threshold = 0.01
t = np.linspace(0.0, 10.0, 100)
delta_t = t[1]

def derv(y, t):
    global delta_t
    dydt = -y
    if (y < threshold):
        dydt += 10 / delta_t
    return dydt 

sol = integrate.odeint(derv, y_0, t) #global variable

plt.plot(t, sol, 'o')
plt.grid()
plt.show()