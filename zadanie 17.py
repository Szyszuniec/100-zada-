# Write a program that computes the net amount of a bank account based a transaction log from console input.
# The transaction log format is shown as following:
# D 100
# W 200
# D means deposit while W means withdrawal.

print("Podaj wpłaty (format D <kwota>) i wypłaty (format W <kwota>): Zakończ wpisując SUMA")
operacja = 0
wynik = 0
while operacja != "SUMA":
    operacja = input()
    try:
        kod = operacja.split(" ")
        if kod[0] == "D":
            wynik += int(kod[1])
        if kod[0] == "W":
            wynik -= int(kod[1])
    except:
        continue

print(wynik)