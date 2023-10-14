# -*- coding: utf-8 -*-
#クロージャ

def cicle_area_func(pi):
    def circle_area(radius):
        return pi * radius * radius
    return circle_area

ca1 = cicle_area_func(3.14)
ca2 = cicle_area_func(3.141592)

print(ca1(10))
print(ca2(10))
"""
314.0
314.1592
"""
