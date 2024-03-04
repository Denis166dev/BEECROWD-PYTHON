X = int(input())
Y = int(input())

maior = max(X,Y)
menor = min(X,Y)

for i in range(menor+1, maior):
    if i%5 == 2 or i%5 == 3:
        print(i)