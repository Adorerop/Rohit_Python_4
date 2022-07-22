'''
Write a Python program to count the number of characters (character
frequency) in a string
'''
#for every char 
s=("asdfghj kjhggds")
d={}
for n in s:
    keys = d.keys()
    if n in keys:
        d[n] += 1
    else:
        d[n] = 1
print(d)
#for one char
print("frequency of char h=",s.count("h"))
