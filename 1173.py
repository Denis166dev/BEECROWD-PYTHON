V = int(input())
valores  = [V]
valorant = 0

for _ in range(9):
    valorant = valores[-1]
    valores.append(valorant*2)

for i in range(10):
    print(f'N[{i}] = {valores[i]}')