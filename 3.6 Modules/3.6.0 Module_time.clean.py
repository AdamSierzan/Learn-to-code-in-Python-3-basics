import time as t #when the name of the module is long, we can use impor as, to call it "t" in this case
print(t.localtime()) # That's how we check local time
time_now = t.localtime()
print("Transaction completed at", str(time_now.tm_hour) + "h" + str(time_now.tm_min) + "m")


print(t.time())
time_now = t.time() 
delivery_time = time_now + (86400*7 )
print(t.localtime(delivery_time))