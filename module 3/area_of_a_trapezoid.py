'''Write a Python program to calculate the area of a trapezoid'''
def at(a,b,h):
    area=((a+b)/2)*h
    return area
a=int(input("Enter a in cm :"))
b=int(input("Enter b in cm :"))
h=int(input("Enter h in cm :"))
print(at(a,b,h),"cm")