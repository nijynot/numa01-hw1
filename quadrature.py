#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 12:04:34 2017

@author: tony
"""

import numpy as np
import matplotlib.pyplot as plt


def ctrapezodial(f, a, b, n):
    h = (b - a) / n
    arr = []
    firstTerm = (h / 2) * (f(a) + f(b))
    for i in range(1, n):
        x_i = a + (i * b - i * a) / n
        arr.append(f(x_i))
    return firstTerm + h * sum(arr)

def e(x):
    return np.exp(x)

def factory(f, a, b):
    def container(increment):
        return ctrapezodial(f, a, b, increment)
    return container

trape = factory(e, 0, 2)

def approx(f, increment, tolerance):
    count = 1
    delta = 1
    while (delta > tolerance):
        delta = f(count * increment) - f(count * (increment + 1))
        count += 1
        print(delta)
    else:
        return f(count * (increment + 1))
        
def plot(f, a, b, n):
    integral_h = factory(f, a, b)
    integral = np.exp(2) - 1
    x = []
    y = []
    for i in range(1, n + 1):
        # data.append(integral_h(2 ** i))
        x.append((b - a) / (2 ** i))
        y.append(integral_h(2 ** i) - integral)
    plt.loglog(x, np.absolute(y))
    plt.grid(True)
    plt.show()

