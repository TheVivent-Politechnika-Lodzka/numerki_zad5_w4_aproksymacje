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
        self.Pn = [P0, P1] # wskaźniki na przygotowane funkcje

        # miejsce na współczynniki
        self.c = []

    def getPureX(self, x):
        return self.FUN(x)

    def getIntegral(self, m):
        # policz wynik
        result = 0
        for i in range(0,m):
            # odpowiedni współczynnik * wartość funkcji w odpowiednim x
            # generalnie brałem stąd: https://www.pamoc.it/tpc_num_int.html#GLQ
            # ale na wiki pewnie też jest to samo
            # (nie ma tego mnożenia przez (b-a)/2, bo jest to już w adapterze)
            result += self.COEFS[m-2][i] * self.FUN(self.X[m-2][i])
        return result

    def getPolyAsString(self, round_to=3) -> str:
        # no, nie muszę chyba tłumaczyć
        # co robi ta funkcja
        coefs = self.c[::-1]

        to_return = ""
        for i in range(len(coefs)):
            to_return += "+" if coefs[i] >= 0 else ""
            to_return += str(round(coefs[i], round_to))
            to_return += "x" + sp(len(coefs)-i-1) if len(coefs)-i-1 != 0 else ""

        return to_return.lstrip("+")

    def getNextC(self):
        i = len(self.c) # pobierz który współczynnik teraz liczysz

        def top(x):
            return self.FUN(x) * self.Pn[i](x) # funkcja liczona * bazowa
   
        numerator = Legendre(top, -1, 1) # oblicz całkę
        numerator.calcRootsAndWeights(5)
        
        # wrzuć współczynnik do tablicy
        self.c.append( numerator.getIntegral(5) / ((i+0.5) ** (-1)) )
        # mianownik współczynnika to całka kwadratu Pi
        # ale z wykładu wiadomo, że całka taka wynosi (i+0.5) ** (-1)


    def getError(self, round_to=3):
        # błąd to kwadrat różnicy funkcji
        # a różnicę funkcji najlepiej policzyć całką
        def fun(x):
            return (self.FUN(x) - self.getAprox(x)) ** 2

        integral = Legendre(fun, -1, 1)
        integral.calcRootsAndWeights(5)
        return integral.getIntegral(5)

    def getAprox(self, x):
        # zwróci wartość aproksymacji w danym punkcie

        coefs = self.c
        
        # ta... niestety było trzeb rozdzielić, bo coś się pruł
        # ¯\_(ツ)_/¯
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
        # dwie pierwsze wartości są wpisane dla Pi
        # a dla X i COEF, nie mają one znaczenia
        # bo są zbyt niedokładne
        if roots < 2: raise Exception("LOL（⊙ｏ⊙）")

        # jeżeli jest już policzone, to nie licz drugi raz LUL
        if len(self.X) >= roots: return

        # jeżeli poprzedni nie są policzone, to je policz
        # żeby indexy w tablicach się zgadzały
        if len(self.Pn) < roots:
            self.calcRootsAndWeights(roots-1)

        # generator funkcji bazowych Pn
        # fajny, nie ?
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
        
        # fsolve i derivative ze scipy są
        # zbyt niedoskonałe, żeby liczyć 
        # rzeczy wyższe niż 6. I tak to jest
        # potrzebne do wyznaczania wartości całki
        # gdzie 6, daje już dość dokładny wynik
        # (pod warunkiem, że funkcja nie jest
        # zbyt skomplikowana), więc raczej spoko
        if roots < 7:
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
        

    