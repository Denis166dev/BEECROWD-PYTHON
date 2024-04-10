N = int(input())

for _ in range(N):

    cont = 0
    palavra = input()
    if len(palavra) > 3:
        print(3)
    else:
        if palavra[0] == 'o':
            cont+=1
        if palavra[1] == 'n':
            cont+=1
        if palavra[2] == 'e':
            cont+=1
        if cont >= 2:
            print(1)
        else:
            print(2)