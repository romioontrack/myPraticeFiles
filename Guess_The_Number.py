# To Guess the number to write the programm to get the exect number

import random

target = random.randint(1,100)

while True:
    userChoice = input("Guess a number or Quit(Q) ")
    if(userChoice== "Q"):
        break
    userChoice= int(userChoice)
    if(userChoice == target):
        print("Success : Correct Guess ")
        break
    
    elif( userChoice < target):
        print("The Guess was too small ! Guess the big number :")
        
    else:
        print("The Guess was too big Number ! Guess the small number :")
        
print("---------------Game  Over ------------------------------------")