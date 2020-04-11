#Write a Python program to count the number of even and odd numbers from a series of numbers. Go to the editor
#Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
#Expected Output :
#Number of even numbers : 5
#Number of odd numbers : 4

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even = []
odd = []
for x in numbers:
    if x%2==0:
        even.append(x)
    else:
        odd.append(x)
print("\nNumber of even numbers: ", len(even), "\nNumber of odd numbers: ", len(odd))