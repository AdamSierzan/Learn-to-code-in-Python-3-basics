#Write a program (function!) that takes a list and returns a new list that 
#contains all the elements of the first list minus all the duplicates.
#
#Extras:
#Write two different functions to do this - one using a loop and 
#constructing a list, and another using sets.
#Go back and do Exercise 5 using sets, and write the solution for that in a different function.

new_list = [2,3,2,3,4,5,2,3,4,2,3,5,6,7,8]
#print(list(set(new_list)))

def no_duplicates (any_list):
    return (set(any_list))

print(no_duplicates(new_list))
