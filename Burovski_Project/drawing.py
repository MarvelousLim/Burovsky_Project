import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from scipy import integrate

def draw(ode_sol, t, energy, m, L):
    head = 5
    fig = plt.figure()

    #first subplot: pendulum wavering
    ax1 = fig.add_subplot(2, 2, 1)
    ax1.set_xlim(-1.2, 1.2)
    ax1.set_ylim(-1.2, 1.2)
    ax1.set_aspect('equal')
    ax1.set_title('x-y coordinates')
    ax1.grid()

    #second: alpha wavering
    ax2 = fig.add_subplot(2, 2, 2)
    ax2.set_xlim(-np.pi, np.pi)
    ax2.set_ylim(t[0], t[-1])
    ax2.set_xlabel('alpha')
    ax2.set_title('alpha-t coordinates')
    ax2.grid()

    #third: energy line
    ax3 = fig.add_subplot(2, 2, 3)
    ax3.set_xlim(t[0], t[-1])
    ax3.set_ylim(0, energy[0] + 0.5)
    ax3.set_title('energy-t coordinates')
    ax3.grid()

    #forth: phase diagramm
    ax4 = fig.add_subplot(2, 2, 4)
    ax4.set_xlim(-np.pi, np.pi)
    ax4.set_ylim(-np.sqrt(2 * energy[0] / (m * L ** 2)), np.sqrt(2 * energy[0] / (m * L ** 2)))
    ax4.set_xlabel('alpha')
    ax4.set_ylabel('omega')
    ax4.set_title('phase diagramm')
    ax4.grid()


    def init(): # Initialize with a blank plot
        line1, = ax1.plot([], []) # an empty lines, global variables
        line1a, = ax1.plot([], [])
        line2, = ax2.plot([], [])
        line2a, = ax2.plot([], [])
        line3, = ax3.plot([], [])
        line3a, = ax3.plot([], [])
        line4, = ax4.plot([], [])
        line4a, = ax4.plot([], [])
        return line1, line1a, line2, line2a, line3, line3a, line4, line4a

    def animate(i):
        #first
        psi = ode_sol[i][0]
        x = [0, np.sin(psi)]
        y = [0, -np.cos(psi)]
        line1, = ax1.plot(x, y, '-', color = 'black')
        line1a, = ax1.plot(x[1], y[1], 'o', color = 'red')
        #second
        psi_arr = ode_sol[:i, 0]
        t_arr = t[:i]
        line2, = ax2.plot(psi_arr[:1 - head], t_arr[:1 - head], color = 'black')
        line2a, = ax2.plot(psi_arr[-head:], t_arr[-head:], color = 'red')
        #third
        energy_arr = energy[:i]
        line3, = ax3.plot(t_arr[:1 - head], energy_arr[:1 - head], color = 'black')
        line3a, = ax3.plot(t_arr[-head:], energy_arr[-head:], color = 'red')
        #forth
        omega_arr = ode_sol[:i, 1]
        line4, = ax4.plot(psi_arr[:1 - head], omega_arr[:1 - head], color = 'black')
        line4a, = ax4.plot(psi_arr[-head:], omega_arr[-head:], color = 'red')
        return line1, line1a, line2, line2a, line3, line3a, line4, line4a

    anim = animation.FuncAnimation(fig, animate, init_func = init, frames = len(t), interval = 20, blit = True)
    plt.legend()
    plt.tight_layout()  
    plt.show()