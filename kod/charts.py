import matplotlib.pyplot as plt
from numpy import arange

def gen_chart(fun, aprox_x, aprox_y, filename):
    # wyczyść figurę
    plt.clf()

    x = arange(-1, 1, 0.01)
    # narysuj funkcje
    plt.plot(x, fun(x), "b-", label="funkcja")
    plt.plot(aprox_x, aprox_y, "r-", label="aproksymacja")
    
    # narysuj legendę
    plt.legend(loc="upper right")

    # zapisz
    plt.savefig(filename)