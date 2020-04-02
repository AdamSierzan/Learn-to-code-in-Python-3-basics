age = int(input("Enter your age:"))

if age < 18:
    print("User is under 18, he will be 18 in:", 18- age, "year")
elif age >= 18 and age < 100:
    print("User is 18 or over 18")
elif age > 100:
    print("I wish you 200 years!")
