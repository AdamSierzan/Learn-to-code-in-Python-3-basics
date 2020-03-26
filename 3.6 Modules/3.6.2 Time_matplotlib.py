#matplotlib in python are used to do charts in python
#matplotlib is and external module, so we have to install it
#let's install it
import matplotlib.pyplot as plt

#now we can create two lists to create simple chart
x = [1,2,3,4]
y = [1000,1500,1400,1200]
plt.plot(x,y) #now we can use the plot function, with two arguments which are lists of values
plt.show() #and now we can show the chart

#So the lists have to be numeric, but we can assign a legend to the list

#So let's create another list called legend and instead of numbers let's write the months

legend = ["January", "February", "March", "April"]
plt.xticks(x, legend) #so we use the function xticks to assign to "x" the "legend"
plt.plot(x,y)
plt.show()

plt.bar(x,y)
plt.ylabel("Sales in USSR")
plt.title("Monthly sales")
plt.show()