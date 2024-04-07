#import
import random

#choose a computer number
computer_number=random.randint(1, 100)

#make a function of is_same
def is_same(target, user_number):
    if target == user_number:
        result="Win"
    elif target > user_number:
        result="Low"
    else:
        result="High"
    return result

#start the game
print("Hello.\nStart the game. I am choosing a number between 1 and 100.")

#User is choosing a number
guess=int(input("pick up a number\n"))

#call the is_same() function
high_or_low=is_same(computer_number, guess)

#continuing the game until the user wins
while high_or_low != "Win":
    if high_or_low == "Low":
        guess=int(input("The target number is greater than your number. choose a number one more again\n"))
    else:
        guess=int(input("The target number is less than your number. choose a number one more again\n"))
    high_or_low=is_same(computer_number, guess)

#game over
input("You win!!\n\n press the enter button if you finish!!")




    
