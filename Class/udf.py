'''
odd even
'''
def rohit(n):
    if n%2==0:
        print("Number is even")
    else:
        print("Number is odd")

def utsav(a,b):
    if a>b:
        print(a)
    else:
        print(b)
def dev(a,b,c):
    if a>b:
        if a>c:
            print(a)
        else:
            print(c)
    else:
        if b>c:
            print(b)
        else:
            print(c)

def mrudani(n):
    if n%2==0:
        print("The number is not prime")
    else:
        for i in range(3,int(n/2)+1,2):
            if n%i==0:
                print("The number is not prime")
                break
        else:
                print("The number is prime")


def dhruvi(n):
    for i in range(1,n+1):
        print(" "*((n+1)-i),"*"*i)


def priyal(n):
    for i in range (1,n+1):
        print(" "*(n+1-i)," *"*i)

def nishu(n):
    a,b=0,1
    print(a,end=" ")
    while b<n:
        print(b,end=" ")
        a,b=b,a+b

def rohitNanera(n):
    for i in range(n,0,-1):
        print("*"*i)

def haidar(n):
    for i in range(n,0,-1):
        print(" "*(n-i),"*"*i)

def axay(n):
    for i in range(n+1):
        for j in range(i+1):
            print("*" ,end="")
        print()

def raji(n):
    for i in range(n,0,-1):
        print(" "*(n-i)," *"*i)
    
        

def vedant(n):
    for j in range(n,0,-1):
        print(" "*(n-j),("* "*j))
    for i in range(1,n+1):
        print(" "*(n-i),("* "*i))

def dhruvish(n):
    for i in range(1,n+1):
        print(" "*(n-i), ("* "*i))
    for j in range(n,0,-1):
        print(" "*(n-j),("* " )*j)





        

        
                
