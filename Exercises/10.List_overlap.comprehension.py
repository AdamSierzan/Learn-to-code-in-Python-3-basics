#and write a program that returns a list that contains only the 
# #elements that are common between the lists (without duplicates). 
# #Make sure your program works on two lists of different sizes. 
# #Write this in one line of Python using at least one list comprehension. 
# #(Hint: Remember list comprehensions from Exercise 7).
import random
list1 = random.sample(range(1,30),12)
list2 = random.sample(range(1,30),13)
print(set(x for x in list1 if x in list2))