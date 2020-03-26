# like conditionals loops can also be nested
#so we can use loops inside loops.
#We can also use loops inside conditionals conditionals inside loops and so on.
#it's a dictionary
blog_posts = {"Python": ["The 10 coolest math functions in python", 'How to make HTTP request in Python' , 'A tutorial about data type'], "Java": ['Java basics', 'Java for intermediate']}
#how can we print posts by category?
for category in blog_posts: #in the first iteration, python will to be assigned to the category variable
    print("Posts about:" , category)
    for post in blog_posts[category]:
        print(post)