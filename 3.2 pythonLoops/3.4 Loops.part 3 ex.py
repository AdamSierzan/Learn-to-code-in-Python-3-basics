#Now we can make our game even cooler by picking a random number we can use the random module for that.
#So before starting the program let's import the random module now the number is going to be random.
import random 
number = random.randint(0,10)
guess = int(input("Try to guess the number between 0 and 10: ")) 
while True:
    if guess == number:
        break
    else:
        guess = int(input("nope, try again: ")) #it's here so he can guess again
print("You guessed it. I was thinking about:", number)
