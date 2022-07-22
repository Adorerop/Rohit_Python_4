'''Write a Python program to read an entire text file'''
file=open("a","w")
file.write("yoo hi there")
file.close()
file=open("a","r")
print(file.read())
file.close()