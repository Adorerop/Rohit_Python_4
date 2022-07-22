'''Write a Python program to combine two dictionary adding values for
common keys.
o d1 = {'a': 100, 'b': 200, 'c':300}
o d2 = {'a': 300, 'b': 200,'d':400}
'''
from collections import Counter
d1 = {'a': 100, 'b': 200, 'c':500}
d2 = {'a': 300, 'b': 200, 'd':400}
dict = Counter(d2) + Counter(d1)
print(dict)