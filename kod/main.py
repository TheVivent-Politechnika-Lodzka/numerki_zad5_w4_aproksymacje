
from functions import print_fun
from legendre import Legendre
from charts import gen_chart

FUNSTR, FUN = print_fun()

# pobierz przedział
A = float(input("Podaj początek przedziału: "))
B = float(input("Podaj koniec przedziału: "))
if A > B: A,B = B,A

APROX = Legendre(FUN, A, B)

print("1. Chcę podać stopień wielomianu")
print("2. Chcę podać epsilon")
choice = int(input("# "))
if not choice in [1, 2]:
    exit("ಠ_ಠ")


POLY_SIZE = 0
EPS = None
if choice == 1: # wprowadzenie stopnia wielomianu
    POLY_SIZE = int(input("Podaj żądany stopień wielomianu: ")) + 1
    
    APROX.calcRootsAndWeights(POLY_SIZE) # przygotuj funkcje bazowe
    for i in range(POLY_SIZE): # policz c
        APROX.getNextC()

if choice == 2: # wprowadzenie epsilona
    EPS = float(input("Podaj epsilon: "))
    POLY_SIZE = 1
    while (APROX.getError() > EPS):
        POLY_SIZE += 1
        APROX.calcRootsAndWeights(POLY_SIZE)
        APROX.getNextC()
        if POLY_SIZE > 100:
            print("PRZEKROCZONO 100 STOPIEŃ WIELOMIANU, PRZERYWAM OBLICZENIA")
            break

print("Aproksymowana funkcja: {}".format(FUNSTR))
print("Wielomian aproksymacji: {}".format(APROX.getPolyAsString()))
print("Błąd aproksymacji: {}".format(APROX.getError()))

if EPS != None:
    print("Epsilon: {}".format(EPS))

# print()
# from utility import smartNewton
# print("Statystyki \"sprytnej\" funkcji do obliczania symbolu Newtona")
# print("needed: {}\ncalculated: {}".format(smartNewton.needed, smartNewton.calculated))

gen_chart(APROX.getPureX, APROX.getAprox, "wykresy/{}_od{}_do{}.jpg".format(input("Podaj nazwę pliku: "), A, B))