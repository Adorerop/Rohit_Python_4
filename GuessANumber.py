import random

num=random.randint(1,20)

while True:

    guess=int(input("Guess A Number Between 1 to 20:"))
    if guess==num:
        print("Correct Number")
        break
    elif guess>num:
        print("You Guessed A Greater Number")
    elif guess<num:
        print("You Gussed A Smaller Number")
