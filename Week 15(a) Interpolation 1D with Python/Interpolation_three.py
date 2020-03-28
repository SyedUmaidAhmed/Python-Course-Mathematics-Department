import numpy as np
from scipy import interpolate
import pylab as py

x = np.r_[0:10:10j]

y = np.cos(x)

f = interpolate.interp1d(x,y)


xnew = np.r_[0:10:100j]


py.figure(1)
py.clf()

py.plot(x,y,'ro',xnew,f(xnew),'b-')
py.show()