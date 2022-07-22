'''Write a Python script to check if a given key already exists in a dictionary'''
d={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
n=int(input())
if d.get(n)!=None:
    print("key exists in a dictionary")
else:
    print("Key does not exist")
