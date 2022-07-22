'''Write a Python function to calculate the factorial of a number (a nonnegative integer)'''
def fact(n):
    if n==0:
        return 1
    elif n<0:
        print("nonnegative integer")
    else:
        return n*fact(n-1)
print(fact(5))