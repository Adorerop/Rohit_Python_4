import random

l=[]
lucky=[]
#print(random.randint(1000,9999))
#print(random.choice([1,2,10,"tops",1.1,"python",True]))
for i in range(1,101):
    l.append(i)

for i in range(10):
    num=random.choice(l)
    l.remove(num)
    lucky.append(num)

print(l)
print(lucky)
