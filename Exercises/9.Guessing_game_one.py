#Generate a random number between 1 and 9 (including 1 and 9). 
#Ask the user to guess the number, then tell them whether they guessed too low, 
#too high, or exactly right. 
# (Hint: remember to use the user input lessons from the very first exercise)

#Extras:

#Keep the game going until the user types “exit”
#Keep track of how many guesses the user has taken, and when the game ends, print this out.

import random

score = 0
while True: 
            score += 1
            b = int(input("Type the number between 1 and 10: "))
            a = random.randint(1,9)
            if b == a:
                print("Ok")
            if a > b:
                print("Your number is higher than mine")
            if a < b:
                print("Your number is smaller than mine")
       
            play_again = input("Do you want to play again, type 'exit', to quit: ")
            if play_again == "exit":
                break
print(score)


