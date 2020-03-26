#loops are very important concept in programming
#loops are structures of repetition.
#We use them to repeat the same lines of code multiple times.

#This is how you create "while" loops

#First let's start a variable called X and that's a sign of value of zero.

#   x = 0 

#Then let's create a list of people that's going to start an empty list

#   people  = []

#Now this is how we start a loop.
#We're going to use the keyword "while" and then we're going to write a condition.

#   while x < 5: 
    
    
#Now there would be this indentation just like the "if" structure. 
#So everything that is aligned here to this point is going to be inside the while loop.
#So if this test returns true it's going to go inside the loop.

# while x < 5:
    #person = input("type the name of a person: ")
    #people.append(person) to add the person to a list

#But if we keep it like this this loop is going to run forever because when we finish here it's going
#to keep running again and again and again unto this doesn't return true anymore.
#But this is not going to happen because we are not changing the value of X..
#So what we need to do is in every iteration of this loop we have to increment the value of X. We can
#do it by typing X equals X plus 1.

# while x < 5:
    #person = input("type the name of a person")
    #people.append(person) to add the person to a list
    #x = x + 1
#we can also use increment operator

# while x < 5:
    #person = input("type the name of a person:")
    #people.append(person) to add the person to a list
    #x += 1
#So this is going to be running in a loop until this test results in false.
#When this happens then we're going to continue with our program.
#In this case let's just print the list of people.

#print(people)

#Ad2

#We could have done it with less lines of code since we're adding people to a list in every iteration
#of the loop.
#We can use the length of the list to control the loop.
#So instead of using X so let's erase this we can use the length
#of that list called people which in the first iteration of the loop is going to be 0.

# people = []
# while len(people) < 5:
    #person = input("Type the name of the person: ")
    #people.append(person) 
#print(people)

#But as we add more people to the list it's going to increase.
#And when this is 5 or greater we're going to jump out of the loop.
#So in this case we don't need to increment the value of any variable.