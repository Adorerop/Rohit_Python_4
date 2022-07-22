#Fibonacci Series
a,b=0,1
n=int(input("Enter number till you need fibonacci series: "))
while b<n:
    print(a,end=" ")
    a,b=b,a+b
