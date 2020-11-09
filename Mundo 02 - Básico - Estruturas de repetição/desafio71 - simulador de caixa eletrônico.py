print('*'*60)
print('Banco Costa')
print('*'*60)

dinheiro =0
valor = int(input('Digite o valor a ser sacado: R$ '))
dinheiro = valor
notasde50 = valor // 50
dinheiro = dinheiro - (notasde50 * 50)
notasde20 = dinheiro // 20
dinheiro = dinheiro - (notasde20 * 20)
notasde10 = dinheiro // 10
dinheiro = dinheiro - (notasde10 * 10)
notasde1 = dinheiro // 1
dinheiro = dinheiro - (notasde1 * 1)

if notasde50 != 0:
    print(f'Total de {notasde50} cédulas de R$ 50.00!')
if notasde20 != 0:
    print(f'Total de {notasde20} cédulas de R$ 20.00!')
if notasde10 != 0:
    print(f'Total de {notasde10} cédulas de R$ 10.00!')
if notasde1 != 0:
    print(f'Total de {notasde1} cédulas de R$ 1.00!')