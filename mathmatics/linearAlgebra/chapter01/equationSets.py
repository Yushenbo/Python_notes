#-*- coding:utf-8 -*-
#########################################################################
# File Name: equationSets.py
# Author: Shen Bo
# mail: nichol_shen@yahoo.com
# Created Time: Thu, May 03, 2018  3:07:48 PM
#########################################################################
#!usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

def function_draw():
    x = [-2, 2, -2, 2]
    y = [-4, 4, 0.5, 2.5]

    fig = plt.figure()
    plt.axhline(y = 0, c = 'black')
    plt.axvline(x = 0, c = 'black')


    plt.plot(x[:2], y[:2], x[2:], y[2:])


    plt.draw()
    plt.show()

def vector_draw():
    from functools import partial 

    fig = plt.figure()
    plt.axhline(y = 0, c = 'black')
    plt.axvline(x = 0, c = 'black')

    ax = plt.gca()
    ax.set_xlim(-2.5, 2.5)
    ax.set_ylim(-3, 4)

    arrow_vector = partial(plt.arrow, width = 0.01, head_width = 0.1,
            head_length = 0.2, length_includes_head = True)

    arrow_vector(0, 0, 2, -1, color = 'g')
    arrow_vector(0, 0, -1, 2, color = 'c')
    arrow_vector(2, -1, -2, 4, color = 'b')
    arrow_vector(0, 0, 0, 3, width = 0.05, color = 'r')

    plt.draw()
    plt.show()
    



if __name__ == '__main__':
    #function_draw()

    vector_draw()
