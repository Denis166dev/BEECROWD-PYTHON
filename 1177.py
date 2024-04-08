T = int(input())
listat = []

for i in range(1000):
    listat.append(i%T)
    
for j in range(1000):
    print(f'N[{j}] = {listat[j]}')