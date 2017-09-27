#-*- coding:utf-8 -*-
#########################################################################
# File Name: traitsProperty.py
# Author: Nichol.Shen
# mail: nichol_shen@yahoo.com
#########################################################################
#!/usr/bin/env python3

from traits.api import HasTraits, Float, Property, cached_property

class Rectangle(HasTraits):
    width = Float(1.0)
    height = Float(2.0)

#area is a property, the associated funciton _get_area will be called when
# the width or height value changed
    area = Property(depends_on=['width', 'height'])

# The democrator of cached_property cache the ouput of _get_area()

    @cached_property
    def _get_area(self):
        print('Recalculating....')
        return self.width * self.height


r = Rectangle()

print('the original area is: ', r.area) # first time get the area

print('Nothing here')

r.width = 10
print(r.width)

print('Modify the width to 10: ' , r.area) 

print('No modification: ' , r.area) 

r.height = 4

print(r.area)

