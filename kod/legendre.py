from scipy.optimize import fsolve
from scipy.misc import derivative
import numpy as np
from utility import funAdapter
from utility import smartNewton as sn
sn = sn.newtonSymbol

class Legendre:
    FUN = None
    a = 0
    b = 0

    # w_i
    COEFS = []

    # q_i
    X = []

    def  __init__(self, fun, a, b):
        self.a = a # początek przedziału
        self.b = b # koniec przdziału
        self.FUN = funAdapter(fun, self.a, self.b) # funkcja całkowana
        # ^^^adapter skalujący przedział z [a, b] na [-1, 1]

    def getPureX(self, x):
        return self.FUN(x)

    def getIntegral(self, m):
        # policz wynik
        result = 0
        for i in range(0,m):
            # odpowiedni współczynnik * wartość funkcji w odpowiednim x
            result += self.COEFS[m-2][i] * self.FUN(self.X[m-2][i])
        return result

    def calcRootsAndWeights(self, roots=2):
        if roots < 2: raise Exception("LOL")

        def Pn(n):
            def wrapper(q):
                # https://en.wikipedia.org/wiki/Legendre_polynomials
                # wzór na sumę iloczynów dwóch symboli newtona i potęgi ułamka
                to_return = 0
                for k in range(n+1):
                    to_return += sn(n, k) * sn(n+k, k) * (((q-1) * 0.5) ** k)
                return to_return

            return wrapper
        
        Pr = Pn(roots)
        qi = fsolve(Pr, np.linspace(-1,1,roots)) # znajdź miejsca zerowe, a więc qi
        wi = []
        for q in qi:
            # wzór jest na wiki
            wi.append(2 / \
                ((1-(q**2)) * (derivative(Pr, q, dx=0.0001)**2)) \
            )

        self.COEFS.append(wi)
        self.X.append(qi)
        

    def getAprox(self, roots=2):

        roots -=2
        x = self.X[roots]
        y = []

        for i in range(len(self.COEFS[roots])):
            result = self.COEFS[roots][i] * self.FUN(self.X[roots][i])
            y.append(result)

        return x, y
