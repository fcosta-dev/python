salario = float(input('QUal o salário do funcionário? '))
if salario > 1250:
    print('O aumento salarial será de 10%, totalizando novo salario em R$ {:.2f}'.format(salario*1.10))
else:
    print('O aumento salarial será de 15%, totalizando novo salario em R$ {:.2f}'.format(salario*1.15))
