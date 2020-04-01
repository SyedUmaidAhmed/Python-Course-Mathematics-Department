import matplotlib.pylab as plt
import numpy as np

x = np.linspace(np.pi, -np.pi, 40) #START,STOP,STEPS

plt.plot(x, np.sin(x))#40 VALUES

plt.xlabel('Angle[rad]')
plt.ylabel('Sin(x)')
plt.show()