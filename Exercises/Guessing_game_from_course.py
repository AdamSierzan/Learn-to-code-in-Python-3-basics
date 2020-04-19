import random
print("WELCOME TO GUESS ME!")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")

shots = [0]
the_number_to_guess = random.randint(1,101)

while True:
    
    players_guess = int(input("Type your number: "))
    print(the_number_to_guess)
    
    if players_guess > 100 or players_guess < 1:
        print("Out of band")
        continue
   
    if players_guess == the_number_to_guess:
        print("You've guessed it in only", len(shots), "guesses")
        break    
      
    shots.append(players_guess)
  
    if shots[-2]:
        if abs(the_number_to_guess) - abs(players_guess) < abs(the_number_to_guess) - abs(shots[-2]):
            print("warmer")
        else: 
            print("colder")
   
    else:    
        if the_number_to_guess - players_guess <= 10:
            print("Warm")
        else:
            print("Cold")
    
