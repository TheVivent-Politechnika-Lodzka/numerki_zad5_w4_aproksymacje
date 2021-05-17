
from functions import print_fun
from legendre import Legendre
from charts import gen_chart


FUNSTR, FUN = print_fun()

# pobierz przedział
A = float(input("Podaj początek przedziału: "))
B = float(input("Podaj koniec przedziału: "))
if A > B: A,B = B,A

test = Legendre(FUN, A, B)

test.calcRootsAndWeights(10)

x, y = test.getAprox(6)
# gen_chart(test.getPureX, x, y, "test6")

test.getNextC()
test.getNextC()
test.getNextC()
test.getNextC()
test.getNextC()

print(test.getAllC())


import matplotlib.pyplot as plt
from numpy import arange
from utility import horner

x = arange(-1, 1, 0.01)
# narysuj funkcje
plt.plot(x, test.FUN(x), "b-", label="og")
plt.plot(x, test.getApproxX(x), "r-", label="aprox", linestyle=":")
plt.plot(x, horner(test.getAllC())(x), "g-", label="aprox", linestyle=":")

# narysuj legendę
plt.legend(loc="upper right")

# zapisz
plt.show()