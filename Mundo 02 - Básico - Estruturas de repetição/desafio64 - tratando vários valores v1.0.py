n = int(input('Digite um número: '))
c = 1
soma = n
while n != 999:
    n = int(input('Digite um número: '))
    if n != 999:
        c += 1
        soma += n
print('Foram digitados {} números.'.format(c))
print('A somatória entre eles é: {}!'.format(soma))
