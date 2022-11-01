from SimpsonIntegration import SimpsonIntegration

import numpy as np
from scipy.integrate import simps

def myfunc(x):
    return np.exp(-x) * x**5

xmin = 0
xmax = 1

my_integral = SimpsonIntegration(myfunc, 1e-4)
result = my_integral.evaluate(xmin, xmax)
print("The result of your integral is {0:.5f}".format(result))

Nc = 10
x = np.linspace(xmin,xmax,Nc+1)
y = myfunc(x)
scipy_res = simps(y,x)
print("The result of your integral carried out with scipy is {0:.5f}".format(scipy_res))

"""
Now write a code to integrate sin(exp(x)) between -pi and pi using SimpsonIntegration.
The code should provide the result with a precision of 1e-3.
Compare your result with the result provided by scipy.integrate.quad. 
"""