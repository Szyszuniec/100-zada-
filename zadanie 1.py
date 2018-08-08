# Program, który znajdzie liczby podzielne przez 7,
# a które nie będą wielkrotnością liczby 5
# i będą zawierały się w przedziale pomiędzy 2000 a 3200.
# Liczby powinny być wypisane w linii po przecinku.

i = 2000
liczby = []
while i < 3200:
    a = i%7
    b = i%5
    if a == 0 and b != 0:
        liczby.append(i)
    i += 1
print(liczby)