total = 0

for _ in range(5):
    numero = float(input())
    if numero%2 == 0:
        total += 1

print(f'{total} valores pares')