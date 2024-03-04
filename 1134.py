A = 0
G = 0
D = 0

while True:
    O = int(input())

    if O == 1:
        A += 1
    elif O == 2:
        G += 1
    elif O == 3:
        D +=1
    elif O == 4:
        break

print('MUITO OBRIGADO')
print(f'Alcool: {A}')
print(f'Gasolina: {G}')
print(f'Diesel: {D}')