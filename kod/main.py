
from functions import print_fun
from legendre import Legendre
from charts import gen_chart
from utility import smartNewton
import numpy as np

FUNSTR, FUN = print_fun()

# pobierz przedział
A = float(input("Podaj początek przedziału: "))
B = float(input("Podaj koniec przedziału: "))
if A > B: A,B = B,A

test = Legendre(FUN, A, B)


test.calcRootsAndWeights(6)
for i in range(6):
    test.getNextC()
print(test.getPolyAsString())

import matplotlib.pyplot as plt
from numpy import arange
from utility import horner

# x = arange(-1, 1, 0.01)
# # narysuj funkcje
# plt.plot(x, test.getPureX(x), "b-", label="orginalna")
# plt.plot(x, test.getAprox(x), "y-", label="aproksymowana", linestyle=":")
# # plt.plot(x, horner(test.getAllC())(x), "g-", label="aprox", linestyle=":")

# # narysuj legendę
# plt.legend(loc="upper right")

# # zapisz
# plt.show()

# print("needed: {}\ncalculated: {}".format(smartNewton.needed, smartNewton.calculated))