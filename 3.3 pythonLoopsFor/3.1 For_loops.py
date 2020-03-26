#For loops work as sequence iterators
#Let's create a list which is a sequence of elemnets using "while loops"

blog_posts = ["The 10 coolest math functions in python", "How to make HTTP request in Python", "A tutorial about data type"]
counter = 0
while counter < len(blog_posts):
    print(blog_posts[counter])
    counter += 1

print("--------------")


#It's much easier to do that using for
blog_posts = ["The 10 coolest math functions in python", "How to make HTTP request in Python", "A tutorial about data type"]
for post in blog_posts: #we created a variable "post" and by default it's assigned to every elent from list
    print(post)


print("--------------")

# We learned the "break" statement, and there's also a "continue" statement, to avoid print the empty values

blog_posts = ["", "The 10 coolest math functions in python", "", "How to make HTTP request in Python", "A tutorial about data type"]
for post in blog_posts: 
    print(post)
#To avoid printing empty values we use: 
blog_posts = ["", "The 10 coolest math functions in python", "How to make HTTP request in Python", "A tutorial about data type"]
for post in blog_posts: 
    if post ==  "":
        continue
    print(post)

print("--------------")

sentence = "I dont care"
for word in sentence:
    print(word)

print("--------------")

#We can also define a specific number of iterations by using range function

for x in range(0,10):
    print(x)

#We can also use for loops in dictionary
#Let's create a dictionary
person  = {"Name": 'Karen Smith', "Age": 25, "Gender":  'Female'}
for info in person:
    print(info, ':', person[info]) #person [info] aby wydrukować wartość tej informacji