from SimpsonIntegration import SimpsonIntegration

import numpy as np
from scipy.integrate import simps

def myfunc(x):
    return np.sin(x)

xmin = 0
xmax = np.pi
Nc = 10

result = SimpsonIntegration.simpson(xmin, xmax, Nc, myfunc)
print("The result of your integral is {0:.3f}".format(result))

x = np.linspace(xmin,xmax,Nc+1)
y = myfunc(x)
scipy_res = simps(y,x)
print("The result of your integral carried out with scipy is {0:.3f}".format(scipy_res))
