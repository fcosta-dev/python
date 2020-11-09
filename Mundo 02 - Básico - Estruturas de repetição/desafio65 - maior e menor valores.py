n = int(input('Digite um número: '))
maior = n
menor = n
media = n
soma = n
c = 1
SN = str(input('* Deseja continuar? [S/N]')).strip()[0]
while SN not in 'SsNn':
    print('Resposta inválida.')
    SN = str(input('* Deseja continuar? ')).strip()[0]

while SN in 'Ss':
    n = int(input('Digite um número: '))
    if maior < n:
        maior = n
    if menor > n:
        menor = n
    c += 1
    soma = soma + n
    SN = str(input('* Deseja continuar? ')).strip()[0]
    while SN not in 'SsNn':
        print('Resposta inválida.')
        SN = str(input('Deseja continuar? ')).strip()[0]

media = (soma / c)
print('------> O MENOR número é {}.'.format(menor))
print('------> O MAIOR número é {}.'.format(maior))
print('------> A MÉDIA entre os números é {:.0f}.'.format(media))
print('------> A somatória entre eles é: {}!'.format(soma))
