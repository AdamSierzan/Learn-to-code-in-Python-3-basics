#JSON is a object converted into string, since all programming languages work with string its suitable
import requests
r = requests.get("https://opentdb.com/api.php?amount=10&category=12&difficulty=easy&type=boolean")
print(r.status_code)
print(r.text)

#to work with JSON we have to parse the the string
#for that we're using the internal module called JSON
import json

#now let's create a variable called question
#and let's use a method of the JSON module called load which converts 
#from JSON or string into Python dict
question = json.loads(r.text)
print(question)
# now it seems the same but it's a dictionary

#to make it easier to read, we can use the module pprint
#and now we can use it with the variable "question" that we turned into a dictionary
import pprint 
pprint.pprint(question)

#to get the specific value (category in this case) we can type:
print(question['results'][0]['question'])
#results is a list inside question dictionary, category is a first element from this list,
#so it has index 0