'''
Write a Python program to get a string made of the first 2 and the last 2
chars from a given a string. Ifthe string length islessthan 2,return instead
of the empty string.
o Sample String:w3resource'
o Expected Result: 'w3ce'
o Sample String: 'w3'
o Expected Result: 'w3w3'
o Sample String: ' w'
o Expected Result: Empty String
'''
s=input("Enter a string: ")
if len(s)>=2:
    s1=s[0:2]+s[len(s)-2:len(s)]

    print(s1)
