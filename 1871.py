while True:
    N,M = map(int, input().split())
    if N == M == 0:
        break
    else:
        soma = N + M
        semzero = str(soma)
        semzero = semzero.replace('0','')
        print(semzero)