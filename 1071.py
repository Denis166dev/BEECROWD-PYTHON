X = int(input())
Y = int(input())

total = 0

if X > Y:
    for numero in range(Y + 1,X):
        if numero%2 != 0:
            total += numero
    print(total)

else:
    for numero in range(X + 1,Y):
        if numero%2 != 0:
            total += numero
    print(total)