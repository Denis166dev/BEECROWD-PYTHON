N = int(input())

dentro = 0
fora = 0

for _ in range(0,N):
    X = int(input())
    if X >= 10 and X <= 20:
        dentro += 1
    else:
        fora += 1
        
print(f'{dentro} in')
print(f'{fora} out')