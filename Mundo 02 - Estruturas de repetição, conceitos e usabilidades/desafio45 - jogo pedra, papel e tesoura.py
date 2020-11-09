from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Suas opções:
 [ 0 ] PEDRA
 [ 1 ] PAPEL
 [ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-='*11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-='*11)
if computador == 0: # computador jogou PEDRA
    if jogador == 0: #jogador jogou PEDRA
        print('EMPATE')
    elif jogador == 1: #jogador jogou PAPEL
        print('JOGADOR VENCE')
    elif jogador == 2: #jogador jogou TESOURA
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 1: # computador jogou PAPEL
    if jogador == 0: #jogador jogou PEDRA
        print('COMPUTADOR VENCE')
    elif jogador == 1: #jogador jogou PAPEL
        print('EMPATE')
    elif jogador == 2: #jogador jogou TESOURA
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
elif computador ==2: # computador jogou TESOURA
    if jogador == 0: #jogador jogou PEDRA
        print('JOGADOR VENCE')
    elif jogador == 1: #jogador jogou PAPEL
        print('COMPUTADOR VENCE')
    elif jogador == 2: #jogador jogou TESOURA
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')
