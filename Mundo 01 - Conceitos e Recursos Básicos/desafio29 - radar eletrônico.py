velocidade = float(input('Digite a velocidade do carro: '))
if velocidade > 80:
    print('Você está acima de 80km/h, foi multado!')
    print('A multa é de R$ {:.2f} !'.format(7*(velocidade-80)))
else:
    print('Sua velocidade está dentro do limite. Parabens!')