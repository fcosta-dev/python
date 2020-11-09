cmulheres_20 = 0
somaidade = 0
media = 0
homem_mais_velho_idade = 0
for c in range(1,5):
    nome = str(input('Digite o nome da {}ª pessoa: '.format(c))).strip()
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo: (M, F, G): ')).strip()
    print('=' * 30)

    #Calculo de média
    somaidade += idade

    #Calculo mulheres com menos de 20 anos
    if sexo in 'Ff' and idade <20:
        cmulheres_20 += 1

    #Calculo de qual o nome do homem mais velho
    if sexo in 'Mm':
        if homem_mais_velho_idade < idade:
            homem_mais_velho_nome = nome
            homem_mais_velho_idade = idade

media = somaidade/4
print('A média de idade do grupo é de: {:.1f} anos'.format(media))
if homem_mais_velho_idade == "":
    print('Não há homem neste range.')
else:
    print('O homem mais velho é {}, com {} anos.'.format(homem_mais_velho_nome.capitalize(), homem_mais_velho_idade))
print('Neste grupo tem {} mulher(es) com menos de 20 anos.'.format(cmulheres_20))