x,y = map(float, input().split())

if x == 0.0 and y == 0.0:
    print('Origem')
elif abs(x) >= 0.1 and y == 0.0:
    print('Eixo X')
elif x == 0.0 and abs(y) >= 0.1:
    print('Eixo Y')
elif x > 0.0 and y > 0.0:
    print('Q1')
elif x < 0.0 and y > 0.0:
    print('Q2')
elif x < 0.0 and y < 0.0:
    print('Q3')
elif x > 0.0 and y < 0.0:
    print('Q4')