'''Write a Python program to find the repeated items of a tuple'''
t=(1,2,1.1,2.2,True,"tops",10,1,"python",100,False,"python","python")
l2=[]
n=0
for i in t:
    
    if i not in l2:
       l2.append(i)
    else:
        print(i,"at -",n)
    n+=1