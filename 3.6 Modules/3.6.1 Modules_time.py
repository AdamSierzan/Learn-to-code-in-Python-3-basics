#In this lesson we will work with the modules
#In this particular lesson we will work with Time module
import time as t #when the name of the module is long, we can use import as, to call it "t" in this case
print(t.localtime()) # That's how we check local time

#now let's say our user is doing a transaction in our programe
#and we want to print a msg with the exact time of the transaction 
# we can create a variable called time 
time_now = t.localtime()
print("Transaction completed at", str(time_now.tm_hour) + "h" + str(time_now.tm_min) + "m")
 #now let's talk about another intresting thing from time module


print(t.time()) # t.time stands for time stamp which is total time,which started in 01.01.1970
#if we want to make calculations with dates, it's easy to do them with timestamps

#Now let's say our product takes 7 days to be delivered
#to tell the client when he's going to recieve it, we have to add 7 days, to the current time
#but if we just add days we would need to write another complex function, to correct day and month
#it's better to use time stamp, but in order to do that, we need to
#convert days into seconds
time_now = t.time() #let's take the now time
delivery_time = time_now + (86400*7 )   #and delivery time which is time now plus seconds in 7 days
print(t.localtime(delivery_time)) #so, what we did, is using local time function but with the timestamp calculated just before
#so now we have the info about tthe delivery date, without the need of writing crazy function to calculate it


#another intresting function of the time module is sleep function
#it is used to delay the execution of the the next line of code
t.sleep(5) #5 secunds of delay
print("xD")