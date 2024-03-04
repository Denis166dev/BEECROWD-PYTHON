N = int(input())

for _ in range(0,N):
    numero = int(input())
    if numero == 0:
        print('NULL')
    elif numero > 0 and numero%2 == 0:
        print('EVEN POSITIVE')
    elif numero < 0 and numero%2 == 0:
        print('EVEN NEGATIVE')
    elif numero > 0 and numero%2 != 0:
        print('ODD POSITIVE')
    elif numero < 0 and numero%2 != 0:
        print('ODD NEGATIVE')