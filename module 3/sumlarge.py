'''
Write a Python function to get the largest number, smallest num and sum
of all from a list
'''
l=[1,2,3,4,5,6,3,4,2,5,3,4,2,5]
l.sort()
sum=0
for i in l:
    sum=sum+i
l1=l.copy()
print("sum of all numbers=",sum)
print("smallest number is :",l[0])
print("largest number is:",l1.pop())