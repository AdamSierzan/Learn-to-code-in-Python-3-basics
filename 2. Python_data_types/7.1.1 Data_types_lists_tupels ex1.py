print("Hi this programme will generate your birth month when you eneter it")
months  = ("January", "February", "March", "April", "June" , "July", "August", "September", "October", "November", "December")
birthday = input("Type your date of birth in the formay: DD-MM-YYYY: ")
print(birthday)
month = birthday[3:5]
print(month)
monthAsNumber = int(month)   # zmieniam typ zmiennej ze stringa na liczbę
print(monthAsNumber)
index = monthAsNumber - 1 #  - 1, bo zaczynamy liczyć od 0 
print(index)
monthFromTuple = months[index]
print(monthFromTuple)
