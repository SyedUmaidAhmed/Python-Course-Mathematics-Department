from scipy.integrate import quad

def integrand(x):
    return x**2

ans, err = quad(integrand, 0, 1)
print (ans)
