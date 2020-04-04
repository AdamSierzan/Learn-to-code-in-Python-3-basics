
#Take two lists and write a program that returns a list that 
#contains only the elements that are common between the lists (without duplicates). 
#Make sure your program works on two lists of different sizes.

#Extras:
#Randomly generate two lists to test this
#Write this in one line of Python (don’t worry if you can’t figure this out at this 
# point - we’ll get to it soon)

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(set(a) & set(b))

#or

x = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
zlist = []
for z in x:
  if z in y:
    zlist.append(z)
print(zlist)


#* For random numbers
import random

randomlist_c = []
for i in range(0,5):
  n = random.randint(1,30)
  randomlist_c.append(n)
print(randomlist_c)
randomlist_d = []
for i in range(0,5):
  nb = random.randint(1,30)
  randomlist_d.append(nb)
print(randomlist_d)
print(set(randomlist_c) & set(randomlist_d))

#* generates 5 random numbers
randomlist_e = random.sample(range(1,30), 5)
randomlist_f = random.sample(range(1, 30), 5)
print(set(randomlist_e) & set(randomlist_f))


