contagem = 0
acumulador = 0

while True:

    N = float(input())
    

    if N < 0 or N > 10:
        print('nota invalida')

    elif N >= 0 and N <= 10:
        acumulador += N
        contagem += 1
        
        if contagem == 2:
            print(f'media = {(acumulador/2):.2f}')
            break