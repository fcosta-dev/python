from datetime import date
atual = date.today().year
nascimento = int(input('Digite o ano de nascimento do atleta: '))
idade = (atual - nascimento)
if idade <= 9:
    print('Aluno tem {} anos. Sua categoria é: Mirim!'.format(idade))
elif idade <= 14:
    print('Aluno tem {} anos. Sua categoria é: Infantil!'.format(idade))
elif idade <= 19:
    print('Aluno tem {} anos. Sua categoria é: Junior!'.format(idade))
elif idade <= 25:
    print('Aluno tem {} anos. Sua categoria é: Senior!'.format(idade))
else:
    print('Aluno tem {} anos. Sua categoria é: Master!'.format(idade))
