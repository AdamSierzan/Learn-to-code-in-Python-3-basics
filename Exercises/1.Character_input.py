print("Hi this programe will tell you, when you'll reach 100 years, please enter your age:")

age = int(input("Your age: "))

name = input("Your name: ")

reaching_100 = 100

x  = reaching_100 - age


for i in range(x):
    print("\n")
    print(name, "you'll reach the age of 100 in year: ", (x + 2020),)

