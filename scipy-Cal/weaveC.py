#-*- coding:utf-8 -*-
#########################################################################
# File Name: weaveC.py
# Author: Nichol.Shen
# mail: nichol_shen@yahoo.com
#########################################################################
#!/usr/bin/env python3

import scipy.weave as weave
import numpy as np
import time

def my_sum(a):
    n = int(len(a))
    code = """
    int i;

    double counter = 0;

    for (i = 0; i < n; i ++)
        couter += a[i];

    return_val = counter;
    """

    err = weave.inline(
            code, ['a', 'n'],
            type_converters = weave.converters.blitz,
            compiler="gcc"
            )

    return err

a = np.arange(0, 10000000, 1.0)

my_sum(a)

start = time.clock()
for i in xrange(100):
    my_sum(a)

print("my_sum: ", (time.clock() - start)/100.0)

start = time.clock
print(sum(a))
print("sum(): ", time.clock() - start)
