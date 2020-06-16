#Write a password generator in Python. Be creative with how you generate passwords - 
# strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. 
# The passwords should be random, generating a new password every time the 
# user asks for a new password. Include your run-time code in a main method.
#Extra:
#Ask the user how strong they want their password to be. 
# For weak passwords, pick a word or two from a list.
import random
import string
print("Hi, this programme will generate a password for you")
def password_gen():
    
    strength = input("For strong password type '''strong''', for easier password type '''easy'''")

    while strength == "easy":
        password = ""
        numbers = "12345678910"
    
        password += random.choice(numbers)
        password += random.choice(string.ascii_lowercase)
        password += random.choice(string.ascii_uppercase)
        password += random.choice(string.ascii_lowercase)
        password += random.choice(string.ascii_uppercase)
        return password
        


    while strength == "strong":
    
        password = ""
        numbers = "12345678910"

        password += random.choice(numbers)
        password += random.choice(string.ascii_lowercase)
        password += random.choice(string.ascii_uppercase)
        password += random.choice(string.ascii_lowercase)
        password += random.choice(string.punctuation)
        password += random.choice(string.punctuation)
        password += random.choice(string.ascii_lowercase)
        password += random.choice(string.ascii_uppercase)
        return  password    
        

print(password_gen())