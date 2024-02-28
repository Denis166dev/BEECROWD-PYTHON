COD, QTD = map(int, input().split())

if COD == 1:
    print(f'Total: R$ {(QTD*4):.2f}')
elif COD == 2:
    print(f'Total: R$ {(QTD*4.5):.2f}')
elif COD == 3:
    print(f'Total: R$ {(QTD*5):.2f}')
elif COD == 4:
    print(f'Total: R$ {(QTD*2):.2f}')
elif COD == 5:
    print(f'Total: R$ {(QTD*1.5):.2f}')