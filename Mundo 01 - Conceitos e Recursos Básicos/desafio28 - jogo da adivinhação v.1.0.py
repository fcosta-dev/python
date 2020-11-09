from random import randint
from time import sleep
computador = randint(0 , 5) #Faz o computador "PENSAR NO NUMERO"
print('-=-' * 20)
if input('Adivinhe um número de 0-5: ') == computador:
    print('PROCESSANDO...')
    sleep(2) #aguarda 2 segundos
    print('Parabens! Você acertou o número')
else:
    print('PROCESSANDO...')
    sleep(2) #aguarda 2 segundos
    print('Tente novamente, o número correto é: {}'.format(computador))
print('FIM')
