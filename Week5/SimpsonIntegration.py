class SimpsonIntegration:
    """
    Class to setup an integration instance with an associated function.

    Parameters
    ----------
    function: callable
        The function to be integrated.
    eps: float
        A value defining the absolute precision of the integration.
    """

    def __init__(self, function, eps=1e-3):
        self.setFunction(function)
        self.setEPS(eps)

    def setFunction(self, function):
        if not callable(function):
            raise TypeError("You have not supplied a valid function")
        self.functionToBeIntegrated = function
        
    def setEPS(self, eps):
        if eps <= 0:
            raise ValueError("Precision must be a positive number")
        self.eps = eps

    def evaluate(self, a, b):

        err = 1e5
        N = 10
        old = 0

        while err > self.eps:
            current = self.simpson(a, b, N, self.functionToBeIntegrated)
            err = abs(current - old)
            N = 2 * N
            old = current

        return current

    @staticmethod
    def simpson(a, b, N, f):

        """
        Simpson rule for numerical integration of a function.

        Parameters:
        -----------
        a: float
            Lower bound of the integral
        b: float
            Upper bound of the integral (must be >a)
        N: int
            Number of intervals (must be an even number)
        f: callable
            Function to be integrated
        """

        if a >= b:
            raise ValueError(
                "The lower bound is greater than or equal to the upper bound"
            )
        
        if not isinstance(N, int):
            raise TypeError(
                "The number of intervals must be an integer"
            )

        if (N%2 != 0):
            raise ValueError(
                "The Simpson's rule requires an even number of intervals"
            )
        
        dx = (b - a) / N

        integral = 0

        fa = f(a)
        fb = f(b)

        for i in range(1,N):

            xi = a + i * dx

            if (i%2 == 1):
                integral += 4*f(xi)
            else:
                integral += 2*f(xi)

        integral += f(a) + f(b)
        integral = dx/3 * integral

        return integral






   
