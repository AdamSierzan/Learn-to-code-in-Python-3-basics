import random

colors = ["blue", "black", "green", "yellow", "purple"]

while True:
    pickedColor = random.choice(colors)
    guess = input("Try to guess the color:")

    while True:
        if (guess == pickedColor()):
            break
        else:
            guess = input("Sorry try again: ")
    print("congratulations, you've guessed it, ",)
    play_again  = input("Let's play again, type 'no' to quit.")
    if play_again() == 'no':
        break


