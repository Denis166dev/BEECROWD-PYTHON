N = int(input())

for _ in range(0,N):
    X,Y = map(int, input().split())
    soma = 0
    if X%2 == 0:
        X+=1
    for _ in range(Y):
        soma+=X
        X+=2
    print(soma)