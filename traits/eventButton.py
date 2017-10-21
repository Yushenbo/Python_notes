#-*- coding:utf-8 -*-
#########################################################################
# File Name: eventButton.py
# Author: Nichol.Shen
# mail: nichol_shen@yahoo.com
#########################################################################
#!/usr/bin/env python3

from traits.api import HasTraits, Float, Event, on_trait_change

class Point(HasTraits):
    x = Float(0.0)
    y = Float(0.0)
    updated = Event

    @on_trait_change("x, y")
    def pos_changed(self):
        self.updated = True

    def _updated_fired(self):
        self.redraw()

    def redraw(self):
        print("redraw at %s, %s"%(self.x, self.y))


def main():
    p = Point()
    p.x = 1
    p.y = 1 # 
    p.x = 1 # p.x has been assigned value so, it's can't be triggered

    p.updated = True
    p.updated = 0 # updated assigned will trigger Event


main()
