from datetime import date

atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1,8):
    nasc = int(input('Em que ano a {} pessoa nasceu? '.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('E também tivemos {} pessoas menores de idade'.format(totmenor))



ano = date.today().year
maioridade = ""
menoridade = ""
qtdmaioridade = 0
qtdmenoridade = 0
for c in range(0,8):
    nome = str(input('Digite o nome da pessoa {}: '.format(c+1)))
    nascimento = int(input('Nascimento: '))
    if ano - nascimento >= 18:
        if qtdmaioridade == 0:
            maioridade = ('{}, {} {} anos.'.format(nome.capitalize(), "com", (ano-nascimento)))
        else:
            maioridade = maioridade, ('{}, {} {} anos.'.format(nome.capitalize(), "com", (ano-nascimento)))
        qtdmaioridade = qtdmaioridade +1
    else:
        if qtdmenoridade == 0:
            menoridade = ('{}, {} {} anos.'.format(nome.capitalize(), "com", (ano-nascimento)))
        else:
            menoridade = menoridade, ('{}, {} {} anos.'.format(nome.capitalize(), "com", (ano-nascimento)))

        qtdmenoridade = qtdmenoridade +1
print('Pessoas com maioridade são {}. E elas são: {}'.format(qtdmaioridade, maioridade))
print('Pessoas com menoridade são {}. E elas são: {}'.format(qtdmenoridade, menoridade))