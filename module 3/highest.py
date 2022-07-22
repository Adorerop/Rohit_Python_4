'''Write a Python program to find the highest 3 values in a dictionary'''
d={1:4,4:6,41:54,5:1,4:45}
l=list(d.values())
l.sort()
l.reverse()
print(l[:3])