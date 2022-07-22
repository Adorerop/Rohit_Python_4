'''Write a Python function that checks whether a passed string is palindrome
or not'''
from re import S


def palindrome(s):
    s1=s[::-1]
    if s==s1:
        print(True)
    else:
        print(False)
palindrome("lmao")