#in this lesson we're going to learn and and or operators
#and learn to solve the problem

#In the previous lesson we created a program to calculate the grades and output the result of a student.
#We use the nested if structure to solve our problem and now we are going to learn two new operators
#So what those operators do is testing multiple conditions at the same time.

# if (avg >= 5):
#   if (attendance >= 0.8):
#        print("Congratulations you've passed the exam")
#instead of nesting we can do it like this
# if (avg >= 5 and attendance >= 0.8):
#    print("Congratulations you've passed the exam")

#So after that we can start an elif statement and we can test the other extreme.
#That is the average grade is less than six and the attendance is less than zero point eight
#in this case we know that the student has failed for both reasons.

# if (avg >= 5 and attendance >= 0.8):
#   print("Congratulations you've passed the exam")
# elif (avg < 5 and attendance < 0.8):
#   print("Sorry you've failed, due to attendence rate lower than 80%")

#Now let's do another elif statement

# if (avg >= 5 and attendance >= 0.8):
#   print("Congratulations you've passed the exam")
# elif (avg < 5 and attendance < 0.8):
#   print("Sorry you've failed, due to attendence rate lower than 80%")
# elif (attendence >= 0.8):

#and if we get inside here we know that the student has failed due to an average grade lowered and six
#and how do we know it.
#Because if we had failed for both reasons we would have ended here.
#So if we are entering here it means that he hasn't been approved and he hasn't failed for both reasons.
#So if the attendance rate is higher than zero point eight at this point it means that he has failed
#due to an average grade lower than six.

# if (avg >= 5 and attendance >= 0.8):
#   print("Congratulations you've passed the exam")
# elif (avg < 5 and attendance < 0.8):
#   print("Sorry you've failed, due to attendence rate lower than 80%")
# elif (attendence >= 0.8):
# else:
#       print("Sorry you've failed, due to attendence rate lower than 80%")

#So this is how the end operator works the or operator is similar but the difference is that when we
#use or only one has to be true for the test to return true.
