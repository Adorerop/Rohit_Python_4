import random
file=open("Random","w")
file.close()
file=open("Random","r+")
file.write('''perfect number, a positive integer that is equal to the 
sum of its proper divisors. The s
mallest perfect number is 6, which is the sum of 1, 2, and 3. Other perfect numb
ers are 28, 496, and 8,128. The discovery of such numbers is lost in prehist
ory. It is known, however, that the Pythagoreans (founded c. 525 BCE
) studied perfect numbers for their “mystical” properties.''')
file.write("i am a god\ngg")
file.seek(0)
s=(file.read())
file.close()
i=list(s.split("\n"))
n=random.randint(0,len(i))
print(i[n])