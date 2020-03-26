#Dictionaries are like lists, but instead of elements organized by index, elemnets have keys, if we want to organize the information about the person, we can do it with a list
#if we would recieve this information from the for ex. server, we wouldnt know what it means., it would be better to have dictionarie in this case
#to start the dictionary we use curved braces {}
#each elemnt is always composed by key value pair
person = {"first_name": "John", "last_name": "Green", "birth_year": "1940",  "country_origin": "Canada"}
print(type(person))
print(person["first_name"] )
#dicitonaries are used most programmin languages
# they are mudible in python
person["birth_year"] = 1940
print(person["birth_year"])
print(person)
#we can also add the information/ key/ or property how its called i python
person["marital_status"] = "Married"
#they can be of any data type
person["children"] = ["Natalie", "Ethan"]
print(person)
#to add the key to the dic, we use apped
person["children"].append("Anna")
print(person)
#if we try to get the property that doesnt exist, we cant get it and get the error, which can cause problems, to avoid it, we  should try to use "get" function
print(person.get("age", "invalid property"))
#if we have any variable, lets call it key, and we asociate the string with it, lets say first_name from our dict, if we do person[Key], we will get the property, its the same as person["first_name"]

Key = "first_name"
print(person[Key])
#if we want to earase the inf from dict we do person.clear()

