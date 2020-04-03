names = {
"Adam" : "male", 
"Tom" : "male", 
"Jack" : "male", 
"Tim" : "male", 
"Jenny" : "female", 
"Mary" : "female",
"Tina" : "female", 
"Juliet" : "female"
}

name = input("Type your name: ")
if (name) in (names.keys()):
    print("Seems like we have your name on the list.")
    print("And its a: ", names[name], "name")
else:
    print("Sorry, we dont have your name on the list")
    x = input("Do you want to add it to the list, type 'yes' or 'no': ")
    if x == "yes": 
        y = input("Is that a male name? If it is type 'yes': ")
        if y == "yes":
            names[name] = "male"
        else:
            names[name] = "female"
    if x != "yes":
        print("Ok, that,s cool")
print(names)