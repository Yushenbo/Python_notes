#-*- coding:utf-8 -*-
#########################################################################
# File Name: leastsq.py
# Author: Nichol.Shen
# mail: nichol_shen@yahoo.com
#########################################################################
#!/usr/bin/env python3

import numpy as np
from scipy.optimize import leastsq
import pylab as pl

def func(x, p):
    """
    数据拟合所用函数：A * sin(2 * pi * k * x + theta)
    """
    A, k, theta = p
    return A * np.sin(2 * np.pi * k * x + theta)

def residuals(p, y, x):
    """
    实验数据 x， y和拟合函数之间的差， p为拟合需要找到的系数
    """
    return y - func(x, p)

x = np.linspace(0, -2 * np.pi, 100)
A, k, theta = 10, 0.34, np.pi/6 #The real Data for parameters
y0 = func(x, [A, k, theta]) # The original data
y1 = y0 + 2 * np.random.randn(len(x)) # Add the noise statistics data

p0 = [7, 0.2, 0] # 第一次猜测的函数拟合函数

# Call leastsq for data fitting(数据拟合)
# residuals for caculating deviation
# p0 is the original value of data fitting function
# args is traial data for fitting action
plsq = leastsq(residuals, p0, args = (y1, x))

print(u"Real parameters: ", [A, k, theta])
print(u"Fitting parameters: ", plsq[0])

pl.plot(x, y0, label=u"Real data")
pl.plot(x, y1, label=u"With noise data")
pl.plot(x, func(x, plsq[0]), label=u"Fitting data")

pl.legend()
pl.show()

