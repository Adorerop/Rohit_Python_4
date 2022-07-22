''' Write a Python program to calculate surface volume and area of a cylinder'''
from math import *
def cyli(r,h):
    volume=pi*r**2*h
    return volume

print(cyli(10,5),"cm^3")