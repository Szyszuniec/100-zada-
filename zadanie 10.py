# Napisz program, który będzie akceptował sekwencje słów
# oddzielonych od siebie spacją i usunie duplikaty oraz zwróci
# słowa posortowane alfanumerycznie.

wyrazy = input("wpisz wyrazy oddzielone spacją: ")
lista = sorted(wyrazy.split(" "))
wynik =[]
for wyraz in lista:
    x = lista.count(wyraz)
    while x > 1:
        lista.remove(wyraz)
        x -= 1
    wynik.append(wyraz)
print(wynik)