import numpy as np
import matplotlib.pyplot as plt


f = lambda x: np.sin(0.2*x) + np.sin(2*x) + 1

x = np.linspace(0,2*np.pi,100)
y = f(x)
print(y)
plt.plot(x,y)

X = np.linspace(np.pi/2,3*np.pi/2,100)
Y = f(X)
print(y)
plt.fill_between(X,Y)

plt.xticks([np.pi/2,3*np.pi/2],['$\pi/2$','$3\pi/2$']); plt.yticks([]);
plt.xlim([0,2*np.pi]); plt.ylim([0,3]);
plt.show()
