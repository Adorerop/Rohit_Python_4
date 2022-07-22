'''Write a Python program to returns sum of all divisors of a number'''
def div(n):
    l=[1]
    for i in range(2,int(n/2)+2):
        if n%i==0:
            l.append(i)
    l.append(n)
    return l
print(div(5000))