import math

while True:
    soma = 0
    try:
        M,N = map(int, input().split())
        soma = math.factorial(M) + math.factorial(N)
        print(soma)
    except EOFError:
        break