number1 = float(input("Please type the first number:"))
number2 = float(input("Please type the second number:"))

def isDevided(a, b):
    if (a + b) % 3 == 0:
        return True
    else:
        return False

if (isDevided(number1, number2) == True):
    print("Tak")
else:
    print("Nie")



  

