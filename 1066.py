totalP = 0
totalI = 0
totalPosi = 0
totalNega = 0

for _ in range(5):
    numero = float(input())
    if numero%2 == 0:
        totalP += 1
    else:
        totalI += 1
    if numero > 0:
        totalPosi += 1
    elif numero < 0:
        totalNega += 1
    

print(f'{totalP} valor(es) par(es)')
print(f'{totalI} valor(es) impar(es)')
print(f'{totalPosi} valor(es) positivo(s)')
print(f'{totalNega} valor(es) negativo(s)')