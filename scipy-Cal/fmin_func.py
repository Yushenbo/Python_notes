#-*- coding:utf-8 -*-
#########################################################################
# File Name: fmin_func.py
# Author: Nichol.Shen
# mail: nichol_shen@yahoo.com
#########################################################################
#!/usr/bin/env python3

import scipy.optimize as opt
import numpy as np

def test_fmin_convolve(fminfunc, x, h, y, yn, x0):
    """
    x (*) h = y (*) 表示卷积
    yn为在y基础上的添加的一下干扰噪声结果
    x0为求解x的初始值
    """
    def convolve_func(h):
        """
        计算 yn - x (*) h 的power
        fmin将通过计算使得power最小
        """
        return np.sum((yn - np.convolve(x, h) ** 2))

    #call the fmin funciton by the default value x0
    h0 = fminfunc(convolve_func, x0)

    print(fminfunc.__name__)
    print("-----------------------")

    #the error of output x (*) h0 and y
    print("error of y:", np.sum((np.convolve(x, h0) - y) ** 2)/np.sum(y ** 2))
    #error of output h0 & h 
    print("error of h:", np.sum((h0 - h) ** 2)/np.sum(h ** 2))
    print("\n")

def test_n(m, n, nscale):
    """
    随机产生x h yn x0等数列， 调用各种fmin函数求解b
    m为x的长度， n为h的长度， nscale为干扰度
    """
    x = np.random.rand(m)
    h = np.random.rand(n)
    y = np.convolve(x, h)
    yn = y + np.random.rand(len(y)) * nscale
    x0 = np.random.rand(n)


    test_fmin_convolve(opt.fmin, x, h, y, yn, x0)
    test_fmin_convolve(opt.fmin_powell, x, h, y, yn, x0)
    test_fmin_convolve(opt.fmin_cg, x, h, y, yn, x0)
    test_fmin_convolve(opt.fmin_bfgs, x, h, y, yn, x0)

if __name__ == "__main__":
    test_n(200, 20, 0.1)

