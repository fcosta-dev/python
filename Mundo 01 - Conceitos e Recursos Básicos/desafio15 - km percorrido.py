kmrodado = float(input('Qual a quantidade de km percorridos pelo carro alugado? '))
qtddias = int(input('Qual a quantidade de dias pelos quais ele foi alugado? '))

print('O preço total é de R$ {2}, sendo que R$ {1} é pelo dia utilizado, e R$ {0} é pelo km rodado!'.format((kmrodado*0.15), (qtddias*60), (kmrodado*0.15+qtddias*60)))
