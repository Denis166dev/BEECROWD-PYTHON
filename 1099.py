N = int(input())

for _ in range(N):
    X,Y = map(int, input().split())
    total = 0

    if X > Y:
        for numero in range(Y + 1, X):
            if numero % 2 != 0:
                total += numero
    elif X < Y:
        for numero in range(X + 1, Y):
            if numero % 2 != 0:
                total += numero
    print(total)
