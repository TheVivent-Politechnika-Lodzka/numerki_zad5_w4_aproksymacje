
from functions import print_fun
from legendre import Legendre
from charts import gen_chart

FUNSTR, FUN = print_fun()

# pobierz przedział
A = float(input("Podaj początek przedziału: "))
B = float(input("Podaj koniec przedziału: "))
if A > B: A,B = B,A

test = Legendre(FUN, A, B)

for i in range(2, 100):
    test.calcRootsAndWeights(i)

print(test.COEFS[24])


# x, y = test.getAprox(27)
# gen_chart(test.getPureX, x, y, "test")
