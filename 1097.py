I = 1
J = [7,6,5]

while I <= 9:
    for i in J:
        print(f'I={I} J={i}')
    I += 2
    J = [x + 2 for x in J]