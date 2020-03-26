import random
people = []
for name in range(0,8):
    name = input("Please type the name:")
    people.append(name)
index = random.randint(0,7)
random_person = people[index]
print("Picking a random person:", random_person)