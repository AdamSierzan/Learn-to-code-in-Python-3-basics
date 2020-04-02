print("Hi, whis programe will let you know what rate (0-10),"
"has the tv series you want to watch:")

series = {
    "Friends": 9, 
    "How I met your mother": 8,
    "Big Bang Theory": 5, 
    "IT:Crowd": 7, 
    "The Office": 7 
    }
    
print(list(series.keys()))
print('-------------------------')
    
    
name = input("Type the name of a tv series:" )
print("TV series {} has {} points in our scale.".format(name, series[name]))


print('------------------------')

new_series = input("Type the name of the series you want to add to list: ")
new_rating = input("How would you rate it:")

series[new_series] = float(new_rating)
print(list(series.keys())) 

   


    
