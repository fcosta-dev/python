from time import sleep
from random import randint
computador = randint(0 , 10) #Faz o computador "PENSAR NO NUMERO"
print('-=-' * 20)
numero = int(input('Adivinhe um número de 0-10: '))
print('PROCESSANDO...')
sleep(1)  # aguarda 1 segundos
c = 1
while numero != computador:
    numero = int(input('Número incorreto! Tente novamente: '))
    c += 1
    print('PROCESSANDO...')
    sleep(1) #aguarda 1 segundos
print('Parabens! Você acertou o número {}, depois de {} tentativas.'.format(computador, c))
print('FIM')
