#napisz program z funckją, który:
#zapyta użytk. o pierwszą i druga liczbę
#wydrukuje użytkownikowi "tak", lub "nie" w zależnośći od tego czy suma jego liczb jest podzielna przez 3
#*Validation of data

data_valid = False

while data_valid == False: 
    number1 = input
    try: 
        number1 = float(input("Please type first number: "))
        data_valid == True
    except: 
            print("Invalid data")
            continue
    else: 
        break
    
data_valid = False

while data_valid == False: 
    number2 = input
    try: 
        number2 = float(input("Please type second number: "))
        data_valid == True
    except: 
            print("Invalid data")
            continue
    else: 
        break


def dividedBYthree(a, b):
    if (a + b) % 3 == 0:
        return True
    else:
        return False
if dividedBYthree(number1, number2) == True:
    print("The sum of", int(number1), "and", int(number2), "=", int(number1 + number2),  "and can be divided by 3")
else:
    print("Sorry, the sum of", number1, "and", number2, "=", int(number1 + number2), "and can't be devided by 3")
