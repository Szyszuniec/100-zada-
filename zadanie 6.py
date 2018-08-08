# Napisz program, który obliczy wartości wg podanego wzoru
# Q = pierwiastek kwadratowy z [(2 * C * D)/H]
# C = 50, H = 30
# D to liczby, które mają zostać wprowadzona przez użytkownika - każda liczba oddzielna przecinkiem.

A = input("Wprowadz liczby oddzielone przecinkiem: ")
C = 50
H = 30
lista = A.split(",")
for liczba in lista:
    D = int(liczba)
    Q = ((2*C*D)/H)**(1/2)
    Q = int(round(Q))
    print(Q, end=",")