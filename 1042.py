A,B,C = map(int, input().split())

voriginais = [A,B,C]

vcrescentes = sorted([A,B,C])

for numero in vcrescentes:
    print(numero)

print()

for numero in voriginais:
    print(numero)