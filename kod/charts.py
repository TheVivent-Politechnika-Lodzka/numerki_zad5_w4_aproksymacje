import matplotlib.pyplot as plt
from numpy import arange

def gen_chart(fun, aprox, filename):
    # wyczyść figurę
    plt.clf()

    x = arange(-1, 1, 0.001)
    # narysuj funkcje
    plt.plot(x, fun(x), "b-", label="funkcja")
    plt.plot(x, aprox(x), "r-", label="aproksymacja", linestyle=":")
    
    # narysuj legendę
    plt.legend(loc="upper right")

    # zapisz
    plt.savefig(filename)