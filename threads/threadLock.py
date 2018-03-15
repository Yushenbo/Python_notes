#-*- coding:utf-8 -*-
#########################################################################
# File Name: threadLock.py
# Author: Shen Bo
# Created Time: Wed, Mar 14, 2018  2:47:25 PM
#########################################################################
#!usr/bin/env python

import threading, time

class Seeker(threading.Thread):
    def __init__(self, cond, name):
        threading.Thread.__init__(self)
        self.cond = cond
        self.name = name

    def run(self):
        time.sleep(1)

        self.cond.acquire()
        print('Step0-PepaPig: Eyes closed already...')
        self.cond.notify()
        self.cond.wait()

        time.sleep(4)
        print('Step2-PepaPig: I found you!!!')
        self.cond.notify()
        self.cond.wait()

        time.sleep(2)
        self.cond.release()
        print('Step4-PepaPig: I am Winner!!hah~')

class Hider(threading.Thread):
    def __init__(self, cond, name):
        threading.Thread.__init__(self)
        self.cond = cond
        self.name = name

    def run(self):
        self.cond.acquire()
        self.cond.wait()

        time.sleep(2)
        print('Step1-LucyGoat: I have already hidden!!!')
        self.cond.notify()
        self.cond.wait()


        time.sleep(2)
        self.cond.notify()
        self.cond.release()
        print('Step3-LucyGoat: You found me, damn it!!!')


def main():
    cond = threading.Condition()
    seeker = Seeker(cond, 'seeker')
    hider = Hider(cond, 'hider')

    seeker.start()
    hider.start()


if __name__ == '__main__':
    main()
