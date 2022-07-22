'''
Write a python program to sum of the first n positive integers
'''
n=int(input("enter a number:"))
sum=0

while n>0:
    sum=sum+n
    n-=1
print(sum)
