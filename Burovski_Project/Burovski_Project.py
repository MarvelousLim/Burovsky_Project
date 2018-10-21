import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import odesol

def pend_derivative(y, t, omega_0):


g = 9.8 #m/s^2
l = 1.0 #m
m = 1.0 #kg
omega_0 = np.sqrt(g / l)
y_0 = [np.pi / 3, 0] #[alpha, omega]
t = np.linspace(0.0, 10.0, 50)
pend_sol = odesol.odeint(pend_derivative, y_0, t, args = omega_0) # возможно, потребуется написать эту шляпу самому

print(pend_sol)
