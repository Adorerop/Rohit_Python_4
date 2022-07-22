'''
Write a Python program to count the number of strings where the string
length is 2 or more and the first and last character are same from a given
list of strings
'''
l=["kljik","koiutrfg54k","m","tv","pop"]
count=0
for i in l:
    if len(i)>=2 and i[:1]==i[-1:]:
        count+=1
print("count of this strings :",count)