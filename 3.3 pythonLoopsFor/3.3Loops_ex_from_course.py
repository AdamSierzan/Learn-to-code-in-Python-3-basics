import random
x = 0
people = []
while x < 7 :
    person = input("Type the first name:")
    people.append(person)
    x += 1
index = random.randint(0,7) #to get the random number
random_person  = people[index]
print("Picking a random person:" random_person)
# print(-----------)

# people = []
# for name in people: