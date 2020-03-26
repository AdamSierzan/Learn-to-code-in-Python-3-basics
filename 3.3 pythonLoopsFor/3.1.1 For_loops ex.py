people = ["john", "mary", "jack"]
for name in people:
    print(name)

print("--------------")


blog_posts = ["", "The 10 coolest math functions in python", "How to make HTTP request in Python", "A tutorial about data type"]
for post in blog_posts: 
    if post ==  "":
        continue
    else:
        print(post)