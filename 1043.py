A,B,C = map(float, input().split())

if A+B > C and A+C > B and B+C > A:
    print(f'Perimetro = {(A+B+C):.1f}')
else:
    print(f'Area = {(((A+B)*C)/2):.1f}')