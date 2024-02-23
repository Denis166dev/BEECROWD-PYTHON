P1 = input().split(' ')
P2 = input().split(' ')

c1,n1,v1 = P1
c2,n2,v2 = P2

pagar = (int(n1)*float(v1)) + (int(n2)*float(v2))
print(f'VALOR A PAGAR: R$ {pagar:.2f}')