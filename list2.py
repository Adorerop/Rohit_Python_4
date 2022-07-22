l=[]

for i in range(1000,3001):
    s=str(i)
    if int(s[0])%2==0 and int(s[1])%2==0 and int(s[2])%2==0 and int(s[3])%2==0:
    #if int(i/1000)%2==0 and int(i/100)%2==0  and int(i/10)%2==0 and i%2==0:
        l.append(i)

print(l)
    
    
