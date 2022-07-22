d={1:"Rohit",2:"Haidar",3:"Akshay",4:"Manthan",5:"Rohit",6:"Dhruvish"}

print(d)
#d.clear()
#print(d)
d1=d.copy()
print(d1)
print(d.get(3))
print(d[5])
t=list(d.items())
print(t[0][1])
print(d.keys())
print(d.values())
print(d.pop(2))
print(d.popitem())
d2={7:"Bipin",8:"Vedant",9:"Dev",10:"Dev",11:"Utsav"}
d.update(d2)
print(d)
d[12]="Raji"
print(d)

for i in d:
    print(i," : ",d[i])
