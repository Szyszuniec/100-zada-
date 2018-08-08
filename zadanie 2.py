# Program, który będzie obliczał silnię podanej liczby.
# Wynik powinien być wypisany w jednej linii po przecinku.
# Liczba zostaje wpisane w konsoli przez użytkownika.

while True:
    print("Wprowadź liczbę naturalną:")
    x = input()
    y = 1
    try:
        x = int(x)
        while x > 0:
            y = y*x
            x -= 1
        print("Obliczona silnia: " + str(y))
        break
    except ValueError:
        print("Wprowadź liczbę naturalną:")
        x = input()

