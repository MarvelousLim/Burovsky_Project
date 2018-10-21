from scipy import integrate

def odeint(dydt, y_0, t, *args):
    return integrate.odeint(dydt, y_0, t, args)
