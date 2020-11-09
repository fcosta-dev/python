total = 0
produtomaisbarato = ""
precoprodutomaisbarato = 0
produtosmaisdemil = 0
c = 0
while True:
    print('='*40)
    produto = str(input('Digite o produto: '))
    preco = float(input('Digite o preço: R$ '))
    total = total + preco
    if preco > 1000:
        produtosmaisdemil += 1
    if c == 0 or preco < precoprodutomaisbarato:
        produtomaisbarato = produto
        precoprodutomaisbarato = preco
    c += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
print('{:=^50}'.format(' FIM DO PROGRAMA '))
print(f'O total gasto na compra foi de R$ {total:.2f}!')
print(f'{produtosmaisdemil} produtos custam mais de R$ 1.000.00!')
print(f'O produto mais barato é a {produtomaisbarato} no valor de R$ {precoprodutomaisbarato:.2f}!')
print(f'Total de {c} produtos cadastrados!')