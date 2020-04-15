#Write a Python program which iterates the integers from 1 to 50. For multiples of three print "Fizz" 
# instead of the number and for the multiples of five print "Buzz". 
# For numbers which are multiples of both three and five print "FizzBuzz".
#Sample Output :
#fizzbuzz
#1
#2
#fizz
#4
#buzz


a = list(range(1,50))
for x in a:
    if x%5 == 0:
        print("fizz")
    elif x%3 == 0:
        print("buzz")
    elif x%5 == 0 and x%3 == 0:
        print("fizz & buzz")
    else:
        print(x)
        