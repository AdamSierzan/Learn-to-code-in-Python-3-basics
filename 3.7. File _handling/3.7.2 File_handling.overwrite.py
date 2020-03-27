#To write on our file we use "w" mode
f = open("text.txt", "w") 
f.write("This text will overwrite the content of our file")
f = open("text.txt")
print(f.read())
#if we don't want to overwerite it, use a mode
