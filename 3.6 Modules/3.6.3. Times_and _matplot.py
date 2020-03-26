import time as t
import matplotlib.pyplot as plt
print("Hi, this program will check how fast you can type the word given by me")
word = "settings"
time = []
attempt = 0
mistakes = 0    

print(input("Press enter when you're ready"))
print("The word is:", word, ", the time start now")

while attempt < 5:
    start = t.time()
    
    attempt1 = input(("Type the word: "))
    
    end = t.time()
    t_elapsed = end - start
    time.append(t_elapsed)
    
    attempt += 1
    
    if (attempt1.lower() != word):
        mistakes += 1
print("You made " + str(mistakes) + " mistake(s).")
x = [1,2,3,4,5]
y = time
plt.plot(x,y)
legend = ["1", "2", "3", "4", "5"]
plt.xticks(x, legend)
plt.ylabel("Time in seconds")
plt.xlabel("Attempt")
plt.title("Your typing evolution")
plt.show()