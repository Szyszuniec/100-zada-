# Napisz program, który będzie sprawdzał hasło użytkownika.
# Hasło musi spełniać następujące kryteria:
# 1. przynajmniej jedna mała litera
# 2. przynajmniej jedna cyfra
# 3. przynajmniej jedna duża litera
# 4. przynajmniej jeden znak szczególny [$#@]
# 5. co najmniej 6 znaków
# 6. nie dłuższe niż 12 znaków.
# Twój program powinien przyjmować sekwencje haseł oddzielonych od siebie przecinkiem i sprawdzać
# pod kątem powyższych wymagań. Hasła, które spełniają kryteria powinny być wydrukowane po przecinku.

print("Wprowadź propozycję hasła (możesz podać kilka propozycji oddzielając je przecinkiem):")
dane = input()
hasla = dane.split(",")
warunek1 = False
warunek2 = False
warunek3 = False
warunek4 = False

for haslo in hasla:
    haslo = str(haslo)
    x = len(haslo)
    if x >= 6 and x <= 12:
        for x in haslo:
            if x.islower:
               warunek1 = True
            if x.isdigit:
                warunek2 = True
            if x.isupper:
                warunek3 = True
            if x == "$" or x == "#" or x == "@":
                warunek4 = True
        if warunek1 and warunek2 and warunek3 and warunek4:
            print(haslo, end=",")
            warunek1 = False
            warunek2 = False
            warunek3 = False
            warunek4 = False
