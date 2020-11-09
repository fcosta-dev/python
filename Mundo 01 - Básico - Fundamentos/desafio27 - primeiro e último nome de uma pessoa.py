n = str(input('Digite o nome da pessoa: ')).strip()
nome = n.split() #Separa o nome em pedaços
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é: {}'.format(nome[0]))
print('Seu último nome é: {}'.format(nome[len(nome)-1]))
