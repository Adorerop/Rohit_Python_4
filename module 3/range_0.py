'''Write a Python function to check whether a number is in a given range
'''
def rang(a,b,n):
    return a<n<b
n=int(input("Enter a number :"))
print(rang(1,100,n))