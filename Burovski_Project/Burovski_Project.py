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
dt = 0.05 #crutch for solve_ivp, or therell be not enought points on graphs

#useless function
def periodic_cond(psi):
    return (psi + np.pi) % (2 * np.pi) - np.pi

def marvelous_strike(y):
    return [y[0], y[1] + 0.4 * np.sign(y[1]) * np.sqrt(2 * energy_calc(y_0) / (m * L ** 2))]

#event function, which stops evaluation, if energy decreased in 2 times
def marvelous_strike_cond(t, y):
    return energy_calc(y) - 0.5 * energy_calc(y_0)
marvelous_strike_cond.terminal = True
marvelous_strike_cond.direction = -1

def energy_calc(y):
    """returns energy of the state (alpha, omega)"""
    alpha, omega = y
    K = 0.5 * m * L * L * omega * omega
    P = m * g * L * (1 - np.cos(alpha)) 
    return K + P

def pend_deriv(t, y):
    """returns dy/dt for odeint or whatever"""
    alpha, omega = y
    dydt = [omega, - 2 * delta * omega - omega_0 ** 2 * np.sin(alpha)]
    return dydt


#big nonelegant part, which solves evaluation from event to event and sew them together
#make sure: marvelous_strike have to drive system out of marvelous_strike_cond zone
status = 1
t_temp = t
y_0_temp = y_0
t = []
ode_sol = []
while status == 1:
    ode_sol_temp = integrate.solve_ivp(pend_deriv, t_temp, y_0_temp, max_step = dt, events = marvelous_strike_cond) #global variable
    status = ode_sol_temp.status
    t += ode_sol_temp.t.tolist()
    ode_sol += ode_sol_temp.y.transpose().tolist()
    print(ode_sol_temp.t_events)
    t_temp = (t[-1], t_temp[1])
    y_0_temp = ode_sol[-1]
    y_0_temp = marvelous_strike(y_0_temp) 

energy = [energy_calc(y) for y in ode_sol]

# Here we done with calculations, so we do nice (or not) pic 
#################################################################################################
#################################################################################################
#################################################################################################

dr.draw(np.array(ode_sol), np.array(t), np.array(energy), m, L)
