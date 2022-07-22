'''Write a Python program to create a dictionary from a string.
o Note: Track the count of the letters from the string. Sample string:
'w3resource'
o Expected output: {'3': 1,'s': 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}'''
s=('w3resource')
d={}
for n in s:
    keys = d.keys()
    if n in keys:
        d[n] += 1
    else:
        d[n] = 1
print(d)