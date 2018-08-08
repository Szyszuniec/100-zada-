# Mając daną liczbę całkowitą n (lub wpisaną przez użytkownika),
# napisz program, który zwróci słownik zawierający liczby od 1 do n i kwadraty tych liczb.

Liczby = {}
while True:
    print("wprowadź liczbę naturalną:")
    try:
        n = int(input())
        i = 1
        if n > 0:
            while i <= n:
                Liczby[i] = i**2
                i +=1
            break
        else:
            continue
    except ValueError:
        continue
print(Liczby)