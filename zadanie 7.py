# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
# The element value in the i-th row and j-th column of the array should be i*j.

X = int(input("podaj wartość X: "))
Y = int(input("podaj wartość Y: "))
lista = []
for j in range(Y):
    for i in range(X):
        lista.append(i*j)
    print(lista)
    lista = []
