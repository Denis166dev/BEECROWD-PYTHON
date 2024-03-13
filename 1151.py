N = int(input())

valores = [0,1]

while len(valores) < N:
    prox_num = valores[-1] + valores[-2]
    valores.append(prox_num)

    valores_str = ' '.join(map(str, valores[:N]))

print(valores_str)