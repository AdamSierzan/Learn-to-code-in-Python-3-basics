a = int(input("Type the number so the program will tell you the list of divisors of that number: "))

divisors = []
list_range = list(range(1, a+1))
x = 1
#a % x = 0

for i in list_range:
    if a % i  == 0:
        divisors.append(i)
print(divisors)




    


    