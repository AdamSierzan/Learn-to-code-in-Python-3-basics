print("Hi, this programme takes a list and prints out the elements that are less than your number")
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new_list = []
b = int(input("Type the number, to find out which elements from the list are smaller than your number: "))
for element in a:
    if element < b:
        new_list.append(element)
print(new_list)
        