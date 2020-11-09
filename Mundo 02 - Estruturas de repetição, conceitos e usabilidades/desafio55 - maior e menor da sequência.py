nome_maior = ""
peso_maior = 0
nome_menor = ""
peso_menor = 0
for c in range(1,6):
    nome = str(input('Digite o nome da {}ª pessoa: '.format(c)))
    peso = float(input('Digite o peso em kg: '))
    if c == 1:
        nome_maior = nome
        nome_menor = nome
        peso_maior = peso
        peso_menor = peso
    else:
        if peso_maior < peso:
            nome_maior = nome
            peso_maior = peso
        if peso_menor > peso:
            nome_menor = nome
            peso_menor = peso
print('O maior peso foi de {}, com {}kg'.format(nome_maior.capitalize(),peso_maior))
print('O menor peso foi de {}, com {}kg'.format(nome_menor.capitalize(),peso_menor))
