I = 0
J = [1,2,3]

while I <= 2:
    for i in J:
        if abs(I - round(I)) < 0.01:
            print(f'I={round(I)} J={round(i)}')
        else:
            print(f'I={I:.1f} J={i:.1f}')

    I += 0.2
    J = [x + 0.2 for x in J]