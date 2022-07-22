'''Write a Python script to concatenate following dictionaries to create a
new one'''
d={1:10,2:20,3:30,4:40}
d2={5:50,6:60}
d.update(d2)
print(d)