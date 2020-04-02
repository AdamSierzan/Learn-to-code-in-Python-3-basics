a = 8
b = 2
c = 5
if a > b and a > c :
    maximum = a
elif b > a and b > c:
    maximum = b
else:
    maximum = c

if a < b and a < c :
    minimum = a
elif b < a and b < c:
    minimum = b
else:
    minimum = c

number = [a, b, c]
print(number.sort())
print(number[0], number[1], number[2], sep=", ")