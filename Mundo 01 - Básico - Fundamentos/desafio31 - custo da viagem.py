distancia = float(input(('Qual a distancia da sua viagem em km? ')))
if distancia <=200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('O preço de uma viagem de {:.2f} km, é de R$ {:.2f}'.format(distancia, preco))
