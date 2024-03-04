while True:
    senha = int(input())

    if senha == 2002:
        print('Acesso Permitido')
        break
    elif senha != 2002:
        print('Senha Invalida')