'''
Write a Python program to sum of three given integers.However, if two
values are equal sum will be zero
'''
a,b,c=int(input("Enter A number:")),int(input("Enter A number:")),int(input("Enter A number:"))
sum=0
if a==b or b==c or a==c:
    print("sum of three integers:",sum)
else:
    sum=a+b+c
    print("sum of three integers:",sum)
