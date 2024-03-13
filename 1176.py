N = int(input())

for _ in range(0,N):
    A = int(input())
    valores = [0,1]

    while len(valores) < A + 1:
        prox_num = valores[-1] + valores[-2]
        valores.append(prox_num)

    print(f'Fib({A}) = {valores[A]}')