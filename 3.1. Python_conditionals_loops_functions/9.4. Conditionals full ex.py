grade1 = float(input("Type the grade of the first test: "))
grade2 = float(input("Type the grade of the second test: "))
absences = int(input("Type the number of absences: "))
classes = int(input("Type the number of the classes: "))

avg = (grade1 + grade2)/2

attendance = (classes - absences) / classes

print("Average grade: ", round(avg, 2 ))
print("Attendence rate: ", str(round((attendance * 100), 2)) + '%' )
if (avg >= 5):
    if (attendance >= 0.8):
        print("Congratulations you've passed the exam")
    else:
        print("Sorry you've failed, due to attendence rate lower than 80%")
elif (attendance >= 0.8):
        print("Sorry you've failed, due to avg lower than 5")
else:
    print("Sorry you've failed, due to attendence lower than 80%, and avg lower than 5")
