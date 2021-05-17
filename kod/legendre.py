from scipy.optimize import fsolve
from scipy.misc import derivative
import numpy as np
from utility import funAdapter
from utility import smartNewton as sn
sn = sn.newtonSymbol
from utility import superScript as sp

def P0(x):
    try:
        return [1] * len(x)
    except:
        return 1

def P1(x):
    return x

class Legendre:


    def  __init__(self, fun, a, b):
        self.a = a # początek przedziału
        self.b = b # koniec przdziału
        self.FUN = funAdapter(fun, self.a, self.b) # funkcja całkowana
        # ^^^adapter skalujący przedział z [a, b] na [-1, 1]

        # w_i
        self.COEFS = []

        # q_i
        self.X = []

        # Pn
        self.Pn = [P0, P1]

        self.c = []

    def getPureX(self, x):
        return self.FUN(x)

    def getIntegral(self, m):
        # policz wynik
        result = 0
        for i in range(0,m):
            # odpowiedni współczynnik * wartość funkcji w odpowiednim x
            result += self.COEFS[m-2][i] * self.FUN(self.X[m-2][i])
        return result

    def getPolyAsString(self) -> str:
        coefs = self.c[::-1]

        to_return = ""
        for i in range(len(coefs)):
            to_return += "+" if coefs[i] >= 0 else ""
            to_return += str(coefs[i])
            to_return += "x" + sp(len(coefs)-i-1) if len(coefs)-i-1 != 0 else ""

        return to_return.lstrip("+")

    def getNextC(self):
        i = len(self.c)

        def top(x):
            return self.FUN(x) * self.Pn[i](x)
   
        numerator = Legendre(top, -1, 1)
        numerator.calcRootsAndWeights(i+2)

        self.c.append( numerator.getIntegral(i+2) / (((i)+0.5) ** (-1)) )


    def getAprox(self, x):
        
        coefs = self.c
        
        if type(x) == np.ndarray:
            to_return = [0] * len(x)
            for i in range(len(coefs)):
                for j in range(len(x)):
                    to_return[j] += coefs[i] * self.Pn[i](x[j])
        
        else:
            to_return = 0
            for i in range(len(coefs)):
                to_return += coefs[i] * self.Pn[i](x)
        
        return to_return

    def calcRootsAndWeights(self, roots=2):
        if roots < 2: raise Exception("LOL（⊙ｏ⊙）")
        if len(self.X) >= roots: return

        if len(self.Pn) < roots:
            self.calcRootsAndWeights(roots-1)

        def Pn(n):
            def wrapper(q):
                # https://en.wikipedia.org/wiki/Legendre_polynomials
                # wzór na sumę iloczynów dwóch symboli newtona i potęgi ułamka
                to_return = 0
                for k in range(n+1):
                    to_return += sn(n+k, k) * sn(n, k) * (((q-1) * 0.5) ** k)
                return to_return

            return wrapper
        
        Pr = Pn(roots)
        qi = fsolve(Pr, np.linspace(-1, 1, roots)) # znajdź miejsca zerowe, a więc qi
        wi = []
        for q in qi:
            # wzór jest na wiki
            wi.append(2 / \
                ((1-(q**2)) * (derivative(Pr, q, dx=1e-10)**2)) \
            )

        self.COEFS.append(wi)
        self.X.append(qi)
        self.Pn.append(Pr)
        

    