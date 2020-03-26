#let's put to variables 
num1 = float(input("type the first number:"))
num2 = float(input("type the second number:"))
#now we can use the if statement, we do it like this
# if (num1 > num2)
#in the parentesis it is expecting the true or false valuable, in most programming languages we use curly braces, 
# and everything in the curly braces is the part of the "if", but not in python, in python we use colon ":"
#the ":" makes automaticly an indetetion, so everything starting with indetetion is the part of if statemtnt
if (num1 > num2):
    print(num1, "is grater than", num2)
elif (num1 == num2):
    print(num1, "is equal than", num2)
#so if this is true it's going to execute this code
else:
    print(num1, "is smaller than", num2)
#Here's how it works, if first statement is true, it's going to ignore the other two statements, 
# if it's not ttrue it's going to continue in structute, if second statemnt is not true it's going to exectue the third one,
#which will be exectued 