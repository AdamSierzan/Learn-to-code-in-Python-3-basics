male_names = ["Adam", "Tom", "Jack"]
female_names = ["Jackie", "Jenny", "Mary"]
name = input("Type your name: ")
if name in male_names:
    print("Seems like we have your name on the list.")
elif name in female_names:
    print("Seems like we have your name on the list :)")
else:
    print("Sorry, we dont have your name on the list")
    x = input("Do you want to add it to the list, type 'yes' or 'no': ")
    if x == "yes": 
        y = input("Is that a male name? If it is type 'yes': ")
        if y == "yes":
            male_names.append(name)
        else:
            female_names.append(name)``
    if x != "yes":
        print("Ok, that,s cool")
print(male_names)
print(female_names)