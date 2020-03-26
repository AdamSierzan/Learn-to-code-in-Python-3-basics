#Let's do a program to make a guess game 
#in this case.
#Let's start of a variable called number with the value of 5 let's create another variable called guess

number = 5
guess = int(input("Try to guess the number between 0 and 10")) 
#convert this to integer so we can compare with the number we have here.
#to do it, we can do  loop

#Let's just start a loop that we run forever.
#We can do this by typing while true because every time this test returns true the loop is going to be
#executed.
while True: 
# So in this case the loop is going to be executed forever unless we stop the execution with a break statement
#which is what we're going to do.
while True:
    if guess == number:
        break #So the break statement will stop the execution of the loop and jump out of it if that doesn't happen.
#if the user will guess the number the program will stop. but we have to 
while True:
    if guess == number:
        break
    else:
        guess = int(input("nope, try again: "))
print("You guessed it. I was thinking about:", number)