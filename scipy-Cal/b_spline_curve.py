#-*- coding:utf-8 -*-
#########################################################################
# File Name: b_spline_curve.py
# Author: Nichol.Shen
# mail: nichol_shen@yahoo.com
#########################################################################
#!/usr/bin/env python3

import numpy as np
import pylab as pl
from scipy import interpolate

x = np.linspace(0, 2 * np.pi + np.pi/4, 10)
y = np.sin(x)

x_new = np.linspace(0, 2 * np.pi + np.pi/4, 100)

f_linear = interpolate.interp1d(x, y)
tck = interpolate.splrep(x, y)
y_bspline = interpolate.splev(x_new, tck)

pl.plot(x, y, "o", label = u"original data")

pl.plot(x_new, f_linear(x_new), label = u"Liner insert value")

pl.plot(x_new, y_bspline, label = u"B-spline insert value")

pl.legend()
pl.show()
