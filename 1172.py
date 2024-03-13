valores = []

for _ in range(0,10):
    N = int(input())
    valores.append(N)

for i, valor in enumerate(valores):
    if valor <= 0:
        valores[i] = 1
    print(f'X[{i}] = {valores[i]}')