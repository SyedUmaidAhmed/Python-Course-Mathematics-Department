import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def mixer(x,t,Tf,Caf):

    Ca = x[0]
    q = 100
    V = 100

    return (q/V*(Caf - Ca))

# Initial Condition
Ca0 = 0.0
Tf = 300
Caf = 1


# Time Interval (min)
t = np.linspace(0,10,100)

# Simulate mixer
Ca = odeint(mixer,Ca0,t,args=(Tf,Caf))

# Construct results and save data file
# Column 1 = time
# Column 2 = concentration
data = np.vstack((t,Ca.T)) # vertical stack
data = data.T             # transpose data
np.savetxt('data.txt',data,delimiter=',')

# Plot the results
plt.plot(t,Ca,'r-',linewidth=3)
plt.ylabel('Ca (mol/L)')
plt.legend(['Concentration'],loc='best')
plt.xlabel('Time (hr)')
plt.show()