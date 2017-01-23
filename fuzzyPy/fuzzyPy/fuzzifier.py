#import numpy as np

class FuzzyPy():
    # Defines TRiangular membership finction f:x->y, with 'a' and 'c' the base of triangle and 'b' is peak
    def trimf(self, x, a, b, c):
        X1 = (x - a) / (b - a)
        X2 = (c - x) / (c - b)
        X3 = np.minimum(X1, X2)
        X4 = np.zeros(x.size)
        y = np.maximum(X3, X4)
        return y

    # Defines Trapezoidal membership finction f:x->y, with 'a' and 'd' the base of trpezoid and 'b' and 'c' the shoulder
    def trapmf(self, x, a, b, c, d):
        X1 = (x - a) / (b - a)
        X2 = np.ones(x.size)
        X3 = (d - x) / (d - c)
        X4 = np.minimum(np.minimum(X1, X2), X3)
        X5 = np.zeros(x.size)
        y = np.maximum(X4, X5)
        return y

    def gaussmf(self, x, c, v):
        y = np.exp(-(x - c) ^ 2 / 2 * v ^ 2)
        return y

class Triangle(FuzzyPy):
    def __init__(self, x, low, middle, high):
        self.low = self.trimf(x, low[0], low[1], low[2])
        self.middle = self.trimf(x, middle[0], middle[1], middle[2])
        self.high = self.trimf(x, high[0], high[1], high[2])



class Trapezoid(FuzzyPy):
    def __init__(self, x, low, middle, high):
        self.low = self.trapmf(x, low[0], low[1], low[2], low[3])
        self.middle = self.trapmf(x, middle[0], middle[1], middle[2], middle[3])
        self.high = self.trapmf(x, high[0], high[1], high[2], high[3])




class Gauss(FuzzyPy):
    def __init__(self, x, low, middle, high):
        self.low = self.gaussmf(x, low[0], low[1])
        self.middle = self.gaussmf(x, middle[0], middle[1])
        self.high = self.gaussmf(x, high[0], high[1])

