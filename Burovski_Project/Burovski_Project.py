import numpy as np
from scipy import integrate
import drawing as dr

g = 9.8 #m/s^2
L = 1.0 #m
m = 1.0 #kg
b = 0.1 #friction coeff in SI-smth

omega_0 = np.sqrt(g / L)
delta = 0.5 * b / m
y_0 = [np.pi - 0.2, 0] #y = [alpha, omega]
t = (0.0, 100.0)
dt = 0.1 #crutch for solve_ivp, or therell be not enought points on graphs

#useless function
def periodic_cond(psi):
    return (psi + np.pi) % (2 * np.pi) - np.pi

#event function, which stops evaluation, if energy decreased in 2 times
def marvelous_strike(t, y):
    return energy_calc(y) - 0.5 * energy_calc(y_0)
#marvelous_strike.terminal = True
marvelous_strike.direction = 1

def energy_calc(y):
    """returns energy of the state"""
    alpha, omega = y
    K = 0.5 * m * L ** 2 * omega ** 2
    P = m * g * L * (1 - np.cos(alpha)) 
    return K + P

def pend_deriv(t, y):
    """returns dy/dt for odeint or whatever"""
    alpha, omega = y
    dydt = [omega, - 2 * delta * omega - omega_0 ** 2 * np.sin(alpha)]
    return dydt

ode_sol = integrate.solve_ivp(pend_deriv, t, y_0, max_step = dt, events = marvelous_strike) #global variable
print(ode_sol.t_events, ode_sol.message)
t = ode_sol.t
ode_sol = ode_sol.y.transpose()
energy = [energy_calc(y) for y in ode_sol]

# Here we done with calculations, so we do nice (or not) pic 
#################################################################################################
#################################################################################################
#################################################################################################

dr.draw(ode_sol, t, energy, m, L)
