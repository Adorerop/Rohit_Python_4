'''Write a Python function to check whether a number is perfect or not'''
def perfact(n):
    l=[1]
    for i in range(2,int(n/2)+2):
        if n%i==0:
            l.append(i)
    sum =0
    for i in l:
        sum+=i
    if n==sum:
        print(True)
    else:
        print(False)
perfact(8128)