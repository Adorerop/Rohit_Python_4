'''
Write a Python program to remove duplicates from a list.
'''
l=[1,2,1.1,2.2,True,"tops",10,1,"python",100,False,"python","python"]
l2=[]
for i in l:
    if i not in l2:
       l2.append(i)
print(l2)