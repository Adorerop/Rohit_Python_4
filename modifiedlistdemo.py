from _collections import deque

l=deque([])

n=int(input("how much you want the size of list:"))
for i in range(1,n+1):
    l.append(input(i))
    print(list(l))
    
print("Now popout of list:")
for i in range(-n,0):
    l.popleft()
    print(list(l))
