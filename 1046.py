I,F = map(int, input().split())

if I < F:
    duracao = F - I
else:
    duracao = 24 - I + F

print(f'O JOGO DUROU {duracao} HORA(S)')