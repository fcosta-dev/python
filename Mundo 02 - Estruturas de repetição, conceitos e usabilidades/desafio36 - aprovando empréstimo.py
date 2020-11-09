valorcasa = float(input('Qual o valor da casa? R$ '))
salario = float(input('Qual o salário? R$ '))
pgtoanos = int(input('Em quantos anos será o pagamento? '))

valormensal = (valorcasa / (pgtoanos*12))

if valormensal > (salario * 0.30):
    print('Empréstimo negado! Pois o valor da prestação mensal de R$ {:.2f}, excede 30% do seu salário de R$ {:.2f}!'.format(valormensal, salario))
else:
    print('Empréstimo aprovado! O valor de sua prestação será de R$ {:.2f}!'.format(valormensal))