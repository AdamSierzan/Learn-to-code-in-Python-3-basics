#create a game to guess the color 
import random
colors = ["black", "green", "yellow", "brown"]

while True:
    color = colors[random.randint(0,len(colors)-1)]
    guess = input("Try to guess the color: ")
    
    while True:
        if (color == guess.lower()):
            break
        else: 
            guess = input("Nope, try again: ")
    print("You've guessed it")
    play_again = input("Do you want to play again, type 'no' to guit: ")
    if play_again == 'no':
        break
print("it was fun bye")