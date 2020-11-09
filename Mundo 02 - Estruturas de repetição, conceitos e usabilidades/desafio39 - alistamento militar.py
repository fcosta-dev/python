from datetime import date
atual = date.today().year
ano = int(input('Digite o ano do nascimento do jovem: '))
if (atual - ano) == 18:
    print('Ele tem {} anos! Já está no tempo de se alistar'.format(atual-ano))
elif (atual - ano) >18:
    print('Ele tem {} anos! Já passou {} anos do tempo de se alistar!'.format((atual - ano),((atual - ano)-18)))
else:
    print('Ele tem {} anos! Ele ainda vai se alistar, falta {} anos!'.format((atual - ano), (18-(atual - ano))))
