numero = int(input('Digite um número inteiro: '))
escolha = int(input("""Escolha uma base de conversão abaixo
              1 - converter para binário
              2 - converter para octal
              3 - converter para hexadecimal
              Escolha: """))
if escolha == 1:
    print('Calculo do número inteiro {} para binário é: {}'.format(numero,bin(numero)[2:]))
elif escolha == 2:
    print('Calculo do número inteiro {} para octal é: {}'.format(numero, oct(numero)[2:]))
elif escolha == 3:
    print('Calculo do número inteiro {} para hexadecimal é: {}'.format(numero, hex(numero)[2:]))
else:
    print('Você digitou uma opção inválida!')
