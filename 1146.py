while True:
    X = int(input())
    if X == 0:
        break
    valores = ' '.join(str(i) for i in range(1, X + 1))
    print(valores)