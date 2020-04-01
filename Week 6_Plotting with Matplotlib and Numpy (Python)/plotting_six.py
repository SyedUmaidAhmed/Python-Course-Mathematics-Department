import matplotlib.pylab as plt
import numpy as np

in_array = np.linspace(-(2*np.pi),2*np.pi,40)
out_array = np.cos(in_array)

print(in_array)

print(out_array)


plt.plot(in_array,out_array,color='red',marker='o')
plt.title('Cos(x)')
plt.show()