HI,MI,HF,MF = map(int, input().split())

TI = HI * 60 + MI
TF = HF * 60 + MF

DT = (TF - TI + 24 * 60) % (24 * 60)

if HI == HF and MI == MF:
    DT = 24 * 60

DH = DT // 60
DM = DT % 60

print(f'O JOGO DUROU {DH} HORA(S) E {DM} MINUTO(S)')