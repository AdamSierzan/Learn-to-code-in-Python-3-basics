# creat a list of 6 people  adn then print a random name
import random
people = []
x = 0
while x < 7:
    name = input("Please enter the first name:")
    people.append(name)
    x += 1
print(random.choice(people))
    
    