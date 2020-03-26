#ten program służy do pozyskiwania danych z biblioteki, użytkownik prosi o informację z bilbioteki i albo ją pozyskuje, albo nie
#aby to zrobić, musimy stworzyć bibliotekę z danymi, następnie stworzyć zmienną, która wyciągnie z biblioteki informację jeśli się tam znajduje.

person = {"name": "Jack",  "gender": "male", "age": "35", "adress": "Seasame street", "phone number": "7876655" }
key = input("what information do you want to know:")
result = person.get(key, "ups, we don't have this information")
print(result)
#every time we work with user input to find smth we have to make sure that what we want to find is in lower case, and the user input is in lower case as well. 
# We should convert the user input to lower case, use the lower method. we can apply it right after the input:
# key = input("what information do you want to know:").lower()