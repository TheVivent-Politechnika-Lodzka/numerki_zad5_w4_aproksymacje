import math

def one(x):
    return math.sin(x) - x*x*x


def two(x):

    w = [0.25, -3, 0, 0, -5]
    value = 0;
    for i in range (4):
        value = value * x;
        value = value + w[i];
    return value;


def three(x):
    return x/math.sqrt(x*x+0.01)


def function_help(fun, x, C, deg, le):
    return (fun.value_of_function(x) - procedure(C, deg, x, le)) * (fun.value_of_function(x) - procedure(C, deg, x, le))


def procedure(C, deg, x, legendre_polies):
    result=0
    for i in range(0,deg+1):
        result = result+C[i]*legendre_polies[i].value_of_function(x)
    return result


def newton_symbol(a, b):
    return math.factorial(a)/(math.factorial(b)*math.factorial(a-b))


def simpson_method(p, k, n, fun1, fun2):
    delta = (k-p)/n
    result = fun1.value_of_function(p)*fun2.value_of_function(p)\
             + fun1.value_of_function(k)*fun2.value_of_function(k)
    for i in range(1,n):
        if i % 2 == 1:
            coe = 4
        else:
            coe = 2
        result = result+coe*fun1.value_of_function(p+i*delta)*fun2.value_of_function(p+i*delta)
    result=(delta/3)*result
    return result


def simpson_method_for_one_function(p, k, n, fun, C, deg,le):
    delta = (k-p)/n
    result = function_help(fun,p,C,deg,le) + function_help(fun,k,C,deg,le)
    for i in range(1,n):
        if i % 2 == 1:
            coe = 4
        else:
            coe = 2
        result = result+function_help(fun,p+i*delta,C,deg,le)
    result=(delta/3)*result
    return result

