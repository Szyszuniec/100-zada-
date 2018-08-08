# You are required to write a program to sort the (name, age, height) tuples by ascending order
# where name is string, age and height are numbers. The tuples are input by console. The sort criteria is:
# 1: Sort based on name;
# 2: Then sort based on age;
# 3: Then sort by score.
# The priority is that name > age > score.

def trzeciawart(wart):
    return wart[2]
def drugawart(wart):
    return wart[1]

linia = ""
print("Podaj dane (Imię,Wiek,Wzrost):")
baza = []
while True:
    linia = input()
    if linia == "koniec":
        break
    osoba = tuple(linia.split(","))
    baza.append(osoba)

baza.sort(key=trzeciawart)
baza.sort(key=drugawart)
baza.sort()
print(baza)