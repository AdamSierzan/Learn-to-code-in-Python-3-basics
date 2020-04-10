#Write a Python program to construct the following pattern, using a nested for loop.
#   * 
#   * * 
#   * * * 
#   * * * * 
#   * * * * * 
#   * * * * 
#   * * * 
#   * * 
#   *

a = [1]
b = [2,3,4,5,4,3,2,1]
for x in a:
    print("*")
for y in b:
    print(y*"*")
