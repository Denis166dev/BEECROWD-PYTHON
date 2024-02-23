nome = str(input())
salario = float(input())
vendas = float(input())

porcentagem = vendas*0.15
salariof = salario + porcentagem

print(f'TOTAL = R$ {salariof:.2f}')