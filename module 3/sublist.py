'''Write a Python program to check whether a list contains a sub list'''
l1=[1,5,4,5,6]
l2=[5,99]

if l2==[]:
    print(True)
elif l2==l1:
    print(True)
elif len(l2)>len(l1):
    print(False)
else:
    for i in range(len(l1)):
        if l1[i]==l2[0]:
            n=1
            while (n < len(l2)) and (l1[i+n] == l2[n]):
                n += 1
            if n == len(l2):			
            	print(True)
    else:
        print(False)