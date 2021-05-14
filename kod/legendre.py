from utility import funDecorator

class Legendre:
    FUN = None
    a = 0
    b = 0
    # COEFS i X z `https://www.pamoc.it/tpc_num_int.html#GLQ`

    # w_i
    COEFS = [
        [1,        1,        0,        0,        0 ],
        [0.55556,  0.88889,  0.55556,  0,        0 ],
        [0.347855, 0.652145, 0.652145, 0.347855, 0 ],
        [0.236927, 0.478629, 0.568889, 0.478629, 0.236927 ],
        [0.171324, 0.360762, 0.467914, 0.467914, 0.360762, 0.171324 ]
    ]

    # q_i
    X = [
        [-0.57735,   0.57735,   0,        0,        0 ],
        [-0.774597,  0,         0.774597, 0,        0 ],
        [-0.861136, -0.339981,  0.339981, 0.861136, 0 ],
        [-0.906180, -0.538469,  0,        0.538469, 0.906180 ],
        [-0.932470, -0.661209, -0.238619, 0.238619, 0.661209, 0.932470 ]
    ]


    def  __init__(self, fun, a, b):
        self.a = a # początek przedziału
        self.b = b # koniec przdziału
        self.FUN_og = fun # funkcja całkowana
        self.FUN = funDecorator(fun, a, b) # funkcja całkowana
        # ^^^dekorator skalujący przedział z [a, b] na [-1, 1]

    def calc(self, m):
        # policz wynik
        result = 0
        for i in range(0,m):
            # odpowiedni współczynnik * wartość funkcji w odpowiednim x
            result += self.COEFS[m-2][i] * self.FUN(self.X[m-2][i])
        # poprawa wyniku w celu zeskalowania przedziału do [-1, 1]
        result *= (self.b-self.a) / 2
        return result

    def calcX(self):
        test = [self.X[4]]
        test.append([])

        for i in range(len(test[0])):
            result = self.COEFS[4][i] * self.FUN(test[0][i])
            # result *= (self.b-self.a)*2
            # result *= (self.a+self.b)/2
            # result *= (self.a-self.b)/2 + (self.b+self.a)/2
            # result *= -(self.a-self.b)/2
            test[1].append(result)

        # scaleX = self.X[0][0] / test[0][0]
        # scaleX = test[1][0] / self.FUN(self.X[0][0])

        # for i in range(len(test[0])):
            # test[0][i] *= self.X[4][i] / test[0][i]

            # test[0][i] = (self.a+self.b)/2 + ((self.b-self.a)*test[0][i])/2
            # test[0][i] *= (self.b-self.a)/2
            # test[0][i] += (self.a+self.b)/2


        return test

    def test(self, x):
        return self.COEFS[4][i] * self.FUN(x)