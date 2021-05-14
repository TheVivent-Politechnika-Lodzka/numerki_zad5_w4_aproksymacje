import matplotlib.pyplot as plt
from numpy import arange

def gen_chart(fun, a, b, filename, lege, simp):
    # wczyczyść figurę
    plt.clf()

    # narysuj oś x i y
    # plt.axhline(0, color='black')
    # plt.axvline(0, color='black')

    x = arange(a, b, 0.01)
    # narysuj funkcje
    plt.plot(x, fun(x), "b-", linewidth=4, label="funkcja")
    plt.plot(lege[0], lege[1], "r-", label="Legendre")
    if simp != None: plt.plot(simp[0], simp[1], "y-", label="Simpson")
    
    # narysuj legendę
    plt.legend(loc="upper right")

    # zapisz
    plt.savefig(filename)