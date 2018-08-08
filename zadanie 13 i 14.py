# Write a program that accepts a sentence and calculate the number of letters and digits.
# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

dane = input("podaj zdanie zawierające liczby i litery: ")
litery = 0
liczby = 0
wielkie = 0
małe = 0
for x in dane:
    if x.isalpha():
        litery += 1
    if x.isdigit():
        liczby += 1
    if x.isupper():
        wielkie += 1
    if x.islower():
        małe += 1
print("zdanie składa się z {} liczb".format(liczby))
print("zdanie składa się z {} liter".format(litery))
print("zdanie składa się z {} wielkich liter".format(wielkie))
print("zdanie składa się z {} małych liter".format(małe))