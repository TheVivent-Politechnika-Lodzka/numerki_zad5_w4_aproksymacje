def funAdapter(fun, A, B):
    
    def wrapper(x):
        x = (A+B)/2 +\
            ((B-A)*x)/2
        return (B-A)/2 * fun(x)
    
    return wrapper

# class smartFactorial(object):

#     knownFacs = [1]

#     @classmethod
#     def factorial(self, x):
#         try:
#             return self.knownFacs[x]
#         except:
#             self.knownFacs.append(self.factorial(x-1)*x)
#             return self.knownFacs[x]

class smartNewton(object):

    knownNewton = [[1]]
    needed = 0
    calculated = 0

    @classmethod
    def newtonSymbol(self, x, y):
        try:
            self.needed += 1
            return self.knownNewton[x][y]
        except:
            self.calculated += 1
            if len(self.knownNewton) < x:
                self.newtonSymbol(x-1, x-1)
            
            self.knownNewton.append([1])

            for i in range(1, len(self.knownNewton[x-1])):
                self.knownNewton[x].append(\
                    self.knownNewton[x-1][i-1] + \
                    self.knownNewton[x-1][i]
                    )

            self.knownNewton[x].append(1)
            return self.knownNewton[x][y]


def horner(coefs):

    def wrapper(x):
        
        coefs.reverse()
        to_return = coefs[0]
        coefs.pop(0)

        for coef in coefs:
            to_return *= coef
            to_return += x

        return to_return

    return wrapper

def superScript(x : int) -> str:
    superscr = "⁰¹²³⁴⁵⁶⁷⁸⁹"

    to_return = ""
    while x > 0:
        i = x%10
        x = x // 10
        to_return = superscr[i] + to_return

    return to_return