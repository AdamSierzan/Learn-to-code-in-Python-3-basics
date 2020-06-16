def round_sum(a, b, c):
  return round10(a) + round10(b) + round10(c)
  
def round10(num):
    if num <= 10:
        if num in range(5,11):
            x = 10 - num
            return ((num) + x)
        else:
            return 0

    if num > 10 and num <= 20:
        if num in range(15,21):
            x = 20 - num
            return ((num) + x)
        else:
            return 10
print(round_sum(4,14,16))