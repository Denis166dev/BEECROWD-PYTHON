X = int(input())
Y = int(input())

maior = max(X,Y)
menor = min(X,Y)
soma = 0

for i in range(menor, maior+1):
    if i%13 != 0:
        soma  += i
print(soma)