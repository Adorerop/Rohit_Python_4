'''
Write a Python program to find the first appearance of the substring 'not'
and 'poor' froma given string, if 'not' follows the 'poor', replace the whole
'not'...'poor'substring with 'good'. Return the resulting string
'''
s=("i am not a god, i am not a king , i am poor  ooooooooooooo")
print(s.find("not"))
print(s.find("poor"))
if s.find("not")<s.find("poor"):
    print(s.replace(s[s.find("not"):(s.find("poor")+4)],"good"))
