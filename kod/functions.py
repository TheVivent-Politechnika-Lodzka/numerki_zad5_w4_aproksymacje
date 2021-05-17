from numpy import sin, cos, tan, exp, arctan
from utility import horner

def cot(x):
    return 1/tan(x)

def csc(x):
    return 1/sin(x)

#####
def f0(x):
    # 2x + 4 [przedział -4 do 0]
    return 2 * x + 4
    
#####

#---#
def f1(x):
    # policzenie schematem hornera [przedział -3.5 do 3.7]
    # 0.3*x³ - 0.1x² - 3.7x + 0.4  [całka = -0.10008]
    coefficients = [0.3, -0.1, -3.7, 0.4]
    
    return horner(coefficients)(x)
#---#

#####
def f2(x):
    # policzenie schematem hornera [przedział -1.5 do 1.5]
    # 0.4x¹⁰ + 0.8x⁹ - 1.1x⁸ - 1.4x⁷ - 0.1x⁶ - 0.9x⁵ + 1.7x⁴ + 0.7x³ - 0.7x² + 0.2x + 2.3
    coefficients = [0.4, 0.8, -1.1, -1.4, -0.1, -0.9, 1.7, 0.7, -0.7, 0.2, 2.3]
    return horner(coefficients)(x)
#####

#---#
def f3(x):
    # przedział -1 do 1
    result = abs(x)
    return result
#---#

#####
def f4(x):
    # przedział -10 do 10
    result = cos(x)
    return result
#####

#---#
def f5(x):
    # przedział -1.5 do 1.5
    result = arctan(cos(abs(sin(x) * sin(x) * tan(x / 2)))) * x*x * sin( 26 + tan(sin(x) / cos(1999)))
    return result
#---#

'''
0. liniowa - done
1. wielomian 3 st - done
2. wielomian 10 st - done
3. abs - done
5. cos - done
4. skompikowane złożenie - done
'''

functions = [
    # 0:
    ["2x + 4", f0],
    # 1:
    ["0.4x⁵ - x⁴ + 0.1x³ + 0.9x² -0.3x + 0.5", f1],
    # 2:
    ["0.4x¹⁰ + 0.8x⁹ - 1.1x⁸ - 1.4x⁷ - 0.1x⁶ - 0.9x⁵ + 1.7x⁴ + 0.7x³ - 0.7x² + 0.2x + 2.3", f2],
    # 3:
    ["|x|", f3],
    # 4:
    ["cos(x)", f4],
    # 5:
    ["arctan(cos(|sin²(x) * tan(x/2)|))sin(26 + tan(sin(x) /cos(1999)))x²", f5]
]

def print_fun():
    for i in range(len(functions)):
        print(str(i) + ". " + functions[i][0])
    i = int(input("Wybierz funkcję: "))
    return functions[i][0],functions[i][1]