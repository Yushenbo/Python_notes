#-*- coding:utf-8 -*-
#########################################################################
# File Name: multiListener.py
# Author: Nichol.Shen
# mail: nichol_shen@yahoo.com
#########################################################################
#!/usr/bin/env python3

from traits.api import HasTraits, Str, Int, Instance, List, on_trait_change

class HasName(HasTraits):
    name = Str()

    def __str__(self):
        return "<%s %s>" %(self.__class__.__name__, self.name)

class Inner(HasName):
    x = Int
    y = Int

class Demo(HasName):
    x = Int
    y = Int

    z = Int(monitor = 1) # data property moinitor of Int

    inner = Inner()
    alist = List(Int)
    test1 = Str()
    test2 = Str()

    def __inner_default(self):
        return Inner(name = "inner1")

    @on_trait_change("x, y, inner.[x, y], test+, +monitor, alist[]")
    def event(self, obj, name, old, new):
        print(obj, name, old, new)


d = Demo(name = "demo")

d.x = 10 #x matched, x changed

d.y = 20 #y matched, y changed

d.inner.x = 1 #inner.[x, y] matched, x changed

d.inner.y = 2 #inner.[x, y] matched, y changed

d.inner = Inner(name = "inner2") # matched inner.[x, y] changed ? remain question

d.test1 = "ok" #test+ matched, test1 changed

d.test2 = "hello" #test+ matched, test2 changed

d.z = 30 #+monitor matched, z changed

d.alist = [3] #alist[] matched, alist changed
d.alist.extend([4, 5]) #alist[] matched, alist changed
d.alist[2] = 10  #alist[] matched, alist changed

