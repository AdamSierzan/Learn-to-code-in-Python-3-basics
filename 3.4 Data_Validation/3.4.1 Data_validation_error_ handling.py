#In this lesson we will learn how to do error handling in Python.
#Every time we work with user input we should make sure not only the data is valid and within the range
#we want which is what we did in the previous lesson but also we need to make sure a bad input is not
#going to cause our program to crash in order to do that.
#We are going to use the "try and accept" statements so let's understand why our program crashed let's
# why our programe crash

#   number = float(input("type a number: ")) #when we type a string out program crashes


# to prevent from crashing we can use "try" block which works the same way as the conditional statement

number = input("type a number: ")
try: 
    number = float(number)
    print("The number is:", number) #if we see this msg it means we did the conversion
except: 
    print("Invalid number")