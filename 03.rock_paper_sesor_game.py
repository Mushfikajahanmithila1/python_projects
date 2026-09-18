"""
rock = 1
paper = 0
sesior = -1

"""
import random
yourchoice = input("Enter your choice: ")
comchoice = random.choice([1, 0, -1])
yourdic = {"r": 1, "p":0, "s": -1}
you = yourdic[yourchoice]
reverdic = {1:"r", 0:"p", -1:"s"}

print(f"Your choice: {reverdic[you]}\nComputer choice: {reverdic[comchoice]}")

if comchoice == you:
    print("It's a tie!")

else:
    if(comchoice == 1 and you == 0):
        print("You win!")
    elif(comchoice == 1 and you == -1):
        print("You lose!")
    elif(comchoice == 0 and you == 1):
        print("You lose!")
    elif(comchoice == 0 and you == -1):
        print("You win!")
    elif(comchoice == -1 and you == 1):
        print("You win!")
    elif(comchoice == -1 and you == 0):
        print("You lose!")
    else:
        print("Something went wrong.")


