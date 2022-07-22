'''
Write a Python program to count the occurrences of each word in a given
sentence
'''
s=('''a boy got killed and eaten by a lion, then lion attacked her one person no one was allowed to even touch,
then hero killed the lion like it was nothing but a mare animale''')
d={}
word=s.split(" ")
for n in word:
    keys = d.keys()
    if n in keys:
        d[n] += 1
    else:
        d[n] = 1
print(d)

