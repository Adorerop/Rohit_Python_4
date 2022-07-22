l=[1,2,1.1,2.2,True,"tops",10,[10,20,30],1,"python",100,False]

print(l[7])
l[7].append(40)
print(l)


print(len(l))
l.append("Java")
print(l)
#l.clear()
#print(l)
l1=l.copy()
print(l1)
l.append(1000)
print(l1)
print(l)
l2=l
print(l2)
l2.append(2000)
print(l)
print(l2)
print(l.count(0))
l3=[11,22,33]
l.extend(l3)
print(l)
print(l.index(10))
l.insert(7,"Data")
print(l)
l.pop()
print(l)
l.pop(10)
print(l)
l.remove(10)
print(l)
l.reverse()
print(l)

for i in l:
    print(i)
