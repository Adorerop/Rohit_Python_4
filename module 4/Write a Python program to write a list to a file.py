l=["1","2","3","4","5","6","7","8","9"]
file=open("ap","w")
file.write(" ")
file.close()
file=open("ap","r+")
for i in l:
    file.write(i)

file.seek(0)
print(list(file.read()))
file.close()