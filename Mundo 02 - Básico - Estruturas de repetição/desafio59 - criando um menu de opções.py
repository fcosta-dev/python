from random import randint
from time import sleep
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

opcao = '1'
while opcao in '1' or '2' or '3' or '4':
    print('='*40)
    opcao = input('''Com estes números você deseja:
        [1] - Somar
        [2] - Multiplicar
        [3] - Saber qual maior
        [4] - Gerar novos números
        [5] - Digitar novos números
        [6] - Sair do Programa
        Digite uma opção válida: ''')
    if opcao == '1':
        print('A soma de {} com {}, é: {}.'.format(n1, n2,(n1+n2)))
    elif opcao == '2':
        print('A multiplicação de {} com {}, é: {}.'.format(n1, n2, (n1 * n2)))
    elif opcao == '3':
        if n1 > n2:
            print('O maior valor entre {} e {}, é: {}.'.format(n1, n2, n1))
        else:
            print('O maior valor entre {} e {}, é: {}.'.format(n1, n2, n2))
    elif opcao == '4':
        n1 = randint(1,10)
        n2 = randint(1,10)
        print('Os novos valores são {} e {}.'.format(n1, n2))
    elif opcao == '5':
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    elif opcao == '6':
        print('Fechando o Programa...')
        sleep(2)
    else:
        opcao = '1'
        print('Opção Inválida.')
print('FIM')