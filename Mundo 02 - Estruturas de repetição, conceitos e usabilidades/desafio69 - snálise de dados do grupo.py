pessoasmais18anos = 0
homens = 0
mulheresmenos20anos = 0
sexo = ''
continuar = 'S'
while True:
    idade = int(input('Digite idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite seu sexo: [M/F]: ')).strip().upper()[0]
    if (idade >= 18):
        pessoasmais18anos += 1
    if (idade < 20) and sexo == 'F':
        mulheresmenos20anos += 1
    if (sexo == 'M'):
        homens += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Deseja continuar o cadastro? [S/N]').strip().upper()[0]
    if continuar == 'N':
        break
print(f'O cadastro possui {pessoasmais18anos} pessoas com mais de 18 anos!')
print(f'O cadastro possui {mulheresmenos20anos} mulheres com menos de 20 anos!')
print(f'O cadastro possui {homens} homens cadastrados.')
print('PROGRAMA ACABOU!')