maior = 0
posicao = 0

for i in range(1,101):
    numero = int(input())
    if numero > maior:
        maior = numero
        posicao = i
    
print(maior)
print(posicao)