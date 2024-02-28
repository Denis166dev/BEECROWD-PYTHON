total = 0

for _ in range(6):
    numero = float(input())
    if numero > 0:
        total += 1

print(f'{total} valores positivos')