N = int(input())

total = 0
totalC = 0
totalR = 0
totalS = 0

for _ in range(N):
    dados = input().split()

    Q = int(dados[0])
    E = dados[1]

    if E == 'C':
        totalC += Q
    elif E == 'R':
        totalR += Q
    elif E == 'S':
        totalS += Q

total = totalC+totalR+totalS

PC = (totalC*100)/total
PR = (totalR*100)/total
PS = (totalS*100)/total

print(f'Total: {total} cobaias')
print(f'Total de coelhos: {totalC}')
print(f'Total de ratos: {totalR}')
print(f'Total de sapos: {totalS}')
print(f'Percentual de coelhos: {PC:.2f} %')
print(f'Percentual de ratos: {PR:.2f} %')
print(f'Percentual de sapos: {PS:.2f} %')