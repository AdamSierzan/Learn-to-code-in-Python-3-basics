a = int(input("Type the number so the program will tell you the list of divisors of that number: "))

divisors = []
list_range = list(range(1, a+1))
x = 1
#a % x = 0

for i in list_range:
    if a % i  == 0:
        divisors.append(i)
print(divisors)

def has_33(nums):
    for i in range(len(nums)-1):
        print(range(len(nums)))
        if nums[i] == 3 and nums[i+1] == 3:
            return True
        else:
            False
print(has_33(1,2,3,4,5,6,7,8))



    


    