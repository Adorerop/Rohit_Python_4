'''
Write a Python program that will return true ifthe two given integervalues
are equal or their sum or difference is 5
'''
a,b=int(input("Enter a number:")),int(input("Enter a number:"))
print(a==b or a+b==5 or a-b==5 or b-a==5)
