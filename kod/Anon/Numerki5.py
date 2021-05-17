from num5_functions import simpson_method
from num5_functions import simpson_method_for_one_function
from num5_functions import procedure
from num5_classes import function
from num5_classes import legendre_polynominal
import matplotlib.pylab as pylab

D = []
C = []
legendre_polies = []
choice = input("Wybierz funkcje \n1: sinx-x^3 \n2: 0.25*x^4-3x^3-5 \n3: |x^2-7|")
choice = int(choice)
if choice == 1 or choice == 2 or choice == 3:
    fun = function(int(choice))
    p = -1
    k = 1
    deg = input("Podaj stopien wielomianu Legendre'a: ")
    n = input("Podaj liczbe przedzialow do calkowania: ")
    p = float(p)
    k = float(k)
    n = int(n)
    deg = int(deg)
    for i in range(deg+1):
        legendre_polies.append( legendre_polynominal(i) )

    for i in range(0,deg+1):
        C.append( simpson_method(p, k, n, legendre_polies[i], fun) / simpson_method(p, k, n, legendre_polies[i], legendre_polies[i]) )

    result = 0

    helping = 0
    val = []
    arg = []
    while(helping < (k - p) ):
        arg.append(p+helping)
        val.append(procedure(C,deg,p+helping,legendre_polies))
        helping = helping + 0.001
    helping=0
    valfun = []
    argfun = []
    while (helping < (k - p)):
        argfun.append(p + helping)
        valfun.append(fun.value_of_function(p + helping))
        helping = helping + 0.001
    pylab.plot(argfun, valfun, 'b')
    pylab.plot(arg,val,'r')
    pylab.legend(('funkcja poczatkowa' , 'funkcja aproksymujaca'))
    pylab.show()

    error = simpson_method_for_one_function(-1,1,n,fun,C,deg,legendre_polies)
    print ("\nBlad aproksymacji to: " , error )
