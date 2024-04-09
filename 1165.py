N = int(input())

for _ in range(N):
    X = int(input())
    i = 2
    while i < X:
        if X % i == 0:
            break
        i += 1

    if i == X:
        print(f'{X} eh primo')
    else:
        print(f'{X} nao eh primo')