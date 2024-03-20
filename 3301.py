H,Z,L = map(int, input().split())

maior = max(H,Z,L)
menor = min(H,Z,L)
meio = (H+Z+L) - maior - menor

if meio == H:
    print('huguinho')
elif meio == Z:
    print('zezinho')
else:
    print('luisinho')