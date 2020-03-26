#In this lesson we're going to learn how to do HTTP request using python
#First we have to understand what HTTP is

#HTTP is the main transfer protocol used in the web 
#When typing an adress in your browser, your're sending HTTP request
#and the server responds with HTML/CSS/JavaScr/ code for the page

#Your browser interprets the code and render the web page 

#HTTP requests are not only used for getting web pages
#We can use it to send and recieve data

#To make it work in python, we need request module
import requests
r  = requests.get("Http://www.google.com") #you can send the request like this
print(r.status_code)

#the request code cna vary, but for value :
# 200 it means ok, 
# 403 forbidden (you probably didn't send the authentication correctly or it was missing an API
# 404 (not found)

#Now we can print the headers of the request, to show info about the request
#We can get specific info by typing specific thing
print((r.headers)["Date"])

#Now let's get to the most iportnat part which is getting the actual response to our request, so the data we requested
print(r.text)
#What we see here is HTML code for Google's front page, so what we requestred for


#So now what do we do with the HTML code from Google.
#Actually this is not going to be very useful for us but now that we know the basics of HTTP requests we
#are going to get some data from  HTTPs through the web and things will start to get interesting.
#That's what we're going to do in the next video.
#I'll see you then.