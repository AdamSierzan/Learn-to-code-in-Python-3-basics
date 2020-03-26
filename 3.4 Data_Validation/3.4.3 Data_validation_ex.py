
data_valid = False

while data_valid == False: 
    grade1 = (input("Type the grade of the first test: "))
    
    try: 
        grade1 = float(grade1)
    except:
        print("Invalid data,please type numbers only. Decimals should be separated with dots.")
        continue
    
    if grade1 < 0 or grade1 > 10:
        print("Grade should be between 0 and 10")
        continue 
    else: 
        data_valid = True 

data_valid = False
while data_valid == False: 
    grade2 = ( input("Type the grade of the second test: "))
    
    try: 
        grade2 = float(grade2)
    except:
            print("Invalid data,please type numbers only. Decimals should be separated with dots.")
            continue
    
    if grade2 < 0 or grade2 > 10:
        print("Grade should be between 0 and 10")
        continue 
    else: 
        data_valid = True

data_valid = False

while data_valid == False: 
    classes = int( input("Type the total number of classes: "))
    
    try: 
        classes = float(grade2)
    except:
            print("Please, type numbers only")
            continue

    if classes <= 0:
        print("The number of classes can't be zero or less")
        continue 
    else: 
        data_valid = True

data_valid = False

while data_valid == False: 
    absences = ( input("Type the number of absences: "))
    
    try: 
        absences = float(absences)
    except:
            print("Please type the numbers only")
            continue
    
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
