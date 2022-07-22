'''
Write a Python function to insert a string in the middle of a string
'''
s1=("toop and coop are good")
s2=("copium")
s3=s1[:int(len(s1)/2)]+s2+s1[int(len(s1)/2):]
print(s3)
