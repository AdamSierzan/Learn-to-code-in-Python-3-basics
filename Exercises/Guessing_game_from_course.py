import random
print("WELCOME TO GUESS ME!")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")

count = 0
rounds = 0
shots = []
the_number_to_guess = random.randint(1,101)

while count == 0:
    
    the_number_to_guess = random.randint(1,101)
    players_guess = int(input("Type your number: "))
    shots.append(players_guess)
    
    if players_guess > 100 or players_guess < 1:
        print("Out of band")
    elif the_number_to_guess - players_guess <= 10:
        print("Warm")
    elif the_number_to_guess - players_guess >= 10:
        print("Cold")
    elif players_guess == the_number_to_guess:
        print("You've guessed it")
        break
    else:
        print("Sorry not this time")
        break
    count+=1
    rounds+=1
while count == 1:
    
    the_number_to_guess = random.randint(1,101)
    players_guess = int(input("Type your number: "))
    shots.append(players_guess)
    
    if players_guess > 100 or players_guess < 1:
        print("Out of band")
    elif the_number_to_guess - players_guess < the_number_to_guess - shots[-1]:
        print("warmer")
    elif the_number_to_guess - players_guess > the_number_to_guess - shots[-1]:
        print("colder")
    elif players_guess == the_number_to_guess:
        print("You've guessed it")
    else:
        print("Sorry not this time")