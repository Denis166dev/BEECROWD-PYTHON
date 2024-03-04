totalg = 0
VI = 0
VG = 0
E = 0
while True:
    I,G = map(int, input().split())
    
    totalg += 1
    if I > G:
        VI +=1
    elif I < G:
        VG += 1
    elif I == G:
        E += 1

    print("Novo grenal (1-sim 2-nao)")
    opcao = int(input())

    if opcao == 2:
       break

print(f'{totalg} grenais')
print(f'Inter: {VI}')
print(f'Gremio: {VG}')
print(f'Empates: {E}')
if VI > VG:
    print('Inter venceu mais')
elif VI < VG:
    print('Gremio venceu mais')
else:
    print('Nao houve vencedor')