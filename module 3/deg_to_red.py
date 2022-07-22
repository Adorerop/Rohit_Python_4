'''Write a Python program to convert degree to radian'''
from math import *
d=int(input("d:"))
print(radians(d))

def dtr(d):
    r=d*(pi/180)
    return r
print(dtr(d))