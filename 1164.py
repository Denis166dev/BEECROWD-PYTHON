N = int(input())

for _ in range(0,N):
    soma = 0
    X = int(input())
    for i in range(1,X):
        if X%i == 0:
            soma += i
    if X == soma:
        print(f'{X} eh perfeito')
    else:
        print(f'{X} nao eh perfeito')