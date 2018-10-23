import numpy as np
from scipy import integrate

g = 9.8 #m/s^2
L = 1.0 #m
m = 1.0 #kg
b = 0.1 # friction coeff in SI smth

omega_0 = np.sqrt(g / L)
delta = 0.5 * b / m
y_0 = [np.pi - 0.2, 0]  #y = [alpha, omega]
t = (0.0, 10.0)

def pend_deriv(t, y):
    """returns dy/dt for odeint"""
    alpha, omega = y
    dydt = [omega, - 2 * delta * omega - omega_0 ** 2 * np.sin(alpha)]
    return dydt 

sol = integrate.solve_ivp(pend_deriv, t, y_0) #global variable
sol = sol.y
print(sol)