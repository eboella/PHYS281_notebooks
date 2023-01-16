from SimpsonIntegration import SimpsonIntegration

import numpy as np
from scipy.integrate import quad

def myfunc(x):
    return np.sin(np.exp(x))

xmin = -np.pi
xmax = np.pi

my_integral = SimpsonIntegration(myfunc, 1e-4)
result = my_integral.evaluate(xmin, xmax)
print("The result of your integral is {0:.5f}".format(result))

scipy_res = quad(myfunc, xmin, xmax)
print("The result of your integral carried out with scipy is {0:.5f}".format(scipy_res[0]))

