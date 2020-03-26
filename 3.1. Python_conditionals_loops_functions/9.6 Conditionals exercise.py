#Create a program to calculate the BMI of a person the BMI stands for body mass index.
#Ask the height in meters and the body weight in kilos.

#So the BMI is going to be calculated by the weight in kilos divided by the squared height.
#So you're going to have the same index then you're going to print the body mass index and also the classification
#according to the following table.

#So if the BMI is less than 18.5 the classification is underweight 
#if it's between 18.5 and 24.9 the classification is normal weight 
#if it's between 25 and 29.9 the classification is overweight 
#and if it's 30 or greater the classification is obesity.

#Good luck and when you've finished the exercise go back here to see the solution

print("Hi this programme will calculate your BMI")
your_weight = float(input("Please enter your weight in kg: "))
your_height = float(input("Please enter your height in meters: "))
bmi  =  your_weight / (your_height * your_height)
print("Your bmi is: ", round(bmi, 2))
if (bmi <= 18.5):
    print("Your classification is underweight")
elif (bmi > 18.5 and bmi <= 24.9 ):
    print ("Your classification is normal weight")
elif (bmi >= 25 and bmi <= 29.9):
    print ("Your classification is overweight")
else:
    print("Your classification is obesity")
