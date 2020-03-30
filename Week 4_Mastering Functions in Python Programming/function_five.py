import math

def f(x):
    return math.sqrt(x+3) - x + 1


for x in [0,1,math.sqrt(2),math.sqrt(2)-1]:
    print("f({:.3f}) = {:.3f}".format(x,f(x)))
