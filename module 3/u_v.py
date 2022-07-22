'''Write a Python program to print all unique values in a dictionary'''
d={1:4,2:5,5:5,6:10,65:4}
l=[]
for i in d.values():
    if i not in  l:
        l.append(i)
print(tuple(l))