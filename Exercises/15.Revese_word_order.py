#Write a program (using functions!) that asks the user for a 
# long string containing multiple words. 
# Print back to the user the same string, 
# except with the words in backwards order. 
# For example, say I type the string:
mystring = "My name is Michele"
def backwards_order(any_string):
    splited_string = any_string.split()
    return splited_string[::-1]
print(backwards_order(mystring))


mystring = "My name is Michele"
def backwards_order(any_string):
    result = []
    y = any_string.split()
    for word in y:
        result.insert(0,word)
    return " ".join(result)
        
print(backwards_order(mystring))