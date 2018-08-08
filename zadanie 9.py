# Napisz program, który będzie akceptował zdania (każde od nowej linii)
# i będzie zwracał te zdania pisane wielkimi literami.

print("wpisz zdania, zakończ wpisując 0:")
line = ""
while True:
    last = input()
    line = line + "\n" + last
    if last == "0":
        line = line[:-1]
        break
line = line.upper()
print(line)