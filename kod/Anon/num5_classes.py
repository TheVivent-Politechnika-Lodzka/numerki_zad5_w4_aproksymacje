import math
from num5_functions import newton_symbol
from num5_functions import one
from num5_functions import two
from num5_functions import three
functions_switch = [one, two, three]
class function:
    def __init__(self, c):
        self.choice = c
        self.pattern = functions_switch[self.choice-1]

    def value_of_function(self, x):
        return self.pattern(x)


class legendre_polynominal:
    def __init__(self, degree):
        self.n = degree

    def value_of_function(self, argument):
        coe = 1/(pow(2, self.n))
        result = 0
        i = 0
        while i <= self.n/2:
            result = result + \
                     pow(-1, i)*newton_symbol(self.n, i)*newton_symbol(2*self.n-2*i, self.n)*pow(argument, self.n-2*i)
            i=i+1

        result = coe*result
        return result
