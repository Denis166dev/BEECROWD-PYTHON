while True:
    M, N = map(int, input().split())
    soma = 0

    if M <= 0 or N <= 0:
        break

    menor = min(M, N)
    maior = max(M, N)

    for numero in range(menor, maior + 1):
        soma += numero

    valores = ' '.join(str(i) for i in range(menor, maior + 1))
    print(valores + f' Sum={soma}')