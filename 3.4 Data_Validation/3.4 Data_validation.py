#in this lesson we're going to talk about data validation,
#let's talk about some problems that might occur with the programe we created before
#It has no validation, a user can type grade higher than 10, and the programme will accepte it
#also it will crash when a user will type a string instead of a number
#let's see how we can do basic data validation using loops
#then we will keep our programe frome crashing by oding error handing

#before asking user for an input we will create a variable called "Data_valid" and assign it to a loop of false 

data_valid = False
while data_valid == False: #test will return true because data_valid is equal to false
    grade1 = float( input("Type the grade of the first test: "))
    if grade1 > 0 or grade1 < 10:
        print("Grade should be between 0 and 10")
        continue #it will jump out of the loop and start again
    else: #if "if" is not true it means we have valid input
        data_valid = True #when we do it, we're ending the loops, and continue with programe

#now we're going to do the same thing with the second grade
data_valid = False
while data_valid == False: 
    grade2 = float( input("Type the grade of the second test: "))
    if grade2 < 0 or grade2 > 10:
        print("Grade should be between 0 and 10")
        continue 
    else: 
        data_valid = True
#and with the number of classes
data_valid = False
while data_valid == False: 
    classes = int( input("Type the total number of classes: "))
    if classes <= 0:
        print("The number of classes can't be zero or less")
        continue 
    else: 
        data_valid = True
#and with the number of absences
data_valid = False
while data_valid == False: 
    absences = int( input("Type the number of absences: "))
    if absences < 0 or absences > classes:
        print("The number of absences can't be less than zero or greater than the number of classes")
        continue 
    else: 
        data_valid = True

avg = (grade1 + grade2) / 2

attendance = (classes - absences) / classes

print("Average grade: ", round(avg, 2 ))
print("Attendence rate: ", str(round((attendance * 100), 2)) + '%' )

if (avg >= 5 and attendance >= 0.8):
   print("Congratulations you've passed the exam")
elif (avg < 5 and attendance < 0.8):
    print("Sorry you've failed, due to attendance rate lower than 80% and average lower than 5")
elif (attendance >= 0.8):
    print("you've failed due to average lover than 5")
else:
    print("Sorry you've failed, due to attendance rate lower than 80%")
