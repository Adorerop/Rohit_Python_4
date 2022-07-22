'''Write a Python program to convert a list of tuples into a dictionary'''
l=[('ll','kk'),(40,50),('oo','pp')]
d={}
n=1
for i in l:
    d[n]=list(i)
    n+=1
print(d)