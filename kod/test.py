from scipy.optimize import fsolve
import numpy as np




def Pn(n):

    def wrapper(q):
        # https://en.wikipedia.org/wiki/Legendre_polynomials
        # wzór na sumę iloczynów dwóch symboli newtona i potęgi ułamka
        sn = smartNewton.newtonSymbol
        to_return = 0
        for k in range(n+1):
            to_return += sn(n, k) * sn(n+k, k) * (((q-1) * 0.5) ** k)
        return to_return

    return wrapper 

if __name__ == "__main__":
    size = int(input("ile miejsc zerowych? "))
    P = Pn(size)
    
    t = fsolve(P, np.linspace(-1,1,size))
    print(t)
    print(type(t[0]))

    # import matplotlib.pyplot as plt
    # from numpy import arange
    # x = arange(-1, 1, 0.01)
    # plt.plot(x, P(x), "b-", label="funkcja")
    # plt.grid()
    # plt.show()

    # x = np.linspace(-1,1,1000)
    # xout = []
    # for i in range(len(x)):
    #     xout.append([x[i], P(x[i])])

    # xout = sorted(xout,key=lambda xout: abs(xout[1]))
    # xout = np.array(xout)

    # print(xout)

# for i in range(size):
#     print(xout[i][0])