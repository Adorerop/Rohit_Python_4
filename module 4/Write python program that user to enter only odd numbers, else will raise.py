try:
    ex=1   
    n=int(input("a="))
    if n%2==0:
        print("ok")
    else:
        ex-=1
    if ex==0:
        n=n/ex
except:
    print("only even numbers are allowed")
