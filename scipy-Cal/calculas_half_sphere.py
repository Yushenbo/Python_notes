#-*- coding:utf-8 -*-
#########################################################################
# File Name: calculas_half_sphere.py
# Author: Nichol.Shen
# mail: nichol_shen@yahoo.com
#########################################################################
#!/usr/bin/env python

from scipy import integrate

def half_circle(x):
    return (1 - x ** 2) ** 0.5

def half_sphere(x, y):
    return (1 - x ** 2 - y ** 2) ** 0.5

S3 = integrate.dblquad(half_sphere, -1, 1,
        lambda x : -half_circle(x),
        lambda x : half_circle(x))


print("Half sphere: " , S3)
