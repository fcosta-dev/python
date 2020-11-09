print('{:=^60}'.format(' LOJAS COSTA '))
valor = float(input('Qual o valor a ser pago pelo produto: R$ '))
print('*'*60)
print('Condições de pagamento')
print('*'*60)
condicao = int(input("""Escolha a sua condição de pagamento abaixo
            1 - Pagamento à Vista em Dinheiro/Cheque (10% de desconto)
            2 - Pagamento à Vista no Cartão (5% de desconto)
            3 - Pagamento em 2x no Cartão (Preço normal)
            4 - Pagamento em 3x ou mais no Cartão (20% de juros)
        """))
if condicao == 1:
    print('Você escolheu pagar em Dinheiro. Ganhou R$ {:.2f} de desconto. O valor a pagar é de R$ {:.2f}!'.format((valor*0.10),(valor*0.90)))
elif condicao == 2:
    print('Você escolheu pagar à vista no Cartão. Ganhou R$ {:.2f} de desconto. O valor a pagar é de R$ {:.2f}!'.format((valor*0.05), (valor*0.95)))
elif condicao == 3:
    print('Você escolheu pagar em 2x no Cartão. Não há desconto, e o valor a pagar é de R$ {:.2f}!'.format(valor))
elif condicao == 4:
    print('Você escolheu pagar em 3x ou mais no Cartão. Foi acrescido o valor de R$ {:.2f} referente 20% de juros. O valor a pagar é de R$ {:.2f}'.format((valor*0.20), valor*1.20))
else:
    print('Opção inválida.')
