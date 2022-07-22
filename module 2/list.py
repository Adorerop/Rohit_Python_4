'''
Write a Python function that takes a list of words and returns the length
of the longest one
'''
def length(l):
    l2=[]
    for i in l:
        s=str(i)
        l2.append(len(s))
    l2.sort()
    return l2.pop()
print("longest word's length is:",length(["afs","agsd","asssdfg","addsdfghjk","asadf"]))
