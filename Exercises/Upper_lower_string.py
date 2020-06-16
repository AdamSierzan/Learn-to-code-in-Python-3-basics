def myfunc(abc):
   result = ''
   for index, letter in enumerate(abc):
        if index%2==0:
            result + letter.upper()
        else:
            result + letter.lower()
        return result


lambda num: num**2
myNums = [3,4,5,3,2]
print(list(map(lambda num:  num<2,myNums )))