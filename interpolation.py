#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 16:47:31 2017

@author: tony
"""

import numpy as np
import matplotlib.pyplot as plt

x = [0, 0.5, 1, 1.5, 2, 2.5]
y = [-2, 0.5, -2, 1, -0.5, 1]

def vandermonde(x):
    return np.vander(x, len(x))

def interpoly(x, y):
    V = vandermonde(x)
    return np.linalg.solve(V, y)
    
def polyval(c, z):
    N = len(c)
    sum = 0
    for i in range(0, N):
        sum += c[i] * (z ** ((N - 1) - i))
    return sum
    
def plot(x, y):
    c = interpoly(x, y)
    p = np.poly1d(c)
    xp = np.linspace(0, 3, 100)
    plt.plot(xp, p(xp), x, y, '*')
    plt.xlim(0, 3)
    plt.ylim(-5, 3)
    plt.show()