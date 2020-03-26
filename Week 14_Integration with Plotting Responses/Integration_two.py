from scipy.integrate import dblquad
import numpy as np

def integrand(y, x):
    'y must be the first argument, and x the second.'
    return y * np.sin(x) + x * np.cos(y)

ans, err = dblquad(integrand, np.pi, 2*np.pi,
                   lambda x: 0,
                   lambda x: np.pi)
print (ans)
