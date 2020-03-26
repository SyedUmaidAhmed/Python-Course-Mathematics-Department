import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-1,3,1000)

def f(x):
    return x**2


plt.plot(x,f(x))
plt.axhline(color='red')

plt.fill_between(x, f(x), where = [(x>0) and (x<2) for x in x], color='blue', alpha =0.3)

# alpha is for transparency

plt.show()
