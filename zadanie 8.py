# Napisz program, który będzie akceptował pisane przez użytkownika
# wyrazy (dodawane po przecinku) i zwróci te same wyrazy posortowane alfabetycznie.

x = (input("wpisz wyrazy oddzielone przecinkami: ")).lower()
lista = x.split(",")
lista = sorted(lista)
print(lista)