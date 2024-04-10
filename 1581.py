N = int(input())

for _ in range(N):
    K = int(input())
    list = []
    for _ in range(K):
        S = input()
        list.append(S)
    sete = set(list)
    if len(sete) == 1:
        print(next(iter(sete)))
    else:
        print('ingles')