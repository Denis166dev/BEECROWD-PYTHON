X, Y = map(int, input().split())
contador = 1

for i in range(1, Y + 1):
    print(i, end='')
    if contador % X == 0:
        print()
    else:
        print(' ', end='')
    contador += 1
