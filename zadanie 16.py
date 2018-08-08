# Użyj comprehension list, aby otrzymać kwadrat każdej liczby nieparzystej z listy.
# Lista ma być wpisana przez użytkownika jako sekwencja liczb oddzielonych od siebie przecinkiem.

dane = input("wpisz liczby oddzielone przecinkiem: ")
liczby = dane.split(",")
for liczba in liczby:
    liczba = int(liczba)
    if liczba%2 == 1:
        print(liczba**2, end=",")