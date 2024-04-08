while True:
    try:
        H = input().split(':')
        hora = int(H[0])
        minuto = int(H[1])

        if hora < 7:
            print('Atraso maximo: 0')
        else:
            atraso = ((hora - 7) * 60) + minuto
            print('Atraso maximo:', atraso)
    except EOFError:
        break