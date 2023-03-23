import random


com = random.randint(0, 100)

us = int(input("Please Enter Number that should lie in the range of 1 to 100:\n"))

if(com == us):
    print("You guessed the right number!!!\n")
else:
    while com != us:
        if(com > us):
            us = int(input("The number is lower than the answer\n"))
        elif(com < us):
            us = int(input("The number is higher than the answer\n"))


print("You guessed the right number!!!\n")
