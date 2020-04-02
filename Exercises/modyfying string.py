sentence = "Python course is nice and easy"
print(len(sentence))
print(sentence[16:20])
print(sentence[7])
print(sentence[-4])
sentence = sentence[0] + 'a' + sentence[2:3] + 'd' + sentence[3:]

print(sentence)


print('-----------------------')

name  = input("Enter your name: ")
last_name = input("Enter your last name: ")
phone_num  = input("Enter your phone numb: ")

print()
print(name.isalpha())
print(last_name.isalpha())
print(phone_num.isdigit())

print()
print(name.capitalize())
print(last_name.capitalize())
print()

print(phone_num.replace("-", "").replace("-", ""))

print(name.endswith("a"))
personal  = name + " " + last_name + "" + phone_num
print(personal)
print(len(personal))

letters = len(personal) - personal.count(" ")
