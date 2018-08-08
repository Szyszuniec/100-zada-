# Write a program which accepts a sequence of comma separated 4 digit binary
# numbers as its input and then check whether they are divisible by 5 or not.
# The numbers that are divisible by 5 are to be printed in a comma separated sequence.

dane = input("wpisz liczby oddzielone przecinkiem: ")
liczby = dane.split(",")
binarne = []
for liczba in liczby:
    binarna = int("0b" + str(liczba), 2)
    if binarna%5 == 0:
        binarna = str(bin(binarna))[2:]
        print(binarna, end=", ")