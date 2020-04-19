def myfunc(abc):
   result = ''
   for index, letter in enumerate(abc):
       if index%2==0:
            result + letter.upper()
        else:
            result + letter.lower()
        return result

