'''Write a Python function that takes a list and returns a new list with unique
elements of the first list'''
def uniqe(l):
    l2=[]
    for i in l:
        if i not in l2:
            l2.append(i)
    return l2
print(uniqe([1,0,5,5,6,54,5,6,45,5,1,5,0,5,6,5,44,5,0,5]))