#dodaj każdą liczbę od 1 do do 100 podzielną przez 3 i 5  i podaj wynik
total = 0
for i in range(1, 100):
    if i % 3 == 0 or i % 5 == 0:
        total += i
print(total)

