#-*- coding:utf-8 -*-
#########################################################################
# File Name: lorenz.py
# Author: Nichol.Shen
# mail: nichol_shen@yahoo.com
#########################################################################
#!/usr/bin/env python3

from scipy.integrate import odeint
import numpy as np

def lorenz(w, t, p, r, b):
    #W vector position, parameters p, r, b
    #dx/dt, dy/dt, dz/dt values
    x, y, z = w
    #lorenz equation
    return np.array([p * (y - x), x * (r - z) - y, x * y - b * z])

t = np.arange(0, 30, 0.01) # create time tramp
# call odeint resove the lorenz equation

track1 = odeint(lorenz, (0.0, 1.00, 0.0), t, args=(10.0, 28.0, 3.0))
track2 = odeint(lorenz, (0.0, 1.01, 0.0), t, args=(10.0, 28.0, 3.0))

#draw
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

fig = plt.figure()
ax = Axes3D(fig)
ax.plot(track1[:, 0], track1[:, 1], track1[:, 2])
ax.plot(track2[:, 0], track2[:, 1], track2[:, 2])

plt.show()
