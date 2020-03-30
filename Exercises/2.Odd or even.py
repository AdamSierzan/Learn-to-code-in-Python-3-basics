print("This program will tell you, wheter the number you'll choose is even or odd")

num = int(input("Type your number to check: "))
check = int(input("Type the second number to divide by: "))

if num % 2 == 0:
    print("the number you typed is even")
    if num % 4 == 0:
        print("Seems like the number given by you, is also a multiple of 4!")
else:
    print("The number you typed is  odd")


if num % check  == 0:
        print("the number you typed is even")
else:
    print(num, "does not divides evenly by", check)