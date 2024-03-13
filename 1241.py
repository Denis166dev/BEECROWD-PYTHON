N = int(input())

for _ in range(N):
    A,B = map(str, input().split())

    if A.endswith(B):
        print('encaixa')
    else:
        print('nao encaixa')