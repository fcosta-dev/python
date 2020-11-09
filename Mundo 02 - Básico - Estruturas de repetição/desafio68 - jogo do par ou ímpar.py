from random import randint
print('-'*40)
print('PROGRAMA PAR OU IMPAR')
print('-'*40)
conquistas = 0
perdas = 0
minhavez_suavez = 0
numerojogado = 0 #jogador é 0 e computador é 1
while True:
    if minhavez_suavez == 0:
        print('É a vez do Jogador: ')
        minhavez_suavez = 1 #A próxima é a vez do computador.
        while True:
            jogador = str(input('JOGADOR: Digite [PAR] ou [IMPAR]: ')).strip().upper()
            if jogador == 'PAR':
                computador = 'IMPAR'
                break
            elif jogador == 'IMPAR':
                computador = 'PAR'
                break
            else:
                'OPÇÃO ERRADA! Digite Novamente!'
    elif minhavez_suavez == 1:
        print('-' * 40)
        print('É a vez do Computador: ')
        minhavez_suavez = 0 #A próxima é a vez do jogador.
        jogo = ['Par', 'Impar']
        opcao = randint(0, 1)
        computador = jogo[opcao].upper()
        print(f'O computador escolhe: {computador}!')
        if computador == 'PAR':
            print('O jogador é IMPAR!')
        else:
            print('O Jogador é PAR!')
    computador_jogada = randint(0,11)
    jogador_jogada = int(input('JOGADOR digite seu número: '))
    numerojogado = computador_jogada + jogador_jogada
    if (numerojogado % 2) == 0:
        # Se for par
        if computador == 'PAR':
            print(f'COMPUTADOR GANHOU! O numero jogado pelo JOGADOR é {jogador_jogada}, e o número do COMPUTADOR é {computador_jogada}. O total é: {jogador_jogada + computador_jogada}, e o número é PAR!')
            print('-'*50)
            print(f'JOGO ACABOU! O JOGADOR ganhou {conquistas} vezes!')
            break
        if computador == 'IMPAR':
            print(f'JOGADOR GANHOU! O numero jogado pelo JOGADOR é {jogador_jogada}, e o número do COMPUTADOR é {computador_jogada}. O total é: {jogador_jogada + computador_jogada}, e o número é PAR!')
            print('-' * 40)
            conquistas += 1
    elif (numerojogado % 2) == 1:
        # Se for impar
        if computador == 'IMPAR':
            print(f'COMPUTADOR GANHOU! O numero jogado pelo JOGADOR é {jogador_jogada}, e o número do COMPUTADOR é {computador_jogada}. O total é: {jogador_jogada + computador_jogada}, e o número é IMPAR!')
            print('-' * 50)
            print(f'JOGO ACABOU! O JOGADOR ganhou {conquistas} vezes!')
            break
        if computador == 'PAR':
            print(f'JOGADOR GANHOU! O numero jogado pelo JOGADOR é {jogador_jogada}, e o número do COMPUTADOR é {computador_jogada}. O total é: {jogador_jogada + computador_jogada}, e o número é IMPAR!')
            print('-' * 40)
            conquistas += 1
        # Se for impar
        par = False
        impar = True
print('FIM')