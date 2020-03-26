#now let's create a function that will help us convert fahrenheit degreeses to celsius
def fahr2celsius(fahr): #so we have a function with fahrenheit argument
    celsius = (5 * (fahr - 32)) / 9 #and a variable "ceslius"
    return celsius #now instead of printing the temp in C we can just return the value
 #now we can do anything with this with this value, since we're not stuck with the print statement
 #let's convert something
print("Celsius", round (fahr2celsius(100),2)) 
#we can use this function to convert the value to Kelvin degreeses
print("Kelvin", round (fahr2celsius(100) + 273.5,2))  #so we're using the result of our function in multiple ways


# we have to remember, that we can have as many argument as we want in the function
def say_hello(person1, person2): 
    print("Hello " + person1 + ",how're doing?" + person2 + " is waiting for you" )

#say_hello("jane") #if we pass only one argument it's going to result in error
say_hello("Jane", " Tim") #they have to be in the same order, we created them
#Jane in person1 and Tim is person 2


#Now how can we have functions like the round function in which we can inform the number of the decimal places or not?
#we can use one or two argument, and asign default value for and argument
def say_hello(person1, person2 = "The Director"): #we use the equal sign and pass a value here, it's going to be default if it's missing late
    print("Hello " + person1 + ",how're doing?" + person2 + " is waiting for you" )
say_hello("Jane") #the director is now assigned as person 2 instead of getting and error
# THE ARGUMENT OF THE FUNCTIONS ARE ALSO CALLED PARAMETERS

#in the case of the round function, You will meet the number of decimal places.
#It just rounds the number without any decimal places.
#So the default value is zero.