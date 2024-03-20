N = int(input())

for _ in range(N):
    valor = str(input())
    contador = 0
    for i in valor:
        if i == '1':
            contador+=2
        elif i == '2':
            contador+=5
        elif i == '3':
            contador+=5
        elif i == '4':
            contador+=4
        elif i == '5':
            contador+=5
        elif i == '6':
            contador+=6
        elif i == '7':
            contador+=3
        elif i == '8':
            contador+=7
        elif i == '9':
            contador+=6
        elif i == '0':
            contador+=6

    print(f'{contador} leds')