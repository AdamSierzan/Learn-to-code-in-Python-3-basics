# Write a Python program to get the Fibonacci series between 0 to 50. Go to the editor
#Note : The Fibonacci Sequence is the series of numbers :
#0, 1, 1, 2, 3, 5, 8, 13, 21, ....
#Every next number is found by adding up the two numbers before it.
#Expected Output : 1 1 2 3 5 8 13 21 34
lenght = int(input("How many fibonacci series you want"))
n = [1,1]
while len(n) < lenght:
    x = len(n[:-1]) + len(n[:-2])
    n.append(x)
print(n)

