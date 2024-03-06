C1,C2,C3,C4 = map(int, input().split())

lista = [C1,C2,C3,C4]
acumulador = 0

for i in lista:
    if i == 0:
        acumulador+=1
    elif i == 1:
        print(acumulador+1)