N1,N2,N3,N4 = map(float, input().split())

media = ((N1*2)+(N2*3)+(N3*4)+(N4*1))/10

if media >= 5.0 and media <= 6.9:
    NE = float(input())
    NM = (media+NE)/2
    print(f'Media: {media:.1f}')
    print('Aluno em exame.')
    print(f'Nota do exame: {NE:.1f}')
    if NM >= 5.0:
        print('Aluno aprovado.')
    elif NM <= 4.9:
        print('Aluno reprovado.')
    print(f'Media final: {NM:.1f}')

elif media >= 7.0:
    print(f'Media: {media:.1f}')
    print('Aluno aprovado.')

elif media < 5.0:
    print(f'Media: {media:.1f}')
    print('Aluno reprovado.')