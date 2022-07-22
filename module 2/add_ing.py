'''
Write a Python program to add 'ing' at the end of a given string (length
should be at least 3). If the given string already ends with 'ing' then add 'ly'
insteadif the string length of the given string is less than 3, leave it
unchanged
'''
s=input("Enter a string :")
if len(s)<3:
    print(s)
else:
    if s.endswith("ing")==True:
        print(s+"ly")
    else:
        print(s+"ing")