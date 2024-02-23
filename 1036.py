import math
A,B,C = map(float, input().split())

delta = (B**2) - (4*A*C)

if delta > 0 and A != 0:
    r1 = (-B + math.sqrt(delta)) / (2*A) 
    r2 = (-B - math.sqrt(delta)) / (2*A)    
    print(f'R1 = {r1:.5f}')
    print(f'R2 = {r2:.5f}')
else:
    print('Impossivel calcular')