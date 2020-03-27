#To write on our file we use "w" mode
f = open("text.txt", "a") 
f.write("\nThis text will be added to the text")
f = open("text.txt")
print(f.read())
