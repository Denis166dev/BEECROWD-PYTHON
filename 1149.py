valores = input().split()

A = int(valores[0])
ultimov = len(valores) - 1
N = int(valores[ultimov])

soma = 0

for i in range(0,N):
    soma += A + i

print(soma)