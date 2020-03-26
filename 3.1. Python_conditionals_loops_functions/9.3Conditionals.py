#Condtitionals, we learn that if is a logical stracture, It evaluates boolean values to decide whether executing blocks of code or not.
#We are now going to create a program to evaluate the grades of a student and see how we can test multiple
#conditions using nested if 
#The first thing we will do is ask for grades of two tests made by a student so Grade 1structures.
#
grade1 = float(input("Type the grade of the first test"))
grade2 = float(input("Type the grade of the second test"))
#we are also going to ask to number of absences, which is goint to be and integer
absences = int(input("Type the number of absences"))
#We are also going to need the total number of classes so we can calculate the attendance rate
classes = int(input("Type the number of the classes"))
#now that we have all the inputs.
#We can calculate the average grade which is going to be grade one plus grade two
avg = (grade1 + grade2)/2
attendance = (classes - absences) / classes
#if (avg > 5):
#    print("Congratulations you've passed th exam")

#if this is true.
#We don't know if the student was approved yet because we still need to check if he had more than 80
#percent of attendance rate.
if (avg > 5):
    if (attendance >= 0.8):
        print("Congratulations you've passed the exam")
    else:
        print("Sorry you've failed")
else:
        print("Sorry you've failed")
#So this way would just solved our problem using nested if structures that are if structures inside if
#structures.
#Now it would be a bit better if we knew the reason why the student has failed.if (avg > 5):
if (avg > 5):
    if (attendance >= 0.8):
        print("Congratulations you've passed the exam")
    else:
        print("Sorry you've failed, due to attendence rate")#this else state is related with "if attendence" not "if avg"
else:
        print("Sorry you've failed, due to avg")#this else state is related with "if avg" not "if attendence", so we know 
# he failed due to avg, but we dont know about the attendence"

#we need to change the code to know the reason 
if (avg > 5):
    if (attendance >= 0.8):
        print("Congratulations you've passed the exam")
    else:
        print("Sorry you've failed, due to attendence rate lower than 80%")#this else state is related with "if attendence" not "if avg"
elif: (attendance >= 0.8)
        print("Sorry you've failed, due to avg lower than 5")#And if we get here it means that this test has failed. So the average grade is lower than six.
#So in this case we just have to test attendance again and if the attendance is higher 
# than zero point
else:
    print("Sorry you've failed, due to attendence lower than 80%, and avg lower than 5")

#now if we get to this point it means that the grade is not greater than six and the attendance rate, is not greater than zero point eight. 
#So this means that the student has failed due to an average grade lowered and six and