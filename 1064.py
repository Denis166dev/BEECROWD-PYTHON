total = 0
media = 0
for _ in range(6):
    numero = float(input())
    if numero > 0:
        total += 1
        media += numero
mediaf = media/total

print(f'{total} valores positivos')
print(f'{mediaf:.1f}')