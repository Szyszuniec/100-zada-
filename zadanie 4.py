# Napisz program, w którym użytkownik wpisuje liczby oddzielone
# od siebie przecinkiem, a program zwraca listę oraz krotkę(tuple).

print("wprowadź liczby oddzielone przecinkiem:")
szereg = input()
z = len(szereg) + 1

if szereg[-1] != ",":
    szereg = szereg + ","

a = 0
b = 0
lista = []

while b < z:
    if szereg[b] != ",":
        b +=1
    else:
        x = szereg[a:b]
        a = b + 1
        b += 1
        lista.append(x)

print(lista)
krotka = tuple(lista)
print(krotka)