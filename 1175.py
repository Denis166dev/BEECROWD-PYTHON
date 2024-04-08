valores = [int(input()) for _ in range(20)]
valores_invertidos = [0]*20
for i in range(20):
    valores_invertidos[i] = valores[-(i+1)]
    print(f'N[{i}] = {valores_invertidos[i]}')