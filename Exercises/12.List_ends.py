#Write a program that takes a list of numbers 
#(for example, a = [5, 10, 15, 20, 25]) 
#and makes a new list of only the first and last elements of the given list. 
#For practice, write this code inside a function.

a = [5, 10, 15, 20, 25]
b = a[0:5:4]
print(b)

def new_list(i):
    print(i[0],i[len(a)-1])
new_list(a)