import time as t
import matplotlib.pyplot as plt

print("Hi this program will let you see your advance in typing speed of the given work")
input("Press start when you're ready")

print("The given word is: programming")

mistakes = 0
times = []

while len(times) < 5: #it has to be len
    start = t.time()
    word = input("Please type the given word: ")
    end =  t.time()
    time_elapsed = end - start

    times.append(time_elapsed)

    if (word.lower() != 'programming'):
        mistakes += 1
print("You've made", mistakes)
print("Now let's see your evolution")

x = ["1", "2", "3,", "4", "5"]
y = times

plt.bar(x,y)
plt.xlabel("Attempt")
plt.ylabel("Time in seconds")
plt.title("Evolution of typing")
plt.show()


    
