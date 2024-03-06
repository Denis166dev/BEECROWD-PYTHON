H,Z,L = map(int, input().split())

if H > Z and H < L:
    print('huguinho')
elif Z > H and Z < L:
    print('zezinho')
elif L < H and L > Z:
    print('luisinho')