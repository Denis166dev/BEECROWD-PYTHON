def mdc(a, b):
    while b != 0:
        a, b = b, a % b
    return a

N = int(input())

for _ in range(N):
    F1, F2 = map(int, input().split())
    print(mdc(F1, F2))