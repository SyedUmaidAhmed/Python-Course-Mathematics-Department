import numpy as np
from scipy import interpolate
import pylab as py



x = np.r_[0:10:11j]

y = np.exp(-x/4)*x

print(y)

f = interpolate.interp1d(x,y)


py.figure(1)

py.clf() #leave window open and clear the plots

py.plot(x,y,'ro')


py.show()