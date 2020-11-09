n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
if n1 > n2:
    print('O PRIMEIRO valor, {}, é MAIOR!'.format(n1))
elif n2 > n1:
    print('O SEGUNDO valor, {}, é MAIOR!'.format(n2))
else:
    print('Não existe valor maior, os números {} e {} são IGUAIS!'.format(n1, n2))