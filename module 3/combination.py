'''Write a Python program to create and display all combinations of letters,
selecting each letter from a different key in a dictionary.
o Sample data: {'1': ['a','b'], '2': ['c','d']}
o Expected Output:
o ac ad bc bd'''
d={'1': ['a','b'], '2': ['c','d']}
l=list(d.values())
for i in l[0]:
    for j in l[1]:
        print(i+j,end=" ")