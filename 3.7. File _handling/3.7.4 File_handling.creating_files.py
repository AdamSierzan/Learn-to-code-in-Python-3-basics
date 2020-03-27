#It is important to mention that the append and write modes can also be used to create a new file.
#So if we pass a file name that does not exist it is going to create one.
#The read mode will return an error if the file does not exist.
#So here instead of opening an existing file let's use the Create mode that is represented by an x.#To write on our file we use "w" mode
f = open("text2.txt", "x") #new files has been created,
#to create a file in another folder on my computer
#to do it, we need to write full path
f = open("/home/adam/Desktop/text3.txt", "x") 
#now the file has been created on the desktop