#-*- coding:utf-8 -*-
#########################################################################
# File Name: demo1.py
# Author: Shen Bo
# mail: Bo.A.Shen@alcatel-sbell.com.cn
# Created Time: Wed, Mar 14, 2018  9:40:25 AM
#########################################################################
#!usr/bin/env python

import time, threading

def testa():
    time.sleep(1)
    print('a')

def testb():
    time.sleep(1)
    print('b')


def main():
#    testa()
#    testb()
    ta = threading.Thread(target=testa)
    tb = threading.Thread(target=testb)
    for t in [ta, tb]:
        t.start()
    for t in [ta, tb]:
        t.join()

    print('DONE')


if __name__ == '__main__':
    main()
