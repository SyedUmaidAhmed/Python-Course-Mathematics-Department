import numpy as np


A = np.array([[20,10],[17,22]])
B = np.array([350,500])

x = np.linalg.solve(A,B)

print(x)