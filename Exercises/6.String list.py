#Ask the user for a string and print out whether this string is a palindrome or not. 
# (A palindrome is a string that reads the same forwards and backwards.)

x = str(input("Please type a sentence here: "))
print(x)
if (x[0:]) == (x[::-1]):
    print("your string is palindrome")
else:
    print("your string isn't a palindrome")

