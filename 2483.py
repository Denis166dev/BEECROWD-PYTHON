I = int(input())

frase = 'Feliz natal!'
a = ''

for _ in range(I):
    a += 'a'

novafrase = frase[:9]+a+frase[10:]
print(novafrase)