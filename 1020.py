dias = int(input())

ano = dias // 365
dias %= 365

mes = dias // 30
dias %= 30

print(f'{ano} ano(s)')
print(f'{mes} mes(es)')
print(f'{dias} dia(s)')