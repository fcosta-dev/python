sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, Digite o sexo: [M/F]: ')).upper()
print('Sexo {} registrado com sucesso.'.format(sexo))
