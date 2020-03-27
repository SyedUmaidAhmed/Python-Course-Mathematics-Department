from scipy.integrate import odeint # DE solve

import numpy as N
import matplotlib
import pylab

def f(y, t):
    return -2 * y * t

y0 = 1 #Questiom

# linspace
t = N.arange(0, 2, 0.01)  # values of t for which we require the solution y(t)

y = odeint(f, y0, t)  # actual computation of y(t)....func, value, put into


pylab.plot(t, y)
pylab.xlabel('t')
pylab.ylabel('y(t)')
pylab.show()
