import math
print("Hi, this programme will let you calculate the area and circumference of a circle")
r = float(input("Plase type the radius: "))
area  = 3.14 * r ** 2
circumference  = 2 * 3.14 * r 
print("The area of the circle with radius:", r, "is", round(area,3),) 
print(", the circumference of a circle with this radius is:", round(circumference, 1))