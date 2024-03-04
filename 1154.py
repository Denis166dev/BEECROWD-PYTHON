soma = 0
q = 0
while True:
    N = int(input())
    if N < 0:
        break
    else:
        soma += N
        q += 1
print(f'{soma/q:.2f}')