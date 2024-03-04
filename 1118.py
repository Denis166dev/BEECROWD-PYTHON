while True:
    contagem = 0
    acumulador = 0

    while contagem < 2:
        nota = float(input())
        
        if nota < 0 or nota > 10:
            print('nota invalida')
        else:
            acumulador += nota
            contagem += 1

    print(f'media = {(acumulador / 2):.2f}')

    opcao = 0
    while opcao != 1 and opcao != 2:
        print("novo calculo (1-sim 2-nao)")
        opcao = int(input())

    if opcao == 2:
        break         