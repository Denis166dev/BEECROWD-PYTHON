N = int(input())
X = list(map(int, input().split()))

menor = X[0]
posicao = 0

for i in range(1, N):
    if X[i] < menor:
        menor = X[i]
        posicao = i

print(f'Menor valor: {menor}')
print(f'Posicao: {posicao}')