
from functions import print_fun
from legendre import Legendre

FUNSTR, FUN = print_fun()

# pobierz przedział
A = float(input("Podaj początek przedziału: "))
B = float(input("Podaj koniec przedziału: "))
if A > B: A,B = B,A

test = Legendre(FUN, A, B)

print(test.calc)