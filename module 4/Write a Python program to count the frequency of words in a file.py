file=open("ap","w")
file.write("yoo hi there")
file.close()
file=open("ap","r+")
file.write("llkkl lllkkkjjkffsd sdjhfbsjhfbj shgdvfhsgvf")
file.seek(0)
s=(file.read())
file.close()
print(s)
d={}
word=s
for n in word:
    keys = d.keys()
    if n in keys:
        d[n] += 1
    else:
        d[n] = 1
print(d)