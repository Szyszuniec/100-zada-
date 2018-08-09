# Stwórz klasę, która będzie miała przynajmniej dwie metody:
# getString - pobieranie łańcucha znaków z konsoli
# printString - wypisywanie łańcucha znaków wielkimi literami
# Dodaj również prostą funkcję testującą.

class Zadanko(): # Definiujemy klasę
    def __init__(self):
        pass
    def getString(self): # Ta metoda zapamiętuje wprowadzony łańcuch znaków
        self.mem = input()
    def printString(self): # Ta metoda zwraca zapamiętany łańcuch znaków wielkimi literami
        print(self.mem.upper())


zad = Zadanko() # Tutaj tworzymy obiekt klasy

def test(): # Definiujemy funkcję testującą
    zad.getString()
    zad.printString()

test() # Odpalamy test