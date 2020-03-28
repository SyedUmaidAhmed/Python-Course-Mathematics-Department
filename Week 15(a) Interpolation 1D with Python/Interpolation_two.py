import numpy as np
from scipy import interpolate
import pylab as py

x = np.r_[0:10:11j]

y = np.exp(-x/4)*x

f = interpolate.interp1d(x,y)

xnew = np.r_[0:10:100j]

print(xnew)


py.figure(1)
py.clf()

py.plot(x,y,'ro','b-')


py.plot(x,y,'ro',xnew,f(xnew),'b-')


py.show()