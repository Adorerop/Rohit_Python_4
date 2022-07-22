#Find factorial of given number

n=int(input("Enter a number : "))
fact=1
for i in range(n,0,-1):
    fact=fact*i
print("Fact= ",fact)
    
